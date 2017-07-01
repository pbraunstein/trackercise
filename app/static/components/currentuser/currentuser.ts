import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
import * as d3 from 'd3';

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
        let data = [30, 86, 168, 281, 303, 365, 1000];

        d3.select(".chart")
          .selectAll("div")
          .data(data)
            .enter()
            .append("div")
            .style("width", function(d) { return d + "px"; })
            .style("background-color", function(d) {return 'steelblue'})
            .text(function(d) { return d; });
            }
}
