import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
@Component({
    selector:'register',
    templateUrl: '/static/components/register/register.html'
})
export class RegisterComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit(value: any) {
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.email = value.register_email;
        data.nickname = value.register_nickname;
        data.password = value.register_password;
        this.endpoint = this.http.post('/register', JSON.stringify(data), {headers: headers});
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        );
    }
}
