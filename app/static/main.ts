import 'zone.js';
import 'reflect-metadata';
import {Component} from '@angular/core';
import {Http, HttpModule} from '@angular/http';
import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {Observable} from "rxjs/Observable";

@Component({
    selector: 'eins',
    template: '<h1 class="eins">EINS</h1>'
})
export class EinsComponent {

}

@Component({
    selector: 'zwei',
    template: '<h1 class="zwei">zwei</h1>'

})
export class ZweiComponent {

}

@Component({
    selector: 'drei',
    template: '<h1 class="drei">drei</h1>'
})
export class DreiComponent {

}

@Component({
    selector: 'vier',
    template: '<h1 class="vier">vier</h1>'
})
export class VierComponent {

}

@NgModule({
    imports: [BrowserModule],
    declarations: [EinsComponent, ZweiComponent, DreiComponent, VierComponent],
    bootstrap:[EinsComponent, ZweiComponent, DreiComponent, VierComponent]
})
export class PhilBox {

}

platformBrowserDynamic().bootstrapModule(PhilBox);

