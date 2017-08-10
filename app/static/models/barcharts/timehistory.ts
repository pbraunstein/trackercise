import {ExerciseHistory} from "./exercisehistory";
export class TimeHistory extends ExerciseHistory {
    private distance: number;
    private duration: number;

    constructor(jsonObject: any) {
        super(jsonObject);
        this.distance = jsonObject.history_distance;
        this.duration = jsonObject.history_duration;
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
        return 0;
    }

    getSets(): number {
        return 1;
    }

}