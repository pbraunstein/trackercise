import {Injectable} from "@angular/core";
import {Router} from "@angular/router";
import {Http} from "@angular/http";
import {Observable} from "rxjs";

@Injectable()
export class LogoutService {
    private endpoint: Observable<any>;

    constructor(private http: Http, private router: Router) {
        this.endpoint = http.post('/logout', '');
    }

    public logout(): void {
        this.endpoint.subscribe(
            data => this.router.navigate(['login']),
            err => console.log(err)
        );
    }
}
