import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { ModalComponent } from '../../components/modal-reservation/modal-reservation.component';

@Component({
  selector: 'app-detail-parking',
  templateUrl: './detail-parking.page.html',
  styleUrls: ['./detail-parking.page.scss'],
})
export class DetailParkingPage implements OnInit {

  constructor(private modalCtrl: ModalController) { }

  ngOnInit() {
  }

  async openModalReservation(){
    const modal = await this.modalCtrl.create({
      component: ModalComponent
    });
    return await modal.present();
  }

}
