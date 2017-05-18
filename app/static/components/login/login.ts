import {Component} from "@angular/core";
import {Http, Headers} from "@angular/http";
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
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.email = value.login_email;
        data.password = value.login_password;
        this.endpoint = this.http.post('/login', JSON.stringify(data), {headers: headers});
        this.endpoint.subscribe(
            data => {
                console.log(data);
            },
            err => console.log(err)
        )
    }
}
