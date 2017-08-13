import {Component} from "@angular/core";
import {Http} from "@angular/http";
import {Observable} from "rxjs";

@Component({
    selector:'user-data',
    templateUrl: '/static/components/userdata/userdata.html'
})
export class UserDataComponent {
    private endpoint: Observable<any>;
    private username: string;
    private taxonomy: Array<any>;
    private history: Array<any>;

    constructor(private http: Http) {
        this.endpoint = this.http.post('/user-data', '');
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => {
                this.username = data.json().nickname;
                this.taxonomy = data.json().taxonomy;
                this.history = data.json().history;
            },
            err => console.log(err)
        );
    }
}
