import {TimeService} from "../../services/timeservice";
import {ExerciseHistory} from "./exercisehistory";

export class TimeHistory extends ExerciseHistory {
    private static WIDTH_BUFFER: number = 20;

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
        return TimeHistory.WIDTH_BUFFER;
    }

    getSets(): number {
        return 1;
    }
}
