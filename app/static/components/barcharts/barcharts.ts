import {RepHistory} from "../../models/rephistory";
export abstract class BarCharts {
    protected exerciseHistory: Array<RepHistory>;

    protected static ANIMATION_TIME: number = 400;  // in milliseconds
    protected static TEXT_OFFSET: number = 4;
    protected static REP_MULTIPLIER: number = 6;
    protected static VERTICAL_OFFSET: number = 170;

    protected convertJsonArrayToObjectArray(historyArray: Array<any>): Array<RepHistory> {
        let historyObjectArray: Array<RepHistory> = [];
        for (let jsonObject of historyArray) {
            historyObjectArray.push(new RepHistory(jsonObject));
        }
        return historyObjectArray;
    }

    protected splitOutSets(): void {
        let newArray: Array<RepHistory> = [];
        for (let i = 0; i < this.exerciseHistory.length; i++) {
            for (let j = 0; j < this.exerciseHistory[i].getSets(); j++) {
                newArray.push($.extend(true, {}, this.exerciseHistory[i]));  // deep copy necessary here
            }
        }
        this.exerciseHistory = newArray;
    }

    protected abstract addOffsets(): number;
}