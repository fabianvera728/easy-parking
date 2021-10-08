/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { RegisterVehicleComponent } from '../../../components/register-vehicle/register-vehicle.component';
import { Vehicle } from '../../../core/interfaces/parking/vehicle';
import { ParkingService } from '../../../core/services/parking/parking/parking.service';

@Component({
  selector: 'app-vehicles',
  templateUrl: './vehicles.page.html',
  styleUrls: ['./vehicles.page.scss'],
})
export class VehiclesPage implements OnInit {

  vehicles: Vehicle[] = [];


  constructor(private modalCtrl: ModalController, private parking_service: ParkingService) { }

  ngOnInit() {
    this.getVehicles();
  }

  async openModalAddVehicle(){
    const modal = await this.modalCtrl.create({
      component: RegisterVehicleComponent
    });
    return await modal.present();
  }


  getVehicles(){
    this.parking_service.getVehicles().subscribe(
      (data) => {
        this.vehicles = data;
        console.log(data);
      },
      (error) => {
        console.log(error);
      }
    );
  }


}
