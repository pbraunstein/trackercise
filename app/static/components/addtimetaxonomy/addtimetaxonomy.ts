import {Component} from "@angular/core";
import {Observable} from "rxjs";
@Component({
    selector: 'add-time-taxonomy',
    templateUrl: '/static/components/addtimetaxonomy/addtimetaxonomy.html'
})
export class AddTimeTaxonomyComponent {
    private endpoint: Observable<any>;
}