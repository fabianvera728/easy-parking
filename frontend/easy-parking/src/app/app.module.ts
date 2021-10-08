import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouteReuseStrategy } from '@angular/router';
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { ModalComponent } from './components/modal-reservation/modal-reservation.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { RegisterVehicleComponent } from './components/register-vehicle/register-vehicle.component';

@NgModule({
  declarations: [AppComponent, ModalComponent, RegisterVehicleComponent],
  entryComponents: [ModalComponent, RegisterVehicleComponent],
  imports: [BrowserModule, ReactiveFormsModule, FormsModule, IonicModule.forRoot(), AppRoutingModule , HttpClientModule],
  providers: [{ provide: RouteReuseStrategy, useClass: IonicRouteStrategy }],
  bootstrap: [AppComponent],
})
export class AppModule {}
