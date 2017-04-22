import 'zone.js';
import 'reflect-metadata';
import 'jquery';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Component} from '@angular/core';
import {Http, HttpModule} from '@angular/http';
import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {Observable} from "rxjs/Observable";

@Component({
    selector: 'i-am',
    template: '<h2> I am {{ status }} </h2><br/><h3>Your lucky number is {{ randNum }}</h3>'
})
export class IAmAliveComponent {
    status: string;
    randNum: number;
    endpoint: Observable<any>;

    constructor(private http: Http) {
        this.status = 'Alive';
        this.randNum = -1;
        this.endpoint = http.get('/get-rand-num');
    }

    ngOnInit() {
        this.randNum = -2;
        this.endpoint.subscribe(
            data => this.randNum = data.json().num,
            err => console.log(err),
            () => console.log("def done")
        );
    }
}

@NgModule({
    imports: [BrowserModule, HttpModule],
    declarations: [IAmAliveComponent],
    bootstrap: [IAmAliveComponent]
})
export class PhilTestModule {
}

platformBrowserDynamic().bootstrapModule(PhilTestModule);
