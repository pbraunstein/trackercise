import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Headers, Http} from "@angular/http";
import {ButtonPainter} from "../../services/buttonpainter";
@Component({
    selector: 'add-rep-taxonomy',
    templateUrl: '/static/components/addreptaxonomy/addreptaxonomy.html'
})
export class AddRepTaxonomyComponent {
    private endpoint: Observable<any>;
    private buttonId: string = '#add-rep-taxonomy-submit';

    constructor(private http: Http) {
    }

    onSubmit(form: any) {
        ButtonPainter.handleFormSubmitProcessing(this.buttonId);
        let value: any = form.value;
        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');
        let data: any = {};
        data.taxonomy_name = value.taxonomy_name;
        data.taxonomy_is_back = AddRepTaxonomyComponent.booleanize(value.is_back);
        data.taxonomy_is_chest = AddRepTaxonomyComponent.booleanize(value.is_chest);
        data.taxonomy_is_shoulders = AddRepTaxonomyComponent.booleanize(value.is_shoulders);
        data.taxonomy_is_biceps = AddRepTaxonomyComponent.booleanize(value.is_biceps);
        data.taxonomy_is_triceps = AddRepTaxonomyComponent.booleanize(value.is_triceps);
        data.taxonomy_is_legs = AddRepTaxonomyComponent.booleanize(value.is_legs);
        data.taxonomy_is_core = AddRepTaxonomyComponent.booleanize(value.is_core);
        data.taxonomy_is_balance = AddRepTaxonomyComponent.booleanize(value.is_balance);
        data.taxonomy_is_cardio = AddRepTaxonomyComponent.booleanize(value.is_cardio);
        data.taxonomy_is_weight_per_hand = AddRepTaxonomyComponent.booleanize(value.is_weight_per_hand);
        this.endpoint = this.http.post('/add-rep-taxonomy', JSON.stringify(data), {headers: headers});
        this.endpoint.subscribe(
            data => {
                console.log(data);
                ButtonPainter.handleFormSubmitSuccess(form, this.buttonId);
            },
            err => {
                console.log(err);
                ButtonPainter.handleFormSubmitFailure(this.buttonId);
            }
        );
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
