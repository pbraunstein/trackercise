import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
@Component({
    selector: 'add-taxonomy',
    templateUrl: '/static/components/addtaxonomy/addtaxonomy.html'
})
export class AddTaxonomyComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit(value: any) {
        console.log(value);
    }
}
