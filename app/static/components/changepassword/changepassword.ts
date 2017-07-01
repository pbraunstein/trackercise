import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, Headers} from "@angular/http";
@Component({
    selector: 'change-password',
    templateUrl: '/static/components/changepassword/changepassword.html'
})
export class ChangePasswordComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit(form: any) {
        let value: any = form.value;
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.old_password = value.current_password;
        data.new_password = value.new_password;
        data.confirm_password = value.confirm_password;

        this.endpoint = this.http.post('/change-password', JSON.stringify(data), {headers: headers});
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        );
    }
}
