import {Component} from "@angular/core";
import {TimeHistoryChart} from "../timehistorychart";
import {BarChartsBar} from "../../models/barcharts/barchartsbar";
@Component({
    selector: 'time-history-by-taxonomy',
    templateUrl: '/static/components/timehistorybytaxonomy/timehistorybytaxonomy.html'
})
export class TimeHistoryByTaxonomyComponent extends TimeHistoryChart {

    protected getXValue(element: BarChartsBar): string {
        return element.getDatestamp();
    }
}
