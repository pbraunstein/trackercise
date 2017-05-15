import {Component} from "@angular/core";
import {Observable} from "rxjs";
import {Http} from "@angular/http";
declare const $:JQueryStatic;

@Component({
    selector: 'add-history',
    templateUrl: '/static/components/addhistory/addhistory.html'
})
export class AddHistoryComponent {
    private endpoint_exercise_pairs: Observable<any>;
    private endpoint_add_history: Observable<any>;

    constructor(private http: Http){
        this.endpoint_exercise_pairs = http.get('/get-valid-id-exercise-pairs');
    }

    ngOnInit() {
        this.endpoint_exercise_pairs.subscribe(
            data => {
                console.log(data);
                this.prepareDropdown(data.json().pairs)
            },
            err => console.log(err)
        );
    }

    prepareDropdown(pairs: Array<any>): void {
        for (let x of pairs) {
            $("#excercises_dropdown").append("<li><a>" + x[1] + "</a></li>");
        }
        console.log(pairs)
    }

    onSubmit(value: any){
        console.log(value);
    }
}
