import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http, URLSearchParams} from "@angular/http";
@Component({
    selector: 'add-taxonomy',
    templateUrl: '/static/components/addtaxonomy/addtaxonomy.html'
})
export class AddTaxonomyComponent {
    private endpoint: Observable<any>;

    constructor(private http: Http) {
    }

    onSubmit(value: any) {
        let params: URLSearchParams = new URLSearchParams();
        params.set('taxonomy_name', value.taxonomy_name);
        params.set('taxonomy_is_back', AddTaxonomyComponent.booleanize(value.is_back));
        params.set('taxonomy_is_chest', AddTaxonomyComponent.booleanize(value.is_chest));
        params.set('taxonomy_is_shoulders', AddTaxonomyComponent.booleanize(value.is_shoulders));
        params.set('taxonomy_is_biceps', AddTaxonomyComponent.booleanize(value.is_biceps));
        params.set('taxonomy_is_triceps', AddTaxonomyComponent.booleanize(value.is_triceps));
        params.set('taxonomy_is_legs', AddTaxonomyComponent.booleanize(value.is_legs));
        params.set('taxonomy_is_core', AddTaxonomyComponent.booleanize(value.is_core));
        params.set('taxonomy_is_balance', AddTaxonomyComponent.booleanize(value.is_balance));
        params.set('taxonomy_is_cardio', AddTaxonomyComponent.booleanize(value.is_cardio));
        params.set('taxonomy_is_weight_per_hand', AddTaxonomyComponent.booleanize(value.is_weight_per_hand));
        this.endpoint = this.http.get('/add-rep-taxonomy', {
            search: params
        });
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
