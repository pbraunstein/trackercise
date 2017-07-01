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

    constructor(private http: Http, private csrfService: CSRFService) {
        this.endpoint_exercise_pairs = http.post('/get-valid-id-exercise-pairs', '');
    }

    ngOnInit() {
        console.log("in ngOnInit");
        this.endpoint_exercise_pairs.subscribe(
            data => {
                this.pairs = data.json().pairs;
            },
            err => console.log(err)
        );
    }

    onChange(value: any) {
        console.log("In onChange");
        console.log(this.shouldBeA);

        let bars;
        let data;
        if (this.shouldBeA) {
            data = [10, 30, 50, 70];
            this.shouldBeA = false;
        } else {
            data = [40, 60, 80];
            this.shouldBeA = true;
        }
        bars = d3.select(".chart")
            .selectAll("div")
            .data(data);
        bars.enter()
            .append("div")
            .style("width", function (d: any) {
                console.log(d);
                return d + "px";
            })
            .style("background-color", d => 'steelblue')
            .text((d) => d.toString());
        bars.transition()
            .duration(400)
            .style("width", function (d: any) {
                console.log(d);
                return d + "px";
            })
            .style("background-color", d => 'steelblue')
            .text((d) => d.toString());
        bars.exit()
            .remove();
        // let headers: Headers = new Headers();
        // headers.append('Content-Type', 'application/json');
        // headers.append('X-CSRFTOKEN', this.csrfService.getToken());
        // let data: any = {};
        // data.exercise_id = value.exercise_id;
        // this.endpoint_history_by_taxonomy = this.http.post(
        //     '/history-by-taxonomy',
        //     JSON.stringify(data),
        //     {headers: headers}
        // );
        // let data2: any = [];
        //
        // this.endpoint_history_by_taxonomy.subscribe(
        //     data => {
        //         this.username = data.json().nickname;
        //         this.history = data.json().history;
        //         console.log(data.json().history);
        //         for (let i = 0; i < this.history.length; i++) {
        //             data2.push(this.history[i].history_weight)
        //         }
        //         // if (data2.length > 0) {
        //
        //     },
        //     err => console.log(err)
        // );
    }
}
