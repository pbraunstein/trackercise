import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
@Component({
    selector:'user-data',
    templateUrl: '/static/components/userdata/userdata.html'
})
export class UserDataComponent {
    private endpoint: Observable<any>

    constructor(private http: Http) {
        this.endpoint.get('/user-data')
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err)
        )
    }
}
