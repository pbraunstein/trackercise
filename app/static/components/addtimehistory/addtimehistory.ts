import {Component} from "@angular/core";
import {Http} from "@angular/http";
import {Observable} from "rxjs";
@Component({
    selector: 'add-time-history',
    templateUrl: '/static/components/addtimehistory/addtimehistory.html'
})
export class AddTimeHistoryComponent {
    private endpoint_time_exercise_pairs: Observable<any>;
    private timeExercisePairs: Array<any>;
    private buttonId: string = '#add-time-history-submit';

    constructor(private http: Http) {
        this.endpoint_time_exercise_pairs = http.post('/get-valid-time-id-exercise-pairs', '');
    }

    ngOnInit() {
        this.endpoint_time_exercise_pairs.subscribe(
            data => {
                console.log(data);
                this.timeExercisePairs = data.json().pairs;
            },
            err => console.log(err)
        );
    }
}
