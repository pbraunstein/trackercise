import {Routes, RouterModule} from "@angular/router";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
import {IntroductionComponent} from "./components/introduction/introduction";
const routes: Routes = [
    {path: '', component: IntroductionComponent},
    {path: 'history-by-taxonomy', component: HistoryByTaxonomyComponent},
    {path: 'settings', component: CurrentUserComponent}
];

export const routing = RouterModule.forRoot(routes);
