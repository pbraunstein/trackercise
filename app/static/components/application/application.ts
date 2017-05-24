import {Component} from "@angular/core";
@Component({
    selector: 'application-component',
    templateUrl: '/static/components/application/application.html',
    styles: [
        `#navbar_botom {margin-bottom: 0; border-radius: 0; position: fixed; bottom: 0; left: 0; right: 0;}`,
        `#buffer {height: 70px}`
    ]
})
export class ApplicationComponent {
}
