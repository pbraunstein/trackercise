import {Injectable} from "@angular/core";
import {CanActivate, Router} from "@angular/router";
import {Http} from "@angular/http";
import {Observable} from "rxjs";
import 'rxjs/Rx';

@Injectable()
export class LoginGuard implements CanActivate {
    private endpoint: Observable<any>;
    private router: Router;
    private userReturned: boolean;

    constructor(private http: Http, router: Router) {
        this.endpoint = this.http.post('/who-am-i', '');
        this.router = router;
        this.userReturned = false;
    }

    canActivate() {
        return this.currentUser().map(
            user => {
                if (user !== null && user !== undefined && user !== '') {
                    return true;
                } else {
                    this.router.navigate(['login']);
                    return false;
                }
            }
        );
    }

    currentUser(): Observable<String> {
        return this.endpoint.map(
            response => response.json().user
        );
    }
}
