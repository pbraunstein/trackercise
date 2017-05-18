import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, URLSearchParams, Headers} from "@angular/http";
@Component({
    selector: 'add-taxonomy',
    templateUrl: '/static/components/addtaxonomy/addtaxonomy.html'
})
export class AddTaxonomyComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit(value: any) {
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.taxonomy_name = value.taxonomy_name;
        data.taxonomy_is_back = AddTaxonomyComponent.booleanize(value.is_back);
        data.taxonomy_is_chest = AddTaxonomyComponent.booleanize(value.is_chest);
        data.taxonomy_is_shoulders = AddTaxonomyComponent.booleanize(value.is_shoulders);
        data.taxonomy_is_biceps = AddTaxonomyComponent.booleanize(value.is_biceps);
        data.taxonomy_is_triceps = AddTaxonomyComponent.booleanize(value.is_triceps);
        data.taxonomy_is_legs = AddTaxonomyComponent.booleanize(value.is_legs);
        data.taxonomy_is_core = AddTaxonomyComponent.booleanize(value.is_core);
        data.taxonomy_is_balance = AddTaxonomyComponent.booleanize(value.is_balance);
        data.taxonomy_is_cardio = AddTaxonomyComponent.booleanize(value.is_cardio);
        data.taxonomy_is_weight_per_hand = AddTaxonomyComponent.booleanize(value.is_weight_per_hand);
        this.endpoint = this.http.post('/add-rep-taxonomy', JSON.stringify(data), {headers: headers});
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err),
        )
    }

    /**
     * Takes in either a boolean or an empty string. If an empty string, returns a string representation of the false
     * boolean. Otherwise, returns a string representation of the boolean passed in.
     */
    private static booleanize(input: any): string {
        if (input) {
            return String(input);
        } else {
            return String(false);
        }
    }
}
