import {Component} from "@angular/core";
import {Headers, Http} from "@angular/http";
import {Observable} from "rxjs";

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
        let dataToSend: any = {};
        dataToSend.old_password = value.current_password;
        dataToSend.new_password = value.new_password;
        dataToSend.confirm_password = value.confirm_password;

        this.endpoint = this.http.post('/change-password', JSON.stringify(dataToSend), {headers: headers});
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        );
    }
}
