/* eslint-disable @typescript-eslint/naming-convention */
import { Component, Input, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { ParkingService } from '../../../../core/services/parking/parking/parking.service';
import { TypesVehicle } from '../../../../core/interfaces/parking/types';
import { Vehicle } from '../../../../core/interfaces/parking/vehicle';
import { FormControl, FormGroup } from '@angular/forms';
import { StorageService } from '../../../../core/services/auth/storage/storage.service';

@Component({
    selector: 'app-modal-reservation',
    templateUrl: './menu.component.html',
    styleUrls: ['./menu.component.scss']
})
export class MenuComponent implements OnInit {


    @Input() parking_slug_name: string;


    constructor(private modalCtrl: ModalController, private storageService: StorageService, private parking_service: ParkingService) { }

    ngOnInit() {

    }

    dismiss() {
        this.modalCtrl.dismiss();
    }

    logout(){
        this.dismiss();
        this.storageService.logout();
    }

}

