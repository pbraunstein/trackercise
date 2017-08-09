import {BarCharts} from "./barcharts";
import {BarChartsBar} from "../models/barchartsbar";
import {RepHistory} from "../models/rephistory";
export abstract class RepHistoryChart extends BarCharts {
    protected convertJsonArrayToBarChartsBarArray(historyArray: Array<any>): Array<BarChartsBar> {
        let historyObjectArray: Array<RepHistory> = [];
        for (let jsonObject of historyArray) {
            historyObjectArray.push(new RepHistory(jsonObject));
        }
        return historyObjectArray;
    }

}