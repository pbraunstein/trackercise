import {Component} from "@angular/core";
import {Http, URLSearchParams} from "@angular/http";
import {Observable} from "rxjs";

@Component({
    selector:'login',
    templateUrl: '/static/components/login/login.html'
})
export class LoginComponent{
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit(value: any) {
        let params: URLSearchParams = new URLSearchParams();
        params.set('email', value.login_email);
        params.set('password', value.login_password);
        this.endpoint = this.http.get('/login', {
            search: params
        });
        this.endpoint.subscribe(
            data => {
                console.log(data);
            },
            err => console.log(err)
        )
    }
}