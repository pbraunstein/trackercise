import {Component} from "@angular/core";
import {CSRFService} from "../../services/csrfservice";
import {Http, Headers} from "@angular/http";
import {Observable} from "rxjs";
import * as d3 from 'd3';
import {BarCharts} from "../barcharts/barcharts";
@Component({
    selector: 'history-by-date',
    templateUrl: '/static/components/historybydate/historybydate.html'
})
export class HistoryByDateComponent extends BarCharts {

    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_date: Observable<any>;
    private pairs: Map<string, string>;

    constructor(private http: Http, private csrfService: CSRFService) {
        super();
        this.endpoint_exercise_pairs = http.post('/get-valid-rep-id-exercise-pairs', '');
    }

    ngOnInit() {
        // Set up horizontal scrolling
        d3.select('#history-by-date-chart')
            .style('height', '400px')
            .style('width', '100%')
            .style('overflow', 'scroll');
        this.svgs = d3.select('#history-by-date-chart').append('svg');
        this.endpoint_exercise_pairs.subscribe(
            data => {
                console.log(data.json());
                this.pairs = this.initPairs(data.json().pairs);
            },
            err => console.log(err)
        );
    }

    private initPairs(jsonObject: any): Map<string, string> {
        let pairs: Map<string, string> = new Map();

        for (let aPair of jsonObject) {
            pairs.set(aPair[0], aPair[1]);
        }

        console.log(pairs);
        return pairs;
    }

    onSubmit(form: any) {
        let value: any = form.value;
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFTOKEN', this.csrfService.getToken());
        let data: any = {};
        data.exercise_date = value.history_date;
        this.endpoint_history_by_date = this.http.post(
            '/rep-history-by-date',
            JSON.stringify(data),
            {headers: headers}
        );
        this.endpoint_history_by_date.subscribe(
            data => {
                console.log(data);
                this.setUpViz(data);
            },
            err => console.log(err)
        )
    }

    protected addOffsets(): number {
        let totalOffset: number = 0;
        let currentId: number = null;

        for (let i = 0; i < this.exerciseHistory.length; i++) {
            let thisId: number = this.exerciseHistory[i].getHistoryId();
            if (currentId) {
                if (currentId == thisId) {
                    totalOffset += HistoryByDateComponent.IN_BETWEEN_SETS_GAP;
                } else {
                    totalOffset += HistoryByDateComponent.IN_BETWEEN_DAYS_GAP;
                }
            }
            this.exerciseHistory[i].setXOffset(totalOffset);
            totalOffset += this.exerciseHistory[i].getWeight();
            this.exerciseHistory[i].setYOffset(HistoryByDateComponent.VERTICAL_OFFSET
                - this.exerciseHistory[i].getReps() * HistoryByDateComponent.REP_MULTIPLIER);
            currentId = thisId;
        }

        return totalOffset;
    }

    protected renderXAxis(): void {
        this.svgs.selectAll('.date-text').remove();
        let iterA = 0;
        let iterB = 0;
        let extraOffset = 0;  // This accounts for the spaces in between columns

        while (iterA < this.exerciseHistory.length) {
            iterB = iterA;
            let exericesIdA = this.exerciseHistory[iterA].getHistoryId();

            // Find first next differing exercise Id
            while (iterB < this.exerciseHistory.length && this.exerciseHistory[iterB].getHistoryId() == exericesIdA) {
                iterB++;
            }

            // Need to back up one, to last one that was the same
            iterB--;

            // Add in space between bars
            extraOffset += (iterB - iterA) * HistoryByDateComponent.IN_BETWEEN_SETS_GAP

            let middleXOffset = (this.exerciseHistory[iterA].getXOffset() + this.exerciseHistory[iterB].getXOffset() + extraOffset)
                / 2;
            this.svgs
                .append('text')
                .text(this.pairs.get(String(exericesIdA)))
                .attr('class', 'date-text')
                .attr('text-anchor', 'end')
                .attr('transform', 'translate(' + String(middleXOffset) + ','
                    + String(HistoryByDateComponent.VERTICAL_OFFSET_2) + ') rotate(-45)');

            iterA = iterB + 1;
            extraOffset += HistoryByDateComponent.IN_BETWEEN_SETS_GAP;
        }
    }
}
