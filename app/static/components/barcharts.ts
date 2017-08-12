import {RepHistory} from "../models/barcharts/rephistory";
import {BarChartsBar} from "../models/barcharts/barchartsbar";
export abstract class BarCharts {
    protected exerciseHistory: Array<BarChartsBar>;
    protected svgs: any;

    protected static ANIMATION_TIME: number = 400;  // in milliseconds
    protected static TEXT_OFFSET: number = 4;
    protected static REP_MULTIPLIER: number = 6;
    protected static VERTICAL_OFFSET: number = 170;
    protected static VERTICAL_OFFSET_2: number = 200;
    protected static TEXT_ROTATION_DEGREES: number = 45;
    protected static IN_BETWEEN_SETS_GAP: number = 1;
    protected static IN_BETWEEN_DAYS_GAP: number = 7;
    protected static WEIGHT_BUFFER: number = 10;

    protected splitOutSets(): void {
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
    protected scaleWeights(): void {
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            this.exerciseHistory[i].setWidth(
                this.exerciseHistory[i].getWidth() + this.exerciseHistory[i].getWidthBuffer()
            );
        }
    }

    protected setUpViz(data: any): void {
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

    protected addOffsets(): number {
        let totalOffset: number = 0;
        let currentDate: string = null;
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            let thisDate: string = this.getXValue(this.exerciseHistory[i])
            if (currentDate) {
                if (currentDate == thisDate) {
                    totalOffset += BarCharts.IN_BETWEEN_SETS_GAP;
                } else {
                    totalOffset += BarCharts.IN_BETWEEN_DAYS_GAP;
                }
            }
            this.exerciseHistory[i].setXOffset(totalOffset);

            totalOffset += this.exerciseHistory[i].getWidth();

            this.exerciseHistory[i].setYOffset(BarCharts.VERTICAL_OFFSET
                - this.exerciseHistory[i].getHeight() * BarCharts.REP_MULTIPLIER);
            currentDate = thisDate;
        }
        return totalOffset;
    }

    protected abstract renderXAxis(): void;

    protected abstract convertJsonArrayToBarChartsBarArray(historyArray: Array<any>): Array<BarChartsBar>;

    protected abstract getXValue(element: BarChartsBar): string;
}
