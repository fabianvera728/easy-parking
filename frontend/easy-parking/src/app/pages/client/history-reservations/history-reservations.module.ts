import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { HistoryReservationsPageRoutingModule } from './history-reservations-routing.module';

import { HistoryReservationsPage } from './history-reservations.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    HistoryReservationsPageRoutingModule
  ],
  declarations: [HistoryReservationsPage]
})
export class HistoryReservationsPageModule {}
