import {Component} from "@angular/core";
import {Http} from "@angular/http";

import {BarChartsBar} from "../../models/barcharts/barchartsbar";
import {CSRFService} from "../../services/csrfservice";
import {RepHistoryChart} from "../rephistorychart";

@Component({
    selector: 'rep-history-by-taxonomy',
    templateUrl: '/static/components/rephistorybytaxonomy/rephistorybytaxonomy.html'
})
export class RepHistoryByTaxonomyComponent extends RepHistoryChart {
    constructor(protected http: Http, protected csrfService: CSRFService) {
        super(http, csrfService);
        this.endpointExercisePairsTarget = '/get-valid-rep-id-exercise-pairs';
        this.endpointExerciseHistoryTarget = '/rep-history-by-taxonomy';
        this.chartSelector = '#rep-history-by-taxonomy-chart';
    }

    ngOnInit() {
        this.prepareViz();
    }

    onChange(value: any) {
        this.makeServerCall(value);
    }

    protected getXValue(element: BarChartsBar): string {
        return element.getDatestamp();
    }

    protected generateDataToSendToServer(value: any): Object {
        return {
            'exercise_id': value.exercise_id
        };
    }
}
