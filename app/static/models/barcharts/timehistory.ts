import {ExerciseHistory} from "./exercisehistory";
export class TimeHistory extends ExerciseHistory {
    private distance: number;
    private duration: number;

    getHistoryId(): number {
        return this.historyId;
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

    getXOffset(): number {
        return this.x_offset;
    }

    setXOffset(value: number): void {
        this.x_offset = value;
    }

    getYOffset(): number {
        return this.y_offset;
    }

    setYOffset(value: number): void {
        this.y_offset = value;
    }

    getDatestamp(): string {
        return this.dateStamp;
    }

    setDatestamp(value: string): void {
        this.dateStamp = value;
    }

    getWidthBuffer(): number {
        return 0;
    }

    getSets(): number {
        return 1;
    }

}