import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {ButtonPainter} from "../../services/buttonpainter";
import {Headers, Http} from "@angular/http";
@Component({
    selector: 'add-time-taxonomy',
    templateUrl: '/static/components/addtimetaxonomy/addtimetaxonomy.html'
})
export class AddTimeTaxonomyComponent {
    private endpoint: Observable<any>;

    constructor(private http:Http) {
    }

    onSubmit(form: any) {
        let exerciseName: string = form.value.time_taxonomy_name;
        ButtonPainter.paintButtonYellow('#add-time-taxonomy-submit');
        ButtonPainter.disableButton('#add-time-taxonomy-submit');

        let headers: Headers = new Headers();
        headers.append('Content-Type', 'application/json');

        let data: Object = {
            'taxonomy_name' : exerciseName
        };

        this.endpoint = this.http.post('/add-time-taxonomy', JSON.stringify(data), {headers: headers});
        this.endpoint.subscribe(
            data => {
                console.log(data)
            },
            err => {
                console.log(err)
            }
        )
    }
}