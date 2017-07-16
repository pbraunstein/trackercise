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
                    .attr('height', data2.length * 50)
                let bars;
                bars = this.svgs.selectAll('g')
                    .data(data2);

                bars.select('rect')
                    .transition()
                    .duration(400)
                    .attr('width', (d: any) => d);

                bars.enter()
                    .append('g')
                    .attr('transform', (d: any, i: any) => 'translate(0,' + i * 50 + ')')
                    .append('rect')
                    .attr('height', (d: any) => 47)
                    .style('fill', 'blue')
                    .transition()
                    .duration(400)
                    .attr('width', (d: any) => d);

                bars.exit()
                    .select('rect')
                    .transition()
                    .duration(400)
                    .attr('width', 0);

                bars.exit().transition().duration(400).remove();
            },
            err => console.log(err)
        );


    }
}
