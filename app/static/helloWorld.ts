import 'zone.js';
import 'reflect-metadata';
import { Component } from '@angular/core';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';


@Component({
    selector: 'i-am',
    template: '<h2> I am {{ status }} </h2>'
})
export class IAmAliveComponent {
    status: string;

    constructor() {
        this.status = 'Alive';
    }
}

@NgModule({
    imports: [BrowserModule],
    declarations: [IAmAliveComponent],
    bootstrap: [IAmAliveComponent]
})
export class PhilTestModule { }

platformBrowserDynamic().bootstrapModule(PhilTestModule);
