import {Routes, RouterModule} from "@angular/router";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {AllDataComponent} from "./components/alldata/alldata";
import {HistoryByTaxonomyComponent} from "./components/historybytaxonomy/historybytaxonomy";
const routes: Routes = [
    {path: '', component: CurrentUserComponent},
    {path: 'all-data', component: AllDataComponent},
    {path: 'history-by-taxonomy', component: HistoryByTaxonomyComponent}
];

export const routing = RouterModule.forRoot(routes);
