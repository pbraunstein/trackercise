import {BarChartsBar} from "./barchartsbar";
/**
 * Model for rep based history exercises
 */
export class RepHistory implements BarChartsBar {
    private historyId: number;
    private sets: number;
    private reps: number;
    private weight: number;
    private dateStamp: string;
    private x_offset: number;
    private y_offset: number;

    constructor(jsonObject: any) {
        this.historyId = jsonObject.history_exercise_id;
        this.sets = jsonObject.history_sets;
        this.reps = jsonObject.history_reps;
        this.weight = jsonObject.history_weight;
        this.dateStamp = jsonObject.history_date.slice(0, 10);  // fragile - this should happen serverside

        // Default values -- will be changed
        this.x_offset = 0;
        this.y_offset = 0;
    }

    // Getters and setters
    public getHistoryId(): number {
        return this.historyId;
    }

    public setHistoryId(newValue: number): void {
        this.historyId = newValue;
    }

    public getSets(): number {
        return this.sets;
    }

    public setSets(value: number): void {
        this.sets = value;
    }

    public getHeight(): number {
        return this.reps;
    }

    public setHeight(value: number): void {
        this.reps = value;
    }

    public getWidth(): number {
        return this.weight;
    }

    public setWidth(newValue: number): void {
        this.weight = newValue;
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

    public getWidthBuffer(): number {
        return 10;
    }
}
