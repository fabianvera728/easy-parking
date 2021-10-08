import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HistoryReservationsPage } from './history-reservations.page';

const routes: Routes = [
  {
    path: '',
    component: HistoryReservationsPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class HistoryReservationsPageRoutingModule {}
