import {Component} from "@angular/core";
import {Http, URLSearchParams} from "@angular/http";
import {Observable} from "rxjs";

@Component({
    selector:'login',
    templateUrl: '/static/components/login/login.html'
})
export class LoginComponent{
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit() {
        console.log("form submitted!");
        let params: URLSearchParams = new URLSearchParams();
        params.set('hi', "Hallo");
        params.set('bye', "Tschuess");
        this.endpoint = this.http.get('/login', {
            search: params
        });
        this.endpoint.subscribe(
            data => {
                console.log(data);
            },
            err => console.log(err)
        )
    }
}