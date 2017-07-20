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
    private exerciseHistory: Array<any>;
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
        this.svgs = d3.select('.chart').append('svg')
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
                this.exerciseHistory = data.json().history;
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

    addOffsets(): number {
        let totalOffset = 0;
        let newArray: Array<any> = [];
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            for (let j = 0; j < this.exerciseHistory[i].history_sets; j++) {
                let oneSet: any = $.extend(true, {}, this.exerciseHistory[i]);
                oneSet.x_offset = totalOffset;
                totalOffset += oneSet.history_weight + 1;

                oneSet.y_offset = HistoryByTaxonomyComponent.VERTICAL_OFFSET
                    - oneSet.history_reps * HistoryByTaxonomyComponent.REP_MULTIPLIER;

                newArray.push(oneSet);
            }
            totalOffset += 5;  // Spacing between groups of sets
        }
        this.exerciseHistory = newArray;
        return totalOffset;
    }
}
