/**
 * Model for rep based history exercises. Does not currently keep track of the type of exercise
 */
export class RepHistory {
    private sets: number;
    private reps: number;
    private weight: number;
    private dateStamp: string;
    private x_offset: number;
    private y_offset: number;

    constructor(jsonObject: any) {
        this.sets = jsonObject.history_sets;
        this.reps = jsonObject.history_reps;
        this.weight = jsonObject.history_weight;
        this.dateStamp = jsonObject.history_date;

        // Default values -- will be changed
        this.x_offset = 0;
        this.y_offset = 0;
    }

    // Getters and setters
    public getSets(): number {
        return this.sets;
    }

    public setSets(newValue: number): void {
        this.sets = newValue;
    }

    public getReps(): number {
        return this.reps;
    }

    public setReps(newValue: number): void {
        this.reps = newValue;
    }

    public getWeight(): number {
        return this.weight;
    }

    public setWeight(newValue: number): void {
        this.weight = newValue;
    }

    public getDatestamp(): string {
        return this.dateStamp;
    }

    public setDatestamp(newValue: string): void {
        this.dateStamp = newValue;
    }

    public getXOffset(): number {
        return this.x_offset;
    }

    public setXOffset(newValue: number): void {
        this.x_offset = newValue;
    }

    public getYOffset(): number {
        return this.y_offset;
    }

    public setYOffset(newValue: number): void {
        this.y_offset = newValue;
    }
}
