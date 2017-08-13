import {Component} from "@angular/core";
import {Http} from "@angular/http";
import {Observable} from "rxjs";

@Component({
    selector:'current-user',
    templateUrl:'/static/components/currentuser/currentuser.html'
})
export class CurrentUserComponent {
    private endpoint: Observable<any>;
    private currentUser: string;
    private currentPassword: string;

    constructor(private http: Http) {
        this.endpoint = http.post('/who-am-i', '');
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => {
                this.currentUser = data.json().user;
                this.currentPassword = data.json().password;
            },
            err => console.log(err)
        );
    }
}
