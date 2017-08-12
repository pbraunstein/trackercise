import {ExerciseHistory} from "./exercisehistory";
import {TimeService} from "../../services/timeservice";
export class TimeHistory extends ExerciseHistory {
    private distance: number;
    private duration: number;

    constructor(jsonObject: any) {
        super(jsonObject);
        this.distance = jsonObject.history_distance;
        this.duration = TimeService.secondsToMinutes(jsonObject.history_duration);
    }

    getWidth(): number {
        return this.distance;
    }

    setWidth(value: number): void {
        this.distance = value;
    }

    getHeight(): number {
        return this.duration;
    }

    setHeight(value: number): void {
        this.duration = value;
    }

    getWidthBuffer(): number {
        return 20;
    }

    getSets(): number {
        return 1;
    }

}