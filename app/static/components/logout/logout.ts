import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";

@Component({
    selector: 'logout',
    templateUrl: '/static/components/logout/logout.html'
})
export class LogoutComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
        this.endpoint = http.post('/logout', '');
    }

    onSubmit() {
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        )
    }
}
