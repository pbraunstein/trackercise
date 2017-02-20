import 'zone.js';
import 'reflect-metadata';
import { Component } from '@angular/core';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';


@Component({
    selector: 'i-am',
    template: '<h2> I am {{ status }} </h2><br/><h3>Your lucky number is {{ randNum }}</h3>'
})
export class IAmAliveComponent {
    status: string;
    randNum: number;

    constructor() {
        this.status = 'Alive';
        this.randNum = 42;
    }
}

@NgModule({
    imports: [BrowserModule],
    declarations: [IAmAliveComponent],
    bootstrap: [IAmAliveComponent]
})
export class PhilTestModule { }

platformBrowserDynamic().bootstrapModule(PhilTestModule);
