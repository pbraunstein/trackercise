/**
 * Model for rep based history exercises
 */
export class RepHistory {
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
