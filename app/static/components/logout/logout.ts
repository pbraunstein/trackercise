import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
import {Router} from "@angular/router";

@Component({
    selector: 'logout',
    templateUrl: '/static/components/logout/logout.html'
})
export class LogoutComponent {
    private endpoint: Observable<any>;
    private router: Router;

    constructor(private http: Http, router: Router) {
        this.endpoint = http.post('/logout', '');
        this.router = router;
    }

    onSubmit() {
        this.endpoint.subscribe(
            data => {
                console.log(data);
                this.router.navigate(['login'])
            },
            err => console.log(err)
        )
    }
}
