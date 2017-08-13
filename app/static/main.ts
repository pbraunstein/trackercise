import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap';
import 'reflect-metadata';
import 'zone.js';

import {HashLocationStrategy, LocationStrategy} from "@angular/common";
import {NgModule} from '@angular/core';
import {FormsModule} from "@angular/forms";
import {HttpModule} from "@angular/http";
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';

import {AddEntriesComponent} from "./components/addentries/addentries";
import {AddRepHistoryComponent} from "./components/addrephistory/addrephistory";
import {AddRepTaxonomyComponent} from "./components/addreptaxonomy/addreptaxonomy";
import {AddTimeHistoryComponent} from "./components/addtimehistory/addtimehistory";
import {AddTimeTaxonomyComponent} from "./components/addtimetaxonomy/addtimetaxonomy";
import {AllDataComponent} from "./components/alldata/alldata";
import {ApplicationComponent} from "./components/application/application";
import {ChangePasswordComponent} from "./components/changepassword/changepassword";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {HistoryByDateComponent} from "./components/historybydate/historybydate";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
import {IntroductionComponent} from "./components/introduction/introduction";
import {LoginComponent} from "./components/login/login";
import {RegisterComponent} from "./components/register/register";
import {RepHistoryByDateComponent} from "./components/rephistorybydate/rephistorybydate";
import {RepHistoryByTaxonomyComponent} from "./components/rephistorybytaxonomy/rephistorybytaxonomy";
import {TimeHistoryByDateComponent} from "./components/timehistorybydate/timehistorybydate";
import {TimeHistoryByTaxonomyComponent} from "./components/timehistorybytaxonomy/timehistorybytaxonomy";
import {UserDataComponent} from "./components/userdata/userdata";
import {LoginGuard} from "./loginguard";
import {routing} from './routing';
import {CSRFService} from "./services/csrfservice";
import {LogoutService} from "./services/logoutservice";

@NgModule({
    imports: [BrowserModule, HttpModule, FormsModule, routing],
    declarations: [
        ApplicationComponent, AllDataComponent, LoginComponent, CurrentUserComponent, RegisterComponent,
        UserDataComponent, AddRepTaxonomyComponent, AddRepHistoryComponent, RepHistoryByTaxonomyComponent,
        IntroductionComponent, ChangePasswordComponent, RepHistoryByDateComponent, AddEntriesComponent,
        AddTimeTaxonomyComponent, AddTimeHistoryComponent, TimeHistoryByTaxonomyComponent, HistoryByTaxonomyComponent,
        HistoryByDateComponent, TimeHistoryByDateComponent
    ],
    providers: [
        {provide: LocationStrategy, useClass: HashLocationStrategy},
        {provide: CSRFService, useClass: CSRFService},
        {provide: LogoutService, useClass: LogoutService},
        LoginGuard
    ],
    bootstrap: [ApplicationComponent]
})
export class TrackercizeModule {

}

platformBrowserDynamic().bootstrapModule(TrackercizeModule);
