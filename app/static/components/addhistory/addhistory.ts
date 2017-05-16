import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, URLSearchParams} from "@angular/http";
@Component({
    selector: 'add-history',
    templateUrl: '/static/components/addhistory/addhistory.html'
})
export class AddHistoryComponent {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_add_history: Observable<any>;
    private pairs: Array<any>;

    constructor(private http: Http){
        this.endpoint_exercise_pairs = http.get('/get-valid-id-exercise-pairs');
    }

    ngOnInit() {
        this.endpoint_exercise_pairs.subscribe(
            data => {
                this.pairs = data.json().pairs;
                console.log(this.pairs);
            },
            err => console.log(err)
        );
    }

    onSubmit(value: any){
        console.log(value);
        let params: URLSearchParams = new URLSearchParams();
        params.set('history_exercise_id', value.history_exercise_id);
        params.set('history_sets', value.history_sets);
        params.set('history_reps', value.history_reps);
        params.set('history_weight', value.history_weight);
        params.set('history_date', value.history_date);
        this.endpoint_add_history = this.http.get('/add-rep-history', {
            search: params
        });
        this.endpoint_add_history.subscribe(
            data => console.log(data),
            err => console.log(err)
        )
    }
}
