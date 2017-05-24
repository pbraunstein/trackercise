import {Injectable} from "@angular/core";
import {CanActivate} from "@angular/router";
import {Http} from "@angular/http";
import {Observable} from "rxjs";
import 'rxjs/Rx';

@Injectable()
export class LoginGuard implements CanActivate {
    private endpoint: Observable<any>;
    private userReturned: boolean;

    constructor(private http: Http) {
        this.endpoint = http.post('/who-am-i', '');
        this.userReturned = false;
    }

    canActivate() {
        return this.currentUser().map(
            user => {
                if (user) {
                    return true;
                } else {
                    return false;
                }
            }
        );
    }

    currentUser(): Observable<String> {
        return this.endpoint.map(
            response => response.json().user
        )
    }
}
