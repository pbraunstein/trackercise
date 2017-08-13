import 'zone.js';
import 'reflect-metadata';
import 'bootstrap/dist/js/bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import {NgModule} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {platformBrowserDynamic} from '@angular/platform-browser-dynamic';
import {HttpModule} from "@angular/http";
import {AllDataComponent} from "./components/alldata/alldata";
import {LoginComponent} from "./components/login/login";
import {FormsModule} from "@angular/forms";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {RegisterComponent} from "./components/register/register";
import {UserDataComponent} from "./components/userdata/userdata";
import {AddRepTaxonomyComponent} from "./components/addreptaxonomy/addreptaxonomy";
import {AddRepHistoryComponent} from "./components/addrephistory/addrephistory";
import {RepHistoryByTaxonomyComponent} from "./components/rephistorybytaxonomy/rephistorybytaxonomy";
import {ApplicationComponent} from "./components/application/application";
import {LocationStrategy, HashLocationStrategy} from "@angular/common";
import {routing} from './routing';
import {IntroductionComponent} from "./components/introduction/introduction";
import {LoginGuard} from "./loginguard";
import {CSRFService} from "./services/csrfservice";
import {LogoutService} from "./services/logoutservice";
import {ChangePasswordComponent} from "./components/changepassword/changepassword";
import {RepHistoryByDateComponent} from "./components/rephistorybydate/rephistorybydate";
import {AddEntriesComponent} from "./components/addentries/addentries";
import {AddTimeTaxonomyComponent} from "./components/addtimetaxonomy/addtimetaxonomy";
import {AddTimeHistoryComponent} from "./components/addtimehistory/addtimehistory";
import {TimeHistoryByTaxonomyComponent} from "./components/timehistorybytaxonomy/timehistorybytaxonomy";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
import {HistoryByDateComponent} from "./components/historybydate/historybydate";
import {TimeHistoryByDateComponent} from "./components/timehistorybydate/timehistorybydate";


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
