import {RepHistory} from "../models/barcharts/rephistory";
import {BarChartsBar} from "../models/barcharts/barchartsbar";
import * as d3 from 'd3';
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
import {CSRFService} from "../services/csrfservice";

/**
 * Class that renders bar charts that express two dimensional data - one datum rendered as the width
 * of the bar and the other datum rendered as the height of the bar
 */
export abstract class BarCharts {
    // Private variables
    private svgs: any;
    private username: string;
    private exerciseHistory: Array<BarChartsBar>;
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_exercise_history: Observable<any>;

    // Protected variables
    protected endpointExercisePairsTarget: string;
    protected endpointExerciseHistoryTarget: string;
    protected chartSelector: string;
    protected pairs: Array<any>;

    // Constants
    private static ANIMATION_TIME: number = 400;  // in milliseconds
    private static TEXT_OFFSET: number = 4;
    private static REP_MULTIPLIER: number = 6;
    private static VERTICAL_OFFSET: number = 170;
    private static VERTICAL_OFFSET_2: number = 200;
    private static TEXT_ROTATION_DEGREES: number = 45;
    private static IN_BETWEEN_SETS_GAP: number = 1;
    private static IN_BETWEEN_DAYS_GAP: number = 7;


    constructor(protected http: Http, protected csrfService: CSRFService) {
    }

    protected prepareViz(): void {
        d3.select(this.chartSelector)
            .style('height', '400px')
            .style('width', '100%')
            .style('outline', '1px solid')
            .style('outline-offset', '10px')
            .style('overflow', 'scroll');
        this.svgs = d3.select(this.chartSelector).append('svg');
        this.endpoint_exercise_pairs = this.http.post(this.endpointExercisePairsTarget, '');
        this.endpoint_exercise_pairs.subscribe(
            data => {
                this.pairs = data.json().pairs;
                this.initPairsMap();
            },
            err => console.log(err)
        );
    }

    // Hook to initiate pairs map for by date charts
    protected initPairsMap(): void {
    }

