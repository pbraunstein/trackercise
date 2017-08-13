import {Component} from "@angular/core";
import {Headers, Http} from "@angular/http";
import {Router} from "@angular/router";
import {Observable} from "rxjs";

import {CSRFService} from "../../services/csrfservice";

@Component({
    selector:'login',
    templateUrl: '/static/components/login/login.html'
})
export class LoginComponent{
    private endpoint: Observable<any>;
    private router: Router;

    constructor(private http: Http, router: Router, private csrfService: CSRFService) {
        this.router = router;
    }

    onSubmit(value: any) {
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.email = value.login_email;
        data.password = value.login_password;
        this.endpoint = this.http.post('/login', JSON.stringify(data), {headers: headers});
        this.endpoint.subscribe(
            data => {
                this.router.navigate(['/']);
                this.csrfService.setToken(data.headers.get('X-CSRFTOKEN'));
                console.log(data);
            },
            err => console.log(err)
        );
    }
}
