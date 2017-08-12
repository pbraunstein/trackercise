export class TimeService {
    public static minutesToSeconds(minutes: number): number {
        return minutes * 60;
    }

    public static secondsToMinutes(seconds: number): number {
        return seconds / 60;
    }
}
