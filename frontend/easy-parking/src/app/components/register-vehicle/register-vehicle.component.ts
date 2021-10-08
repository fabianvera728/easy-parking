/* eslint-disable @typescript-eslint/naming-convention */
import { Component, Input, OnInit } from '@angular/core';
import { ModalController } from '@ionic/angular';
import { ParkingService } from '../../core/services/parking/parking/parking.service';
import { TypesVehicle } from '../../core/interfaces/parking/types';
import { Vehicle } from '../../core/interfaces/parking/vehicle';
import { FormControl, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
    selector: 'app-modal-reservation',
    templateUrl: './register-vehicle.component.html',
    styleUrls: ['./register-vehicle.component.scss']
})
export class RegisterVehicleComponent implements OnInit {


    type_vehicles: TypesVehicle[];
    vehicle_form: FormGroup;

    constructor(private modalCtrl: ModalController, private roter: Router, private parking_service: ParkingService) { }

    ngOnInit() {
        this.getTypesVehicles();
        this.initVehicleForm();
    }

    dismiss() {
        this.modalCtrl.dismiss();
    }

    getTypesVehicles(){
        this.parking_service.listTypesVehicle().subscribe(
            (data) => {
                this.type_vehicles = data;
                this.vehicle_form.patchValue({type: this.type_vehicles[0].id});
            },
            (error) => {
                console.log(error);
            }
        );
    }

    initVehicleForm(){
        this.vehicle_form = new FormGroup({
            license_plate: new FormControl(),
            brand_vehicle: new FormControl(),
            description: new FormControl(),
            type: new FormControl(),
        });
    }

    onSubmit(){
        console.log(this.vehicle_form.value);
        this.parking_service.createVehicle(this.vehicle_form.value).subscribe(
            (data) => {
                this.roter.navigate(['/tabs/vehicles']);
                this.dismiss();
            },
            (error) => {
                console.log(error);
            }
        );
    }


}
