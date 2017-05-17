import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, URLSearchParams} from "@angular/http";
@Component({
    selector:'history-by-taxonomy',
    templateUrl: '/static/components/historybytaxonomy/historybytaxonomy.html'
})
export class HistoryByTaxonomyComponent {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_taxonomy: Observable<any>;
    private pairs: Array<any>;

    constructor(private http: Http){
        this.endpoint_exercise_pairs = http.get('/get-valid-id-exercise-pairs');
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
        let params: URLSearchParams = new URLSearchParams();
        console.log(value);
        params.set('plop', value.exercise_id);
        this.endpoint_history_by_taxonomy = this.http.get('/history-by-taxonomy', {
            search: params
        });
        this.endpoint_history_by_taxonomy.subscribe(
            data => console.log(data),
            err => console.log(err)
        );
    }
}
