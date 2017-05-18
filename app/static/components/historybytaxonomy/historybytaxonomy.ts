import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, URLSearchParams, Headers} from "@angular/http";
@Component({
    selector:'history-by-taxonomy',
    templateUrl: '/static/components/historybytaxonomy/historybytaxonomy.html'
})
export class HistoryByTaxonomyComponent {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_taxonomy: Observable<any>;
    private pairs: Array<any>;
    private history: Array<any>;
    private username: string;

    constructor(private http: Http){
        this.endpoint_exercise_pairs = http.post('/get-valid-id-exercise-pairs', '');
    }

    ngOnInit() {
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
                this.history = data.json().history;
            },
            err => console.log(err)
        );
    }
}
