import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
import {CSRFService} from "../../services/csrfservice";
import * as d3 from 'd3';
import {RepHistoryChart} from "../rephistorychart";
import {BarChartsBar} from "../../models/barcharts/barchartsbar";

@Component({
    selector: 'rep-history-by-taxonomy',
    templateUrl: '/static/components/rephistorybytaxonomy/rephistorybytaxonomy.html'
})
export class RepHistoryByTaxonomyComponent extends RepHistoryChart {
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

    protected getXValue(element: BarChartsBar): string {
        return element.getDatestamp();
    }
}
