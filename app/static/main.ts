import 'zone.js';
import 'reflect-metadata';
import 'jquery';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {HttpModule, CookieXSRFStrategy, XSRFStrategy} from "@angular/http";
import {AllDataComponent} from "./components/alldata/alldata";
import {LoginComponent} from "./components/login/login";
import {FormsModule} from "@angular/forms";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {LogoutComponent} from "./components/logout/logout";
import {RegisterComponent} from "./components/register/register";
import {UserDataComponent} from "./components/userdata/userdata";
import {AddTaxonomyComponent} from "./components/addtaxonomy/addtaxonomy";
import {AddHistoryComponent} from "./components/addhistory/addhistory";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
import {ApplicationComponent} from "./components/application/application";
import {LocationStrategy, HashLocationStrategy} from "@angular/common";
import {routing} from './routing';
import {IntroductionComponent} from "./components/introduction/introduction";
import {LoginGuard} from "./loginguard";


@NgModule({
    imports: [BrowserModule, HttpModule, FormsModule, routing],
    declarations: [
        ApplicationComponent, AllDataComponent, LoginComponent, CurrentUserComponent, LogoutComponent,
        RegisterComponent, UserDataComponent, AddTaxonomyComponent, AddHistoryComponent, HistoryByTaxonomyComponent,
        IntroductionComponent
    ],
    providers: [
        {provide: LocationStrategy, useClass: HashLocationStrategy},
        {provide: XSRFStrategy,  useClass: CookieXSRFStrategy},
        LoginGuard
    ],
    bootstrap: [ApplicationComponent]
})
export class TrackercizeModule {

}

platformBrowserDynamic().bootstrapModule(TrackercizeModule);
