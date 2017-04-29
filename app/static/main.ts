import 'zone.js';
import 'reflect-metadata';
import {Component} from '@angular/core';
import 'jquery';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';

@Component({
    selector: 'upper',
    template: `
                <div class="row">
                    <div class="col-sm-6 col-md-6 col-lg-6">EINS</div>
                    <div class="col-sm-6 col-md-6 col-lg-6">ZWEI</div>
                </div>
            `
})
export class UpperComponent {

}

@Component({
    selector: 'lower',
    template: `
                <div class="row">
                    <div class="col-sm-6 col-md-6 col-lg-6">DREI</div>
                    <div class="col-sm-6 col-md-6 col-lg-6">VIER</div>
                </div>
            `

})
export class LowerComponent {

}

@Component({
    selector: 'application-component',
    template: `
                <div class="container">
                    <upper></upper>
                    <lower></lower>
                </div>
              `
})
export class ApplicationComponent {

}

@NgModule({
    imports: [BrowserModule],
    declarations: [UpperComponent, LowerComponent, ApplicationComponent],
    bootstrap:[ApplicationComponent]
})
export class PhilBox {

}

platformBrowserDynamic().bootstrapModule(PhilBox);

