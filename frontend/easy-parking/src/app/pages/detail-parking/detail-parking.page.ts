/* eslint-disable @typescript-eslint/dot-notation */
/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ModalController } from '@ionic/angular';
import { ModalComponent } from '../../components/modal-reservation/modal-reservation.component';
import { ParkingService } from '../../core/services/parking/parking/parking.service';
import { Parking } from '../../core/interfaces/parking/parking';

@Component({
  selector: 'app-detail-parking',
  templateUrl: './detail-parking.page.html',
  styleUrls: ['./detail-parking.page.scss'],
})
export class DetailParkingPage implements OnInit {

  parking: Parking =
    {
      id: 1,
      address: {
        id: 1,
        country: "",
        state: "",
        city: "",
        street: "",
        number_street: 3,
        neighborhood: "",
        description: ""
      },
      price: {
        id: 1,
        morning: 6.0,
        evening: 14.0,
        night: 19.0,
        weekend: 20.0
      },
      slug_name: "",
      description: "",
      phone_number: "",
      limit_image: 1,
      owner: 1
    };

  constructor(private modalCtrl: ModalController, private parking_service: ParkingService, private activated_route: ActivatedRoute) { }

  ngOnInit() {
    this.getParkingData();
  }


  getParkingData() {
    this.activated_route.params.subscribe(params => {
      this.parking_service.getParking(params.slug_name).subscribe(
        (data) => {
          console.log(data);
          this.parking = data;
        },
        (error) => {
          console.log(error);
        }
      );
      console.log(params.slug_name);
    });
  }

  async openModalReservation() {
    const modal = await this.modalCtrl.create({
      component: ModalComponent,
      componentProps: { parking_slug_name: this.parking.slug_name }
    });
    return await modal.present();
  }

}
