import {ExerciseHistory} from "./exercisehistory";
/**
 * Model for rep based history exercises
 */
export class RepHistory extends ExerciseHistory {
    private static WEIGHT_BUFFER: number = 10;

    private sets: number;
    private reps: number;
    private weight: number;

    constructor(jsonObject: any) {
        super(jsonObject);
        this.sets = jsonObject.history_sets;
        this.reps = jsonObject.history_reps;
        this.weight = jsonObject.history_weight;
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

    public getWidthBuffer(): number {
        return RepHistory.WEIGHT_BUFFER;
    }

    public getDataLabel(): string {
        return '';
    }
}
