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
    private shouldBeA = true;
    private svgs: any;

    private static ANIMATION_TIME: number = 400;  // in milliseconds
    private static BAR_HEIGHT: number = 46;
    private static TEXT_HORIZONTAL_OFFSET: number = 3;
    private static REP_MULTIPLIER: number = 6;

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
                this.svgs.attr('width', 720)
                    .attr('height', totalOffset);
                let bars = this.svgs.selectAll('g')
                    .data(this.exerciseHistory);

                // Update
                bars.select('rect')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('width', (d: any) => d.history_reps * HistoryByTaxonomyComponent.REP_MULTIPLIER)
                    .attr('height', (d: any) => d.history_weight);
                bars.select('text')
                    .attr('text-anchor', 'start')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('x', (d: any) => d.history_reps * HistoryByTaxonomyComponent.REP_MULTIPLIER + HistoryByTaxonomyComponent.TEXT_HORIZONTAL_OFFSET)
                    .text((d: any) => d.history_reps.toString() + ' reps with ' + d.history_weight.toString() + ' pounds');

                // Enter
                let barsEnter = bars.enter()
                    .append('g')
                    .attr('transform', (d: any, i: any) => 'translate(0,' + d.offset + ')');

                barsEnter.append('rect')
                    .attr('height', (d: any) => HistoryByTaxonomyComponent.BAR_HEIGHT)
                    .style('fill', 'blue')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('width', (d: any) => d.history_reps * HistoryByTaxonomyComponent.REP_MULTIPLIER)
                    .attr('height', (d: any) => d.history_weight);
                barsEnter.append('text')
                    .attr('text-anchor', 'start')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('x', (d: any) => d.history_reps * HistoryByTaxonomyComponent.REP_MULTIPLIER + HistoryByTaxonomyComponent.TEXT_HORIZONTAL_OFFSET)
                    .attr('y', (d: any) => d.history_weight / 2)
                    .text((d: any) => d.history_reps.toString() + ' reps with ' + d.history_weight.toString() + ' pounds');

                // Exit
                let barsExit = bars.exit();
                barsExit.select('rect')
                    .transition()
                    .duration(400)
                    .attr('width', 0);
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
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            this.exerciseHistory[i].offset = totalOffset;
            totalOffset += this.exerciseHistory[i].history_weight + 1;
        }
        return totalOffset;
    }
}
