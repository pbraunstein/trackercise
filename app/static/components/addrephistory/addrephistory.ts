import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
import {ButtonPainter} from "../../services/buttonpainter";
@Component({
    selector: 'add-rep-history',
    templateUrl: '/static/components/addrephistory/addrephistory.html'
})
export class AddRepHistoryComponent {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_add_history: Observable<any>;
    private pairs: Array<any>;
    private buttonId: string = '#add-history-submit';

    constructor(private http: Http) {
        this.endpoint_exercise_pairs = http.post('/get-valid-rep-id-exercise-pairs', '');
    }

    ngOnInit() {
        this.endpoint_exercise_pairs.subscribe(
            data => {
                this.pairs = data.json().pairs;
            },
            err => console.log(err)
        );
    }

    onSubmit(form: any) {
        let value: any = form.value;
        ButtonPainter.handleFormSubmitProcessing(this.buttonId);
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
