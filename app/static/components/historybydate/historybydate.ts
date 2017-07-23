import {Component} from "@angular/core";
import {CSRFService} from "../../services/csrfservice";
import {Http, Headers} from "@angular/http";
import {RepHistory} from "../../models/rephistory";
import {Observable} from "rxjs";
@Component({
    selector: 'history-by-date',
    templateUrl: '/static/components/historybydate/historybydate.html'
})
export class HistoryByDateComponent {

    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_date: Observable<any>;
    private pairs: Map<string, string>;
    private exerciseHistory: Array<RepHistory>;

    constructor(private http: Http, private csrfService: CSRFService) {
        this.endpoint_exercise_pairs = http.post('/get-valid-id-exercise-pairs', '');
    }

    ngOnInit() {
        this.endpoint_exercise_pairs.subscribe(
            data => {
                console.log(data.json())
                this.pairs = this.initPairs(data.json().pairs);
            },
            err => console.log(err)
        );
    }

    private initPairs(jsonObject: any): Map<string, string> {
        let pairs: Map<string, string> = new Map();

        for (let aPair of jsonObject) {
            pairs.set(aPair[0], aPair[1]);
        }

        console.log(pairs);
        return pairs;
    }

    onSubmit(form: any) {
        let value: any = form.value;
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFTOKEN', this.csrfService.getToken());
        let data: any = {};
        data.exercise_date = value.history_date;
        this.endpoint_history_by_date = this.http.post(
            '/history-by-date',
            JSON.stringify(data),
            {headers: headers}
        );
        this.endpoint_history_by_date.subscribe(
            data => console.log(data),
            err => console.log(err)
        )
    }

}
