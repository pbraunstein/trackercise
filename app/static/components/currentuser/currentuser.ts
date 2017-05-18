import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
@Component({
    selector:'current-user',
    templateUrl:'/static/components/currentuser/currentuser.html'
})
export class CurrentUserComponent {
    private endpoint: Observable<any>;
    private currentUser: string;

    constructor(private http: Http) {
        this.endpoint = http.post('/who-am-i', '');
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => {
                this.currentUser = data.json().user;
            },
            err => console.log(err)
        )
    }
}
