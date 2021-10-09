/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ParkingService } from '../../../core/services/parking/parking/parking.service';

@Component({
  selector: 'app-history-reservations',
  templateUrl: './history-reservations.page.html',
  styleUrls: ['./history-reservations.page.scss'],
})
export class HistoryReservationsPage implements OnInit {

  reservations: any[] = [];

  constructor(private active_route: ActivatedRoute, private parking_service: ParkingService) { }

  ngOnInit() {
    this.getHistoryReservations();
  }

  getHistoryReservations(){
    this.active_route.params.subscribe(params => {
      this.parking_service.getReservations().subscribe(
        (data) => {
          this.reservations = data;
        },
        (error) => {
          console.log(error);
        }
      );
    }
    );
  }


}
