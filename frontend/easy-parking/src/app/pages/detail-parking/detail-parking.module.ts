import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { DetailParkingPageRoutingModule } from './detail-parking-routing.module';

import { DetailParkingPage } from './detail-parking.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    DetailParkingPageRoutingModule
  ],
  declarations: [DetailParkingPage]
})
export class DetailParkingPageModule {}
