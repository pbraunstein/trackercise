import {BarCharts} from "./barcharts";
import {BarChartsBar} from "../models/barcharts/barchartsbar";
import {TimeHistory} from "../models/barcharts/timehistory";
/**
 * Intermediate class in the hierarchy of BarCharts. Any TimeExercise bar chart should extend this class
 * and implement the remaining abstract methods
 */
export abstract class TimeHistoryChart extends BarCharts {
    protected convertJsonArrayToBarChartsBarArray(historyArray: Array<any>): Array<BarChartsBar> {
        let historyObjectArray: Array<TimeHistory> = [];
        for (let jsonObject of historyArray) {
            historyObjectArray.push(new TimeHistory(jsonObject));
        }
        return historyObjectArray;
    }
}
