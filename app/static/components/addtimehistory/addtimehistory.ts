import {Component} from "@angular/core";
import {Http} from "@angular/http";
import {Observable} from "rxjs";
import {TimeService} from "../../services/timeservice";
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

    ngOnInit(): void {
        this.endpoint_time_exercise_pairs.subscribe(
            data => {
                console.log(data);
                this.timeExercisePairs = data.json().pairs;
            },
            err => console.log(err)
        );
    }

    onSubmit(form: any): void {
        let value: any = form.value;
        let minutes = value.time_history_duration_minutes;
        let seconds = value.time_history_duration_seconds;
        let durationSeconds: number;
        durationSeconds = TimeService.minutesToSeconds(value.time_history_duration_minutes)
            + value.time_history_duration_seconds;
        let data: Object = {
            'history_exercise_id': value.time_history_exercise_id,
            'history_distance': value.time_history_distance,
            'history_duration': durationSeconds,
            'history_date': value.time_history_date
        };
    }

}
