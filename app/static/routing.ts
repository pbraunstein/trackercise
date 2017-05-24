import {Routes, RouterModule} from "@angular/router";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
import {IntroductionComponent} from "./components/introduction/introduction";
import {LoginComponent} from "./components/login/login";
import {LogoutComponent} from "./components/logout/logout";

const routes: Routes = [
    {path: '', component: IntroductionComponent},
    {path: 'history-by-taxonomy', component: HistoryByTaxonomyComponent},
    {path: 'settings', component: CurrentUserComponent},
    {path: 'login', component: LoginComponent},
    {path: 'logout', component: LogoutComponent}
];

export const routing = RouterModule.forRoot(routes);