    private splitOutSets(): void {
        let newArray: Array<BarChartsBar> = [];
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            for (let j = 0; j < this.exerciseHistory[i].getSets(); j++) {
                newArray.push($.extend(true, {}, this.exerciseHistory[i]));  // deep copy necessary here
            }
        }
        this.exerciseHistory = newArray;
    }

    /**
     * BarCharts.WEIGHT_BUFFER is added to every entries weight so that body weight exercises are not rendered
     * as 0-width bars
     */
    private scaleWeights(): void {
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            this.exerciseHistory[i].setWidth(
                this.exerciseHistory[i].getWidth() + this.exerciseHistory[i].getWidthBuffer()
            );
        }
    }

    protected makeServerCall(value: any) {
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFTOKEN', this.csrfService.getToken());
        this.endpoint_exercise_history = this.http.post(
            this.endpointExerciseHistoryTarget,
            JSON.stringify(this.generateDataToSendToServer(value)),
            {headers: headers}
        );
        this.endpoint_exercise_history.subscribe(
            data => {
                console.log(data);
                this.username = data.json().nickname;
                this.setUpViz(data);
            },
            err => console.log(err)
        )
    }

    private setUpViz(data: any): void {
        this.exerciseHistory = this.convertJsonArrayToBarChartsBarArray(data.json().history);
        this.splitOutSets();
        this.scaleWeights();
        let totalOffset = this.addOffsets();
        this.renderXAxis();
        this.svgs.attr('width', totalOffset)
            .attr('height', BarCharts.VERTICAL_OFFSET * 2);
        let bars = this.svgs.selectAll('g')
            .data(this.exerciseHistory);

        // Enter
        let barsEnter = bars.enter()
            .append('g')
            .attr('transform', (d: any, i: number) => 'translate(' + d.x_offset + ',' + d.y_offset + ')');
        barsEnter.append('rect')
            .style('fill', 'blue')
            .transition()
            .duration(BarCharts.ANIMATION_TIME)
            .attr('width', (d: RepHistory) => d.getWidth())
            .attr('height', (d: RepHistory) => d.getHeight() * BarCharts.REP_MULTIPLIER);
        barsEnter.append('text')
            .attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getWidth() / 2 + ','
            + -1 * BarCharts.TEXT_OFFSET + ')' + ' rotate(' + -1 * BarCharts.TEXT_ROTATION_DEGREES + ')')
            .transition()
            .duration(BarCharts.ANIMATION_TIME)  // Label (actual weight) shouldn't include buffer for UI purposes
            .text((d: RepHistory) => d.getHeight().toString() + ',' + (d.getWidth() - d.getWidthBuffer()).toString());

        // Update
        bars.attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getXOffset() + ',' + d.getYOffset() + ')');
        bars.select('rect')
            .transition()
            .duration(BarCharts.ANIMATION_TIME)
            .attr('width', (d: RepHistory) => d.getWidth())
            .attr('height', (d: RepHistory) => d.getHeight() * BarCharts.REP_MULTIPLIER);
        bars.select('text')
            .attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getWidth() / 2 + ','
            + -1 * BarCharts.TEXT_OFFSET + ')' + ' rotate(' + -1 * BarCharts.TEXT_ROTATION_DEGREES + ')')
            .transition()
            .duration(BarCharts.ANIMATION_TIME)  // Label (actual weight) shouldn't include buffer for UI purposes
            .text((d: RepHistory) => d.getHeight().toString() + ',' + (d.getWidth() - d.getWidthBuffer()).toString());

        // Exit
        let barsExit = bars.exit();
        barsExit.select('rect')
            .transition()
            .duration(400)
            .attr('height', 0);
        barsExit.transition()
            .delay(BarCharts.ANIMATION_TIME)
            .remove();
        barsExit.select('text')
            .remove();
    }

    private addOffsets(): number {
        let totalOffset: number = 0;
        let currentXValue: string = null;
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            let thisXValue: string = this.getXValue(this.exerciseHistory[i])
            if (currentXValue) {
                if (currentXValue == thisXValue) {
                    totalOffset += BarCharts.IN_BETWEEN_SETS_GAP;
                } else {
                    totalOffset += BarCharts.IN_BETWEEN_DAYS_GAP;
                }
            }
            this.exerciseHistory[i].setXOffset(totalOffset);

            totalOffset += this.exerciseHistory[i].getWidth();

            this.exerciseHistory[i].setYOffset(BarCharts.VERTICAL_OFFSET
                - this.exerciseHistory[i].getHeight() * BarCharts.REP_MULTIPLIER);
            currentXValue = thisXValue;
        }
        return totalOffset;
    }

    private renderXAxis(): void {
        this.svgs.selectAll('.date-text').remove();
        let iterA = 0;
        let iterB = 0;
        let extraOffset = 0;  // Space between the columns

        while (iterA < this.exerciseHistory.length) {
            iterB = iterA;
            let xValueA = this.getXValue(this.exerciseHistory[iterA]);

            // Find first differing x value
            while (iterB < this.exerciseHistory.length && this.getXValue(this.exerciseHistory[iterB]) == xValueA) {
                iterB++;
            }

            // Back up one to the last date that was the same
            iterB--;

            // Add in space between bars
            extraOffset += (iterB - iterA) * BarCharts.IN_BETWEEN_SETS_GAP;

            let middleXOffset = (this.exerciseHistory[iterA].getXOffset() + this.exerciseHistory[iterB].getXOffset()
                + extraOffset) / 2;
            this.svgs
                .append('text')
                .text(xValueA)
                .attr('class', 'date-text')
                .attr('text-anchor', 'end')
                .attr('transform', 'translate(' + String(middleXOffset) + ','
                    + String(BarCharts.VERTICAL_OFFSET_2) + ') rotate(-45)');

            iterA = iterB + 1;
            extraOffset += BarCharts.IN_BETWEEN_DAYS_GAP;
        }
    }

    protected abstract convertJsonArrayToBarChartsBarArray(historyArray: Array<any>): Array<BarChartsBar>;

    /**
     * Each child class gets the value that is used on the X axis. In by taxonomy charts this is the date, and in
     * by date charts this is the id.
     */
    protected abstract getXValue(element: BarChartsBar): string;

    /**
     * The params sent down to the server are different based on whether the chart is rep history time history
     */
    protected abstract generateDataToSendToServer(value: any): Object;
}
