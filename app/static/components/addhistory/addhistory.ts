import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";

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
    }
}
