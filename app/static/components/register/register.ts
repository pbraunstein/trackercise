import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, URLSearchParams} from "@angular/http";
@Component({
    selector:'register',
    templateUrl: '/static/components/register/register.html'
})
export class RegisterComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit(value: any) {
        let params: URLSearchParams = new URLSearchParams();
        params.set('email', value.register_email);
        params.set('nickname', value.register_nickname);
        params.set('password', value.register_password);
        this.endpoint = this.http.get('/register', {
            search: params
        });
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        )
    }
}
