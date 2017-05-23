import {Routes, RouterModule} from "@angular/router";
import {CurrentUserComponent} from "./components/currentuser/currentuser";
import {AllDataComponent} from "./components/alldata/alldata";
const routes: Routes = [
    {path: '', component: CurrentUserComponent},
    {path: 'all-data', component: AllDataComponent}
];

export const routing = RouterModule.forRoot(routes);
