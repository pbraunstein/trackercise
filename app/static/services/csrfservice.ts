import {Injectable} from "@angular/core";

@Injectable()
export class CSRFService {
    private static csrfToken: string = '';

    public setToken(newValue: string): void {
        CSRFService.csrfToken = newValue;
    }

    public getToken(): string {
        return CSRFService.csrfToken;
    }
}
