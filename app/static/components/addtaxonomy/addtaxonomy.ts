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
        params.set('name', AddTaxonomyComponent.booleanize(value.taxonomy_name));
        params.set('is_back', AddTaxonomyComponent.booleanize(value.is_back));
        params.set('is_chest', AddTaxonomyComponent.booleanize(value.is_chest));
        params.set('is_shoulders', AddTaxonomyComponent.booleanize(value.is_shoulders));
        params.set('is_biceps', AddTaxonomyComponent.booleanize(value.is_biceps));
        params.set('is_triceps', AddTaxonomyComponent.booleanize(value.is_triceps));
        params.set('is_legs', AddTaxonomyComponent.booleanize(value.is_legs));
        params.set('is_core', AddTaxonomyComponent.booleanize(value.is_core));
        params.set('is_balance', AddTaxonomyComponent.booleanize(value.is_balance));
        params.set('is_cardio', AddTaxonomyComponent.booleanize(value.is_cardio));
        params.set('is_weight_per_hand', AddTaxonomyComponent.booleanize(value.is_weight_per_hand));
        this.endpoint = this.http.get('/add-rep-taxonomy', {
            search: params
        });
        this.endpoint.subscribe(
            data => console.log(data),
            err => console.log(err),
        )
    }

    private static booleanize(input: any): string {
        if (input) {
            return String(input);
        } else {
            return String(false);
        }
    }
}
