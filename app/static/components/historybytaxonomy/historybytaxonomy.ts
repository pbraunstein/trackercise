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
        this.svgs = d3.select('.chart')
            .append('svg')
            .attr('width', 300)
            .attr('height', 300);
        this.endpoint_exercise_pairs.subscribe(
            data => {
                this.pairs = data.json().pairs;
            },
            err => console.log(err)
        );
    }

    onChange(value: any) {
        let bars;
        let data;
        if (this.shouldBeA) {
            data = [10, 30, 50, 70];
            this.shouldBeA = false;
        } else {
            data = [40, 60, 80];
            this.shouldBeA = true;
        }
        console.log(data);

        bars = this.svgs.selectAll('g')
            .data(data);

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
    }
}
