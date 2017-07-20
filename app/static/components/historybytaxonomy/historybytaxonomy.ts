import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
import {CSRFService} from "../../services/csrfservice";
import * as d3 from 'd3';

@Component({
    selector: 'history-by-taxonomy',
    templateUrl: '/static/components/historybytaxonomy/historybytaxonomy.html'
})
export class HistoryByTaxonomyComponent {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_taxonomy: Observable<any>;
    private pairs: Array<any>;
    private exerciseHistory: Array<RepHistoryObject>;
    private username: string;
    private svgs: any;

    private static ANIMATION_TIME: number = 400;  // in milliseconds
    private static TEXT_OFFSET: number = 4;
    private static REP_MULTIPLIER: number = 6;
    private static VERTICAL_OFFSET: number = 170;

    constructor(private http: Http, private csrfService: CSRFService) {
        this.endpoint_exercise_pairs = http.post('/get-valid-id-exercise-pairs', '');
    }

    ngOnInit() {
        this.svgs = d3.select('.chart').append('svg');
        this.endpoint_exercise_pairs.subscribe(
            data => {
                this.pairs = data.json().pairs;
            },
            err => console.log(err)
        );
    }

    onChange(value: any) {
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFTOKEN', this.csrfService.getToken());
        let data: any = {};
        data.exercise_id = value.exercise_id;
        this.endpoint_history_by_taxonomy = this.http.post(
            '/history-by-taxonomy',
            JSON.stringify(data),
            {headers: headers}
        );
        this.endpoint_history_by_taxonomy.subscribe(
            data => {
                this.username = data.json().nickname;
                this.exerciseHistory = this.convertJsonArrayToObjectArray(data.json().history);
                this.splitOutSets();
                let totalOffset = this.addOffsets();
                this.svgs.attr('width', totalOffset)
                    .attr('height', HistoryByTaxonomyComponent.VERTICAL_OFFSET);
                let bars = this.svgs.selectAll('g')
                    .data(this.exerciseHistory);

                // Enter
                let barsEnter = bars.enter()
                    .append('g')
                    .attr('transform', (d: any, i: any) => 'translate(' + d.x_offset + ',' + d.y_offset + ')');
                barsEnter.append('rect')
                    .style('fill', 'blue')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('width', (d: any) => d.history_weight)
                    .attr('height', (d: any) => d.history_reps * HistoryByTaxonomyComponent.REP_MULTIPLIER);
                barsEnter.append('text')
                    .attr('transform', (d: any, i: any) => 'translate(' + d.history_weight / 2 + ',' + -1 * HistoryByTaxonomyComponent.TEXT_OFFSET + ')' + ' rotate(-45)')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .text((d: any) => d.history_reps.toString() + ',' + d.history_weight.toString());

                // Update
                bars.attr('transform', (d: any, i: any) => 'translate(' + d.x_offset + ',' + d.y_offset + ')');
                bars.select('rect')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('width', (d: any) => d.history_weight)
                    .attr('height', (d: any) => d.history_reps * HistoryByTaxonomyComponent.REP_MULTIPLIER);
                bars.select('text')
                    .attr('transform', (d: any, i: any) => 'translate(' + d.history_weight / 2 + ',' + -1 * HistoryByTaxonomyComponent.TEXT_OFFSET + ')' + ' rotate(-45)')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .text((d: any) => d.history_reps.toString() + ',' + d.history_weight.toString());

                // Exit
                let barsExit = bars.exit();
                barsExit.select('rect')
                    .transition()
                    .duration(400)
                    .attr('height', 0);
                barsExit.transition()
                    .delay(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .remove();
                barsExit.select('text')
                    .remove();
            },
            err => console.log(err)
        );
    }

    private convertJsonArrayToObjectArray(historyArray: Array<any>): Array<RepHistoryObject> {
        return null;
    }

    private splitOutSets(): void {
        let newArray: Array<any> = [];
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            for (let j = 0; j < this.exerciseHistory[i].getSets(); j++) {
                newArray.push($.extend(true, {}, this.exerciseHistory[i]));  // deep copy necessary here
            }
        }
        this.exerciseHistory = newArray;
    }

    private addOffsets(): number {
        let totalOffset: number = 0;
        let currentDate: string = null;
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            let thisDate: string = this.exerciseHistory[i].getDatestamp();
            if (currentDate) {
                if (currentDate == thisDate) {
                    totalOffset += 1;
                } else {
                    totalOffset += 7;
                }
            }
            this.exerciseHistory[i].setXOffset(totalOffset);

            totalOffset += this.exerciseHistory[i].getWeight();

            this.exerciseHistory[i].setYOffset(HistoryByTaxonomyComponent.VERTICAL_OFFSET
                - this.exerciseHistory[i].getReps() * HistoryByTaxonomyComponent.REP_MULTIPLIER);
            currentDate = thisDate;
        }
        return totalOffset;
    }
}

class RepHistoryObject {
    private sets: number;
    private reps: number;
    private weight: number;
    private dateStamp: string;
    private x_offset: number;
    private y_offset: number;

    constructor(jsonObject: any) {
        this.sets = jsonObject.history_sets;
        this.reps = jsonObject.history_reps;
        this.weight = jsonObject.history_weight;
        this.dateStamp = jsonObject.history_date;

        // Default values -- will be changed
        this.x_offset = 0;
        this.y_offset = 0;
    }

    // Getters and setters
    public getSets(): number {
        return this.sets;
    }

    public setSets(newValue: number): void {
        this.sets = newValue;
    }

    public getReps(): number {
        return this.reps;
    }

    public setReps(newValue: number): void {
        this.reps = newValue;
    }

    public getWeight(): number {
        return this.weight;
    }

    public setWeight(newValue: number): void {
        this.weight = newValue;
    }

    public getDatestamp(): string {
        return this.dateStamp;
    }

    public setDatestamp(newValue: string): void {
        this.dateStamp = newValue;
    }

    public getXOffset(): number {
        return this.x_offset;
    }

    public setXOffset(newValue: number): void {
        this.x_offset = newValue;
    }

    public getYOffset(): number {
        return this.y_offset;
    }

    public setYOffset(newValue: number): void {
        this.y_offset = newValue;
    }
}
