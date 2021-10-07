/* eslint-disable @typescript-eslint/naming-convention */
import { Component, Input, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { ParkingService } from '../../core/services/parking/parking/parking.service';
import { TypesVehicle } from '../../core/interfaces/parking/types';
import { Vehicle } from '../../core/interfaces/parking/vehicle';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
    selector: 'app-modal-reservation',
    templateUrl: './modal-reservation.component.html',
    styleUrls: ['./modal-reservation.component.scss']
})
export class ModalComponent implements OnInit {


    @Input() parking_slug_name: string;
    type_vehicles: TypesVehicle[];
    vehicles: Vehicle[] = [
        {
            id: 1,
            owner: 1,
            license_plate: 'XLF-402',
            type: 1,
            brand_vehicle: 'Ford 350'
        },
        {
            id: 2,
            owner: 1,
            license_plate: 'sadf',
            type: 2,
            brand_vehicle: 'hola'
        }
    ];
    reserve_form: FormGroup;

    constructor(private modalCtrl: ModalController, private parking_service: ParkingService) { }

    ngOnInit() {
        this.getTypesVehicles();
        this.initReserveForm();
    }

    dismiss() {
        this.modalCtrl.dismiss();
    }

    getTypesVehicles(){
        this.parking_service.listTypesVehicle().subscribe(
            (data) => {
                this.type_vehicles = data;
            },
            (error) => {
                console.log(error);
            }
        );
    }

    initReserveForm(){
        this.reserve_form = new FormGroup({
            description: new FormControl(),
            vehicle: new FormControl(this.vehicles[0].license_plate),
            parking: new FormControl(this.parking_slug_name),
            start_timestamp: new FormControl('1995-04-15'),
            final_timestamp: new FormControl('1995-04-15'),
        });
    }

    onSubmit(){
        console.log(this.reserve_form.value);
        this.parking_service.createReservation(this.reserve_form.value).subscribe(
            (data) => {
                this.dismiss();
            },
            (error) => {
                console.log(error);
            }
        );
    }


}
