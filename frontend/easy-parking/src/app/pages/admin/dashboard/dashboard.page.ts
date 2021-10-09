/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit } from '@angular/core';
import { Parking } from '../../../core/interfaces/parking/parking';
import { ParkingService } from '../../../core/services/parking/parking/parking.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.page.html',
  styleUrls: ['./dashboard.page.scss'],
})
export class DashboardPage implements OnInit {

  parkings: Parking[];

  constructor(private parking_service: ParkingService) { }

  ngOnInit() {
    this.getParkings();
  }


  getParkings(){
    this.parking_service.listparkingsforadmin().subscribe(
      (data) => {
        this.parkings = data;
        console.log(data)
      },
      (error) => {
        console.log('Ocurrio un error');
      }
    );
   /*  this.parking_service.listparkingsTop().subscribe(
      (data) => {
        this.parkingsTops = data;
      },
      (error) => {
        console.log(error);
      }
    ); */
  }

}
