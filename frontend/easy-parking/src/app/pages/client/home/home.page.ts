/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit } from '@angular/core';
import { Parking } from '../../../core/interfaces/parking/parking';
import { ParkingService } from '../../../core/services/parking/parking/parking.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {

  parkings: Parking[];
  parkingsTops: Parking[];

  constructor(private parking_service: ParkingService) {}

  ngOnInit(){
    this.getParkings();
  }

  getParkings(){
    this.parking_service.listparkings().subscribe(
      (data) => {
        this.parkings = data;
      },
      (error) => {
        console.log('Ocurrio un error');
      }
    );
    this.parking_service.listparkingsTop().subscribe(
      (data) => {
        this.parkingsTops = data;
      },
      (error) => {
        console.log(error);
      }
    );
  }




}
