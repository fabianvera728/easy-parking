import { Component, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { MenuComponent } from '../menu/menu.component';

@Component({
  selector: 'app-toolbar',
  templateUrl: './toolbar.component.html',
  styleUrls: ['./toolbar.component.scss'],
})
export class ToolbarComponent implements OnInit {

  constructor(private modalCtrl: ModalController) { }

  ngOnInit() {}


  async openModal(){
    const modal = await this.modalCtrl.create({
      component: MenuComponent,
    });
    return await modal.present();
  }

}
