import {Component} from "@angular/core";
import {CSRFService} from "../../services/csrfservice";
import {Http} from "@angular/http";
import {BarChartsBar} from "../../models/barcharts/barchartsbar";
import {TimeHistoryChart} from "../timehistorychart";
@Component({
    selector: 'time-history-by-date',
    templateUrl: '/static/components/timehistorybydate/timehistorybydate.html'
})
export class TimeHistoryByDateComponent extends TimeHistoryChart {
    private pairsMap: Map<string, string>;

    constructor(protected http: Http, protected csrfService: CSRFService) {
        super(http, csrfService);
        this.endpointExercisePairsTarget = '/get-valid-time-id-exercise-pairs';
        this.endpointExerciseHistoryTarget = '/time-history-by-date';
        this.chartSelector = '#time-history-by-date-chart';
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

    onSubmit(value: any) {
        this.makeServerCall(value);
    }

    protected getXValue(element: BarChartsBar): string {
        return this.pairsMap.get(element.getHistoryId().toString());
    }

    protected generateDataToSendToServer(value: any): Object {
        return {'exercise_date': value.history_date };
    }
}
