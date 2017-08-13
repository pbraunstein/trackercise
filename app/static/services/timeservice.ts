export class TimeService {
    private static SECONDS_PER_MINUTE: number = 60;

    public static minutesToSeconds(minutes: number): number {
        return minutes * TimeService.SECONDS_PER_MINUTE;
    }

    public static secondsToMinutes(seconds: number): number {
        return seconds / TimeService.SECONDS_PER_MINUTE;
    }
}
