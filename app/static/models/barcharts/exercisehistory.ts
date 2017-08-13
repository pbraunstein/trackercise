import {BarChartsBar} from "./barchartsbar";
export abstract class ExerciseHistory implements BarChartsBar {
    private static DATESTAMP_LENGTH: number = 10;

    protected historyId: number;
    protected dateStamp: string;
    protected x_offset: number;
    protected y_offset: number;

    constructor(jsonObject: any) {
        this.historyId = jsonObject.history_exercise_id;

        // fragile - this should happen serverside
        this.dateStamp = jsonObject.history_date.slice(
            0, ExerciseHistory.DATESTAMP_LENGTH
        );

        // Default values -- will be changed
        this.x_offset = 0;
        this.y_offset = 0;
    }


    public getHistoryId(): number {
        return this.historyId;
    }

    public setHistoryId(value: number): void {
        this.historyId = value;
    }

    public getDatestamp(): string {
        return this.dateStamp;
    }

    public setDatestamp(value: string): void {
        this.dateStamp = value;
    }

     public getXOffset(): number {
        return this.x_offset;
    }

    public setXOffset(value: number): void {
        this.x_offset = value;
    }

    public getYOffset(): number {
        return this.y_offset;
    }

    public setYOffset(value: number): void {
        this.y_offset = value;
    }

    // These methods must be implemented by the child classes
    public abstract getWidth(): number;
    public abstract setWidth(value: number): void;
    public abstract getHeight(): number;
    public abstract setHeight(value: number): void;
    public abstract getWidthBuffer(): number;
    public abstract getSets(): number;
}
