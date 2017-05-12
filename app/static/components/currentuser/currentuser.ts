import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
@Component({
    selector:'current-user',
    templateUrl:'/static/components/currentuser/currentuser.html'
})
export class CurrentUserComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
        this.endpoint = http.get('/who-am-i')
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        )
    }
}