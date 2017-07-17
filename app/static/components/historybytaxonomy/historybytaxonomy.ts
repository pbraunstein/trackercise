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
    private history: Array<any>;
    private username: string;
    private shouldBeA = true;
    private svgs: any;

    private static ANIMATION_TIME: number = 400;  // in milliseconds
    private static BAR_HEIGHT: number = 46;
    private static TEXT_HORIZONTAL_OFFSET: number = 3;

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
        let data2: any = [];

        this.endpoint_history_by_taxonomy.subscribe(
            data => {
                this.username = data.json().nickname;
                this.history = data.json().history;
                console.log(data.json().history);
                for (let i = 0; i < this.history.length; i++) {
                    data2.push(this.history[i].history_weight);
                }
                this.svgs.attr('width', 720)
                    .attr('height', data2.length * 50);
                let bars = this.svgs.selectAll('g')
                    .data(data2);

                // Update
                bars.select('rect')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('width', (d: any) => d);
                bars.select('text')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('x', (d: any) => d + HistoryByTaxonomyComponent.TEXT_HORIZONTAL_OFFSET)
                    .text((d: any) => d.toString());

                // Enter
                let barsEnter = bars.enter()
                    .append('g')
                    .attr('transform', (d: any, i: any) => 'translate(0,' + i * 50 + ')');

                barsEnter.append('rect')
                    .attr('height', (d: any) => HistoryByTaxonomyComponent.BAR_HEIGHT)
                    .style('fill', 'blue')
                    .transition()
                    .duration(HistoryByTaxonomyComponent.ANIMATION_TIME)
                    .attr('width', (d: any) => d);
                barsEnter.append('text')
                    .attr('x', (d: any) => d + HistoryByTaxonomyComponent.TEXT_HORIZONTAL_OFFSET)
                    .attr('y', (d: any) => HistoryByTaxonomyComponent.BAR_HEIGHT / 2)
                    .text((d: any) => d.toString());

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
}
