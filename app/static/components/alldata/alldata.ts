import {Component} from "@angular/core";
import {Http} from "@angular/http";
import {Observable} from "rxjs";

@Component({
    selector: 'all-data',
    templateUrl: '/static/components/alldata/alldata.html'
})
export class AllDataComponent {
    private endpoint: Observable<any>;
    private users: Array<any>;
    private taxonomy: Array<any>;
    private repHistory: Array<any>;

    constructor(private http: Http) {
        this.endpoint = this.http.post('/all-data', '');
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => {
                this.users = data.json().users;
                this.taxonomy = data.json().taxonomy;
                this.repHistory = data.json().history;
            },
            err => console.log(err),
        );
    }
}
