import {Component} from "@angular/core";
import {TimeHistoryChart} from "../timehistorychart";
import {BarChartsBar} from "../../models/barcharts/barchartsbar";
import {Http} from "@angular/http";
import {CSRFService} from "../../services/csrfservice";
@Component({
    selector: 'time-history-by-taxonomy',
    templateUrl: '/static/components/timehistorybytaxonomy/timehistorybytaxonomy.html'
})
export class TimeHistoryByTaxonomyComponent extends TimeHistoryChart {

    constructor(protected http: Http, protected csrfService: CSRFService) {
        super(http, csrfService);
        this.endpointExercisePairsTarget = '/get-valid-time-id-exercise-pairs';
        this.endpointExerciseHistoryTarget = '/time-history-by-taxonomy';
        this.chartSelector = '#time-history-by-taxonomy-chart';
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
