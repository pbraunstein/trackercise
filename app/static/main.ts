import 'zone.js';
import 'reflect-metadata';
import {Component} from '@angular/core';
import 'jquery';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {HttpModule} from "@angular/http";
import {AllDataComponent} from "./components/alldata/alldata";

@Component({
    selector: 'application-component',
    template: `
                <div class="container">
                    <all-data></all-data>
                </div>
              `
})
export class ApplicationComponent {

}

@NgModule({
    imports: [BrowserModule, HttpModule],
    declarations: [ApplicationComponent, AllDataComponent],
    bootstrap:[ApplicationComponent]
})
export class TrackercizeModule {

}

platformBrowserDynamic().bootstrapModule(TrackercizeModule);

