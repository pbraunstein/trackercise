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
    selector: 'upper',
    template: `
                <div class="row">
                    <div id="ul" class="col-sm-6 col-md-6 col-lg-6">EINS</div>
                    <div id="ur" class="col-sm-6 col-md-6 col-lg-6">ZWEI</div>
                </div>
            `,
    styles: ['#ul { background-color: red } #ur { background-color: green }']
})
export class UpperComponent {

}

@Component({
    selector: 'lower',
    template: `
                <div class="row">
                    <div id="ll" class="col-sm-6 col-md-6 col-lg-6">DREI</div>
                    <div id="lr" class="col-sm-6 col-md-6 col-lg-6">VIER</div>
                </div>
            `,
    styles: ['#ll { background-color: blue }  #lr { background-color: violet }']

})
export class LowerComponent {

}

@Component({
    selector: 'application-component',
    template: `
                <div class="container">
                    <upper></upper>
                    <lower></lower>
                    <all-data></all-data>
                </div>
              `
})
export class ApplicationComponent {

}

@NgModule({
    imports: [BrowserModule, HttpModule],
    declarations: [UpperComponent, LowerComponent, ApplicationComponent, AllDataComponent],
    bootstrap:[ApplicationComponent]
})
export class PhilBox {

}

platformBrowserDynamic().bootstrapModule(PhilBox);

