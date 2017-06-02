import {Routes, RouterModule} from "@angular/router";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
import {IntroductionComponent} from "./components/introduction/introduction";
import {LoginComponent} from "./components/login/login";
import {LoginGuard} from "./loginguard";
import {AddHistoryComponent} from "./components/addhistory/addhistory";
import {AddTaxonomyComponent} from "./components/addtaxonomy/addtaxonomy";

const routes: Routes = [
    {path: '', component: IntroductionComponent},
    {path: 'history-by-taxonomy', component: HistoryByTaxonomyComponent, canActivate:[LoginGuard]},
    {path: 'add-history-entry', component: AddHistoryComponent, canActivate:[LoginGuard]},
    {path: 'add-taxonomy-entry', component: AddTaxonomyComponent, canActivate:[LoginGuard]},
    {path: 'settings', component: CurrentUserComponent, canActivate:[LoginGuard]},
    {path: 'login', component: LoginComponent},
];

export const routing = RouterModule.forRoot(routes);
