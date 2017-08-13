import {Component} from "@angular/core";
import {Headers, Http} from "@angular/http";
import {Observable} from "rxjs";

import {SelectOption} from "../../models/selectoption";
import {ButtonPainter} from "../../services/buttonpainter";
import {TimeService} from "../../services/timeservice";

@Component({
    selector: 'add-time-history',
    templateUrl: '/static/components/addtimehistory/addtimehistory.html'
})
export class AddTimeHistoryComponent {
    private endpointTimeExercisePairs: Observable<any>;
    private endpointAddTimeHistory: Observable<any>;
    private timeExercisePairs: Array<SelectOption>;
    private buttonId: string = '#add-time-history-submit';

    constructor(private http: Http) {
        this.endpointTimeExercisePairs = http.post('/get-valid-time-id-exercise-pairs', '');
    }

    ngOnInit(): void {
        this.endpointTimeExercisePairs.subscribe(
            data => {
                this.timeExercisePairs = [];
                data.json().pairs.forEach((p: any) => this.timeExercisePairs.push(new SelectOption(p)));
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
            + Number(value.time_history_duration_seconds);
        let dataToSend: Object = {
            'history_exercise_id': value.time_history_exercise_id,
            'history_distance': value.time_history_distance,
            'history_duration': durationSeconds,
            'history_date': value.time_history_date
        };

        this.endpointAddTimeHistory = this.http.post(
            '/add-time-history', JSON.stringify(dataToSend), {headers: headers}
            );

        this.endpointAddTimeHistory.subscribe(
            data => {
                console.log(data);
                ButtonPainter.handleFormSubmitSuccess(form, this.buttonId);
            },
            err => {
                console.log(err);
                ButtonPainter.handleFormSubmitFailure(this.buttonId);
            }
        );
    }
}
