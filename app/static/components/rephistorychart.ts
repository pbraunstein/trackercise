import {BarChartsBar} from "../models/barcharts/barchartsbar";
import {RepHistory} from "../models/barcharts/rephistory";
import {BarCharts} from "./barcharts";

/**
 * Intermediate class in the hierarchy of BarCharts. Any RepExercise bar chart should extend this class
 * and implement the remaining abstract methods from BarCharts
 */
export abstract class RepHistoryChart extends BarCharts {
    protected convertJsonArrayToBarChartsBarArray(historyArray: Array<any>): Array<BarChartsBar> {
        let historyObjectArray: Array<RepHistory> = [];
        for (let jsonObject of historyArray) {
            historyObjectArray.push(new RepHistory(jsonObject));
        }
        return historyObjectArray;
    }
}
