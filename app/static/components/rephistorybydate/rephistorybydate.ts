import {Component} from "@angular/core";
import {CSRFService} from "../../services/csrfservice";
import {Http, Headers} from "@angular/http";
import {RepHistoryChart} from "../rephistorychart";
import {BarChartsBar} from "../../models/barcharts/barchartsbar";
@Component({
    selector: 'rep-history-by-date',
    templateUrl: '/static/components/rephistorybydate/rephistorybydate.html'
})
export class RepHistoryByDateComponent extends RepHistoryChart {
    private pairsMap: Map<string, string>;

    constructor(private http: Http, private csrfService: CSRFService) {
        super();
        this.endpoint_exercise_pairs = http.post('/get-valid-rep-id-exercise-pairs', '');
        this.chartSelector = '#rep-history-by-date-chart';
    }

    ngOnInit() {
        this.prepareViz();
    }

    protected initPairsMap(): void {
        this.pairsMap = new Map();
        for (let aPair of this.pairs) {
            this.pairsMap.set(aPair[0], aPair[1]);
        }
    }

    onSubmit(form: any) {
        let value: any = form.value;
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFTOKEN', this.csrfService.getToken());
        let data: any = {};
        data.exercise_date = value.history_date;
        this.endpoint_exercise_history = this.http.post(
            '/rep-history-by-date',
            JSON.stringify(data),
            {headers: headers}
        );
        this.endpoint_exercise_history.subscribe(
            data => {
                console.log(data);
                this.setUpViz(data);
            },
            err => console.log(err)
        )
    }

    protected getXValue(element: BarChartsBar): string {
        return this.pairsMap.get(element.getHistoryId().toString());
    }
}
