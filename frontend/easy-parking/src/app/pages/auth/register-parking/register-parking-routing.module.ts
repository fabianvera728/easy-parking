import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { RegisterParkingPage } from './register-parking.page';

const routes: Routes = [
  {
    path: '',
    component: RegisterParkingPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class RegisterParkingPageRoutingModule {}
