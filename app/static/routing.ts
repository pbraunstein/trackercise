import {Routes, RouterModule} from "@angular/router";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {RepHistoryByTaxonomyComponent} from "./components/rephistorybytaxonomy/rephistorybytaxonomy";
import {IntroductionComponent} from "./components/introduction/introduction";
import {LoginComponent} from "./components/login/login";
import {LoginGuard} from "./loginguard";
import {HistoryByDateComponent} from "./components/historybydate/historybydate";
import {AddEntriesComponent} from "./components/addentries/addentries";

const routes: Routes = [
    {path: '', component: IntroductionComponent},
    {path: 'rep-history-by-taxonomy', component: RepHistoryByTaxonomyComponent, canActivate:[LoginGuard]},
    {path: 'history-by-date', component: HistoryByDateComponent, canActivate:[LoginGuard]},
    {path: 'add-entries', component: AddEntriesComponent, canActivate:[LoginGuard]},
    {path: 'settings', component: CurrentUserComponent, canActivate:[LoginGuard]},
    {path: 'login', component: LoginComponent},
];

export const routing = RouterModule.forRoot(routes);
