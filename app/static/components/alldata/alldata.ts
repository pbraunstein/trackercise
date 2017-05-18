import {Observable} from "rxjs";
import {Http} from "@angular/http";
import {Component} from "@angular/core";

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
        this.endpoint = http.post('/all-data', '');
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
