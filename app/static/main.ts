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
import {LoginComponent} from "./components/login/login";
import {FormsModule} from "@angular/forms";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {LogoutComponent} from "./components/logout/logout";
import {RegisterComponent} from "./components/register/register";
import {UserDataComponent} from "./components/userdata/userdata";
import {AddTaxonomyComponent} from "./components/addtaxonomy/addtaxonomy";
import {AddHistoryComponent} from "./components/addhistory/addhistory";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";

@Component({
    selector: 'application-component',
    template: `
                <nav class="navbar navbar-default">
                </nav>
                    <div class="container">
                        <current-user></current-user>
                        <login></login>
                        <register></register>
                        <logout></logout>
                        <add-taxonomy></add-taxonomy>
                        <add-history></add-history>
                        <history-by-taxonomy></history-by-taxonomy>
                        <user-data></user-data>
                        <all-data></all-data>
                    </div>
              `
})
export class ApplicationComponent {

}

@NgModule({
    imports: [BrowserModule, HttpModule, FormsModule],
    declarations: [
        ApplicationComponent, AllDataComponent, LoginComponent, CurrentUserComponent, LogoutComponent,
        RegisterComponent, UserDataComponent, AddTaxonomyComponent, AddHistoryComponent, HistoryByTaxonomyComponent
    ],
    bootstrap:[ApplicationComponent]
})
export class TrackercizeModule {

}

platformBrowserDynamic().bootstrapModule(TrackercizeModule);
