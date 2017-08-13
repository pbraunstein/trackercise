import {Component} from "@angular/core";
import {Http} from "@angular/http";

import {BarChartsBar} from "../../models/barcharts/barchartsbar";
import {CSRFService} from "../../services/csrfservice";
import {RepHistoryChart} from "../rephistorychart";

@Component({
    selector: 'rep-history-by-date',
    templateUrl: '/static/components/rephistorybydate/rephistorybydate.html'
})
export class RepHistoryByDateComponent extends RepHistoryChart {
    private pairsMap: Map<string, string>;

    constructor(protected http: Http, protected csrfService: CSRFService) {
        super(http, csrfService);
        this.endpointExercisePairsTarget = '/get-valid-rep-id-exercise-pairs';
        this.endpointExerciseHistoryTarget = '/rep-history-by-date';
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
