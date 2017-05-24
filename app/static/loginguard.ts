import {Injectable} from "@angular/core";
import {CanActivate} from "@angular/router";
import {Http} from "@angular/http";
import {Observable} from "rxjs";

@Injectable()
export class LoginGuard implements CanActivate {
    private endpoint: Observable<any>;
    private userReturned: boolean;

    constructor(private http: Http) {
        this.endpoint = http.post('/who-am-i', '');
    }

    canActivate(): boolean {
        this.endpoint.subscribe(
            data => {
                console.log(data);
            },
            err => console.log(err)
        );
        return false;
    }

}