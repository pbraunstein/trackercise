import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
@Component({
    selector: 'add-history',
    templateUrl: '/static/components/addhistory/addhistory.html'
})
export class AddHistoryComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http){
    }

    onSubmit(value: any){
        console.log(value);
    }
}
