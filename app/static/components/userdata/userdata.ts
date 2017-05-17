import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
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
        this.endpoint = http.get('/user-data')
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => {
                this.username = data.json().nickname;
                this.taxonomy = data.json().taxonomy;
                this.history = data.json().history;
                console.log(this.username);
                console.log(this.taxonomy);
                console.log(this.history);
            },
            err => console.log(err)
        )
    }
}