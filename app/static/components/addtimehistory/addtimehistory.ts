import {Component} from "@angular/core";
import {Http, Headers} from "@angular/http";
import {Observable} from "rxjs";
import {TimeService} from "../../services/timeservice";
import {ButtonPainter} from "../../services/buttonpainter";
@Component({
    selector: 'add-time-history',
    templateUrl: '/static/components/addtimehistory/addtimehistory.html'
})
export class AddTimeHistoryComponent {
    private endpoint_time_exercise_pairs: Observable<any>;
    private endpoint_add_time_history: Observable<any>;
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
        ButtonPainter.handleFormSubmitProcessing(this.buttonId);
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let value: any = form.value;
        let durationSeconds: number;
        durationSeconds = TimeService.minutesToSeconds(value.time_history_duration_minutes)
            + value.time_history_duration_seconds;
        let dataToSend: Object = {
            'history_exercise_id': value.time_history_exercise_id,
            'history_distance': value.time_history_distance,
            'history_duration': durationSeconds,
            'history_date': value.time_history_date
        };

        this.endpoint_add_time_history = this.http.post('/add-time-history', JSON.stringify(dataToSend), {headers: headers});

        this.endpoint_add_time_history.subscribe(
            data => {
                console.log(data);
                ButtonPainter.handleFormSubmitSuccess(form, this.buttonId);
            },
            err => {
                console.log(err);
                ButtonPainter.handleFormSubmitFailure(this.buttonId);
            }
        )
    }
}
