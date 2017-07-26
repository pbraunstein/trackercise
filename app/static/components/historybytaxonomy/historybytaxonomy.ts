import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
import {CSRFService} from "../../services/csrfservice";
import {RepHistory} from "../../models/rephistory";
import * as d3 from 'd3';
import {BarCharts} from "../barcharts/barcharts";
import {HistoryByDateComponent} from "../historybydate/historybydate";

@Component({
    selector: 'history-by-taxonomy',
    templateUrl: '/static/components/historybytaxonomy/historybytaxonomy.html'
})
export class HistoryByTaxonomyComponent extends BarCharts {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_taxonomy: Observable<any>;
    private pairs: Array<any>;
    private username: string;

    constructor(private http: Http, private csrfService: CSRFService) {
        super();
        this.endpoint_exercise_pairs = http.post('/get-valid-id-exercise-pairs', '');
    }

    ngOnInit() {
        this.svgs = d3.select('#history-by-taxonomy-chart').append('svg');
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
                this.setUpViz(data);
            },
            err => console.log(err)
        );
    }

    protected addOffsets(): number {
        let totalOffset: number = 0;
        let currentDate: string = null;
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            let thisDate: string = this.exerciseHistory[i].getDatestamp();
            if (currentDate) {
                if (currentDate == thisDate) {
                    totalOffset += HistoryByTaxonomyComponent.IN_BETWEEN_SETS_GAP;
                } else {
                    totalOffset += HistoryByTaxonomyComponent.IN_BETWEEN_DAYS_GAP;
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

    protected renderXAxis(): void {
        this.svgs.selectAll('.date-text').remove();
        let currentDate: string = null;
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            let thisDate: string = this.exerciseHistory[i].getDatestamp();
            if (!currentDate || currentDate != thisDate) {
                this.svgs
                    .append('text')
                    .attr('class', 'date-text')
                    .attr('x', this.exerciseHistory[i].getXOffset())
                    .attr('y', HistoryByTaxonomyComponent.VERTICAL_OFFSET + 15)
                    .text(thisDate);
            }
            currentDate = thisDate;
        }
    }
}
