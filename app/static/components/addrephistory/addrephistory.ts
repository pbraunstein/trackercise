import {Component} from "@angular/core";
import {Headers, Http} from "@angular/http";
import {Observable} from "rxjs";

import {SelectOption} from "../../models/selectoption";
import {ButtonPainter} from "../../services/buttonpainter";

@Component({
    selector: 'add-rep-history',
    templateUrl: '/static/components/addrephistory/addrephistory.html'
})
export class AddRepHistoryComponent {
    private endpointExercisePairs: Observable<any>;
    private endpointAddHistory: Observable<any>;
    private repExercisePairs: Array<SelectOption>;
    private buttonId: string = '#add-history-submit';

    constructor(private http: Http) {
        this.endpointExercisePairs = http.post('/get-valid-rep-id-exercise-pairs', '');
    }

    ngOnInit(): void {
        this.endpointExercisePairs.subscribe(
            data => {
                this.repExercisePairs = [];
                data.json().pairs.forEach((p: any) => this.repExercisePairs.push(new SelectOption(p)));
            },
            err => console.log(err)
        );
    }

    onSubmit(form: any): void {
        let value: any = form.value;
        ButtonPainter.handleFormSubmitProcessing(this.buttonId);
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.history_exercise_id = value.history_exercise_id;
        data.history_sets = value.rep_history_sets;
        data.history_reps = value.rep_history_reps;
        data.history_weight = value.rep_history_weight;
        data.history_date = value.rep_history_date;
        this.endpointAddHistory = this.http.post('/add-rep-history', JSON.stringify(data), {headers: headers});
        this.endpointAddHistory.subscribe(
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
