import {RouterModule, Routes} from "@angular/router";

import {AddEntriesComponent} from "./components/addentries/addentries";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {HistoryByDateComponent} from "./components/historybydate/historybydate";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
import {IntroductionComponent} from "./components/introduction/introduction";
import {LoginComponent} from "./components/login/login";
import {LoginGuard} from "./loginguard";

const routes: Routes = [
    {path: '', component: IntroductionComponent},
    {path: 'history-by-taxonomy', component: HistoryByTaxonomyComponent, canActivate:[LoginGuard]},
    {path: 'history-by-date', component: HistoryByDateComponent, canActivate:[LoginGuard]},
    {path: 'add-entries', component: AddEntriesComponent, canActivate:[LoginGuard]},
    {path: 'settings', component: CurrentUserComponent, canActivate:[LoginGuard]},
    {path: 'login', component: LoginComponent},
];

export const routing = RouterModule.forRoot(routes);
