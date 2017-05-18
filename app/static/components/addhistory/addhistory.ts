import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
@Component({
    selector: 'add-history',
    templateUrl: '/static/components/addhistory/addhistory.html'
})
export class AddHistoryComponent {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_add_history: Observable<any>;
    private pairs: Array<any>;

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

    onSubmit(value: any){
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.history_exercise_id = value.history_exercise_id;
        data.history_sets = value.history_sets;
        data.history_reps = value.history_reps;
        data.history_weight = value.history_weight;
        data.history_date = value.history_date;
        this.endpoint_add_history = this.http.post('/add-rep-history', JSON.stringify(data), {headers: headers});
        this.endpoint_add_history.subscribe(
            data => console.log(data),
            err => console.log(err)
        )
    }
}
