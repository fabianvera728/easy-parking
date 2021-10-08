import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { DetailParkingPage } from './detail-parking.page';

const routes: Routes = [
  {
    path: '',
    component: DetailParkingPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class DetailParkingPageRoutingModule {}
