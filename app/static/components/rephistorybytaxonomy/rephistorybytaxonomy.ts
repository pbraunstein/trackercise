import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
import {CSRFService} from "../../services/csrfservice";
import * as d3 from 'd3';
import {BarCharts} from "../barcharts/barcharts";

@Component({
    selector: 'rep-history-by-taxonomy',
    templateUrl: '/static/components/rephistorybytaxonomy/rephistorybytaxonomy.html'
})
export class RepHistoryByTaxonomyComponent extends BarCharts {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_taxonomy: Observable<any>;
    private pairs: Array<any>;
    private username: string;

    constructor(private http: Http, private csrfService: CSRFService) {
        super();
        this.endpoint_exercise_pairs = http.post('/get-valid-rep-id-exercise-pairs', '');
    }

    ngOnInit() {
        // Set up horizontal scrolling
        d3.select('#rep-history-by-taxonomy-chart')
            .style('height', '400px')
            .style('width', '100%')
            .style('overflow', 'scroll');
        this.svgs = d3.select('#rep-history-by-taxonomy-chart').append('svg');
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
            '/rep-history-by-taxonomy',
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
                    totalOffset += RepHistoryByTaxonomyComponent.IN_BETWEEN_SETS_GAP;
                } else {
                    totalOffset += RepHistoryByTaxonomyComponent.IN_BETWEEN_DAYS_GAP;
                }
            }
            this.exerciseHistory[i].setXOffset(totalOffset);

            totalOffset += this.exerciseHistory[i].getWidth();

            this.exerciseHistory[i].setYOffset(RepHistoryByTaxonomyComponent.VERTICAL_OFFSET
                - this.exerciseHistory[i].getHeight() * RepHistoryByTaxonomyComponent.REP_MULTIPLIER);
            currentDate = thisDate;
        }
        return totalOffset;
    }

    protected renderXAxis(): void {
        this.svgs.selectAll('.date-text').remove();
        let iterA = 0;
        let iterB = 0;
        let extraOffset = 0;  // Space between the columns

        while (iterA < this.exerciseHistory.length) {
            iterB = iterA;
            let dateA = this.exerciseHistory[iterA].getDatestamp();

            // Find first differing date
            while (iterB < this.exerciseHistory.length && this.exerciseHistory[iterB].getDatestamp() == dateA) {
                iterB++;
            }

            // Back up one to the last date that was the same
            iterB--;

            // Add in space between bars
            extraOffset += (iterB - iterA) * RepHistoryByTaxonomyComponent.IN_BETWEEN_SETS_GAP;

            let middleXOffset = (this.exerciseHistory[iterA].getXOffset() + this.exerciseHistory[iterB].getXOffset()
                + extraOffset) / 2;
            this.svgs
                .append('text')
                .text(dateA)
                .attr('class', 'date-text')
                .attr('text-anchor', 'end')
                .attr('transform', 'translate(' + String(middleXOffset) + ','
                    + String(RepHistoryByTaxonomyComponent.VERTICAL_OFFSET_2) + ') rotate(-45)');

            iterA = iterB + 1;
            extraOffset += RepHistoryByTaxonomyComponent.IN_BETWEEN_DAYS_GAP;
        }
    }
}
