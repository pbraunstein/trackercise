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
export class HistoryByDateComponent extends BarCharts{

    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_date: Observable<any>;
    private pairs: Map<string, string>;

    constructor(private http: Http, private csrfService: CSRFService) {
        super();
        this.endpoint_exercise_pairs = http.post('/get-valid-id-exercise-pairs', '');
    }

    ngOnInit() {
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
            '/history-by-date',
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
                    totalOffset += 1;
                } else {
                    totalOffset += 7;
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
        let currentId: number = null;
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            let thisId: number = this.exerciseHistory[i].getHistoryId();
            if (!currentId || currentId != thisId) {
                this.svgs
                    .append('text')
                    .attr('class', 'date-text')
                    .attr('x', this.exerciseHistory[i].getXOffset())
                    .attr('y', HistoryByDateComponent.VERTICAL_OFFSET + 15)
                    .text(this.pairs.get(String(thisId)));
            }
            currentId = thisId;
        }
    }

}
