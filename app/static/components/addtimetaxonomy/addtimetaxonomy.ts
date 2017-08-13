import {Component} from "@angular/core";
import {Headers, Http} from "@angular/http";
import {Observable} from "rxjs";

import {ButtonPainter} from "../../services/buttonpainter";

@Component({
    selector: 'add-time-taxonomy',
    templateUrl: '/static/components/addtimetaxonomy/addtimetaxonomy.html'
})
export class AddTimeTaxonomyComponent {
    private endpoint: Observable<any>;
    private buttonId: string = '#add-time-taxonomy-submit';

    constructor(private http:Http) {
    }

    onSubmit(form: any) {
        let exerciseName: string = form.value.time_taxonomy_name;
        ButtonPainter.handleFormSubmitProcessing(this.buttonId);

        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');

        let dataToSend: Object = {
            'taxonomy_name' : exerciseName
        };

        this.endpoint = this.http.post('/add-time-taxonomy', JSON.stringify(dataToSend), {headers: headers});
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
}
