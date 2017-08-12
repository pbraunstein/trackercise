import {Component} from "@angular/core";
import {Http, Headers} from "@angular/http";
import {CSRFService} from "../../services/csrfservice";
import {RepHistoryChart} from "../rephistorychart";
import {BarChartsBar} from "../../models/barcharts/barchartsbar";

@Component({
    selector: 'rep-history-by-taxonomy',
    templateUrl: '/static/components/rephistorybytaxonomy/rephistorybytaxonomy.html'
})
export class RepHistoryByTaxonomyComponent extends RepHistoryChart {
    private username: string;

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
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('X-CSRFTOKEN', this.csrfService.getToken());
        let data: any = {};
        data.exercise_id = value.exercise_id;
        this.endpoint_exercise_history = this.http.post(
            this.endpointExerciseHistoryTarget,
            JSON.stringify(data),
            {headers: headers}
        );
        this.endpoint_exercise_history.subscribe(
            data => {
                this.username = data.json().nickname;
                this.setUpViz(data);
            },
            err => console.log(err)
        );
    }

    protected getXValue(element: BarChartsBar): string {
        return element.getDatestamp();
    }
}
