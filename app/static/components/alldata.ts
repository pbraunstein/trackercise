import {Observable} from "rxjs";
import {Http} from "@angular/http";
import {Component} from "@angular/core";

@Component({
    selector: 'all-data',
    template: `
                <h2>Users</h2>
                <table class="table table-striped table-condensed">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Email</th>
                            <th>Nickname</th>
                            <th>Password</th>
                            <th>Authenticated</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr *ngFor="let u of users">
                            <td>
                                {{ u.users_id }}
                            </td>
                            <td>
                                {{ u.users_email }}
                            </td>
                            <td>
                                {{ u.users_nickname }}
                            </td>
                            <td>
                                {{ u.users_password }}
                            </td>
                            <td>
                                {{ u.users_authenticated }}
                            </td>
                        </tr>
                    </tbody>
                </table>
                <h2>Taxonomy</h2>
                <table class="table table-striped table-condensed">
                    <thead>
                        <tr>
                            <th>
                                ID
                            </th>
                            <th>
                                Name
                            </th>
                            <th>
                                Is Back
                            </th>
                            <th>
                                Is Chest
                            </th>
                            <th>
                                Is Shoulders
                            </th>
                            <th>
                                Is Biceps
                            </th>
                            <th>
                                Is Triceps
                            </th>
                            <th>
                                Is Legs
                            </th>
                            <th>
                                Is Core
                            </th>
                            <th>
                                Is Balance
                            </th>
                            <th>
                                Is Cardio
                            </th>
                            <th>
                                Is Weight Per Hand
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr *ngFor="let tax of taxonomy">
                            <td>
                                {{ tax.taxonomy_id }}
                            </td>
                            <td>
                                {{ tax.taxonomy_name }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_back }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_chest }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_shoulders }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_biceps }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_triceps }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_legs }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_core }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_balance }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_cardio }}
                            </td>
                            <td>
                                {{ tax.taxonomy_is_weight_per_hand }}
                            </td>
                        </tr>
                    </tbody>
                </table>
                <h2>History</h2>
                <table class="table table-striped table-condensed">
                    <thead>
                        <tr>
                            <th>
                                ID
                            </th>
                            <th>
                                User ID
                            </th>
                            <th>
                                Exercise ID
                            </th>
                            <th>
                                Sets
                            </th>
                            <th>
                                Reps
                            </th>
                            <th>
                                Weight
                            </th>
                            <th>
                                Date
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr *ngFor="let hist of repHistory">
                            <td>
                                {{ hist.history_id }}                            
                            </td>
                            <td>
                                {{ hist.history_user_id }}                            
                            </td>
                            <td>
                                {{ hist.history_exercise_id }}                            
                            </td>
                            <td>
                                {{ hist.history_sets }}                            
                            </td>
                            <td>
                                {{ hist.history_reps }}                            
                            </td>
                            <td>
                                {{ hist.history_weight }}                            
                            </td>
                            <td>
                                {{ hist.history_date }}                            
                            </td>
                        </tr>
                    </tbody>
                </table>
            `
})
export class AllDataComponent {
    private endpoint: Observable<any>;
    private users: Array<any>;
    private taxonomy: Array<any>;
    private repHistory: Array<any>;

    constructor(private http: Http) {
        this.endpoint = http.get('/all-data');
    }

    ngOnInit() {
        this.endpoint.subscribe(
            data => {
                this.users = data.json().users;
                this.taxonomy = data.json().taxonomy;
                this.repHistory = data.json().history;
            },
            err => console.log(err),
            () => console.log("lets see how this goes")
        );
    }
}