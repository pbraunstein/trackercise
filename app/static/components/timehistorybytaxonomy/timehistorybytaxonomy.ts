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
    }

    protected getXValue(element: BarChartsBar): string {
        return element.getDatestamp();
    }
}
