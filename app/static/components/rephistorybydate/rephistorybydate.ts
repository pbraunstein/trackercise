import {Component} from "@angular/core";
import {CSRFService} from "../../services/csrfservice";
import {Http, Headers} from "@angular/http";
import {Observable} from "rxjs";
import {RepHistoryChart} from "../rephistorychart";
import {BarChartsBar} from "../../models/barcharts/barchartsbar";
@Component({
    selector: 'rep-history-by-date',
    templateUrl: '/static/components/rephistorybydate/rephistorybydate.html'
})
export class RepHistoryByDateComponent extends RepHistoryChart {

    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_history_by_date: Observable<any>;
    private pairs: Map<string, string>;

    constructor(private http: Http, private csrfService: CSRFService) {
        super();
        this.endpoint_exercise_pairs = http.post('/get-valid-rep-id-exercise-pairs', '');
        this.chartSelector = '#rep-history-by-date-chart';
    }

    ngOnInit() {
        this.initVizContainer();
        this.endpoint_exercise_pairs.subscribe(
            data => {
                console.log(data.json());
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
            '/rep-history-by-date',
            JSON.stringify(data),
            {headers: headers}
        );
        this.endpoint_history_by_date.subscribe(
            data => {
                console.log(data);
                this.setUpViz(data);
            },
            err => console.log(err)
        )
    }

    protected getXValue(element: BarChartsBar): string {
        return this.pairs.get(element.getHistoryId().toString());
    }
}
