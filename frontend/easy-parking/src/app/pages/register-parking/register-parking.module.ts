import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { RegisterParkingPageRoutingModule } from './register-parking-routing.module';
import { RegisterParkingPage } from './register-parking.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RegisterParkingPageRoutingModule,
    ReactiveFormsModule,
    FormsModule
  ],
  declarations: [RegisterParkingPage]
})
export class RegisterParkingPageModule {}
