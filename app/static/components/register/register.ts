import {Component} from "@angular/core";
import {Headers, Http} from "@angular/http";
import {Observable} from "rxjs";

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
        let dataToSend: any = {};
        dataToSend.email = value.register_email;
        dataToSend.nickname = value.register_nickname;
        dataToSend.password = value.register_password;
        this.endpoint = this.http.post('/register', JSON.stringify(dataToSend), {headers: headers});
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        );
    }
}
