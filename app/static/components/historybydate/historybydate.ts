import {Component} from "@angular/core";
import {CSRFService} from "../../services/csrfservice";
import {Http, Headers} from "@angular/http";
import {RepHistory} from "../../models/rephistory";
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
    private svgs: any;

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
                this.exerciseHistory = this.convertJsonArrayToObjectArray(data.json().history);
                this.splitOutSets();
                let totalOffset = this.addOffsets();
                this.svgs.attr('width', totalOffset)
                    .attr('height', HistoryByDateComponent.VERTICAL_OFFSET * 2);
                let bars = this.svgs.selectAll('g')
                    .data(this.exerciseHistory);

                // Enter
                let barsEnter = bars.enter()
                    .append('g')
                    .attr('transform', (d: any, i: number) => 'translate(' + d.x_offset + ',' + d.y_offset + ')');
                barsEnter.append('rect')
                    .style('fill', 'blue')
                    .transition()
                    .duration(HistoryByDateComponent.ANIMATION_TIME)
                    .attr('width', (d: RepHistory) => d.getWeight())
                    .attr('height', (d: RepHistory) => d.getReps() * HistoryByDateComponent.REP_MULTIPLIER);
                barsEnter.append('text')
                    .attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getWeight() / 2 + ',' + -1 * HistoryByDateComponent.TEXT_OFFSET + ')' + ' rotate(-45)')
                    .transition()
                    .duration(HistoryByDateComponent.ANIMATION_TIME)
                    .text((d: RepHistory) => d.getReps().toString() + ',' + d.getWeight().toString());

                // Update
                bars.attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getXOffset() + ',' + d.getYOffset() + ')');
                bars.select('rect')
                    .transition()
                    .duration(HistoryByDateComponent.ANIMATION_TIME)
                    .attr('width', (d: RepHistory) => d.getWeight())
                    .attr('height', (d: RepHistory) => d.getReps() * HistoryByDateComponent.REP_MULTIPLIER);
                bars.select('text')
                    .attr('transform', (d: RepHistory, i: number) => 'translate(' + d.getWeight() / 2 + ',' + -1 * HistoryByDateComponent.TEXT_OFFSET + ')' + ' rotate(-45)')
                    .transition()
                    .duration(HistoryByDateComponent.ANIMATION_TIME)
                    .text((d: RepHistory) => d.getReps().toString() + ',' + d.getWeight().toString());

                // Exit
                let barsExit = bars.exit();
                barsExit.select('rect')
                    .transition()
                    .duration(400)
                    .attr('height', 0);
                barsExit.transition()
                    .delay(HistoryByDateComponent.ANIMATION_TIME)
                    .remove();
                barsExit.select('text')
                    .remove();
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

}
