import {Component} from "@angular/core";

@Component({
    selector:'login',
    templateUrl: '/static/components/login/login.html'
})
export class LoginComponent{
    onSubmit() {
        console.log("form submitted!");
    }
}