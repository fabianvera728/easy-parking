/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { IonSlides } from '@ionic/angular';
import { ParkingService } from '../../../core/services/parking/parking/parking.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register-parking',
  templateUrl: './register-parking.page.html',
  styleUrls: ['./register-parking.page.scss'],
})
export class RegisterParkingPage implements OnInit {

  @ViewChild('slideParkingRegister')  slides: IonSlides;

  parking_form!: FormGroup;

  constructor(private parking_service: ParkingService, private router_service: Router) { }

  ngOnInit() {
    this.initParkingForm();
  }
  initParkingForm() {
    this.parking_form = new FormGroup({
      parking: new FormGroup({
        slug_name: new FormControl(),
        name: new FormControl(),
        description: new FormControl(),
        phone_number: new FormControl(),
        limit_image: new FormControl()
      }),
      price: new FormGroup({
        morning: new FormControl(),
        evening: new FormControl(),
        night: new FormControl(),
        weekend:new FormControl()
      }),
      address: new FormGroup({
        country: new FormControl(),
        state: new FormControl(''),
        city: new FormControl(),
        street: new FormControl(),
        number_street: new FormControl(),
        neighborhood: new FormControl(),
        description: new FormControl()
      }),
      places: new FormGroup({
        car: new FormGroup({
          type: new FormControl(2),
          reserved_limit: new FormControl()
        }),
        motorcycle: new FormGroup({
          type: new FormControl(1),
          reserved_limit: new FormControl()
        }),
        bus: new FormGroup({
          type: new FormControl(3),
          reserved_limit: new FormControl()
        })
      })
    });
  }

  swipeNext(){
    this.slides.slideNext();
  }

  onSubmit(){
    this.parking_service.createParking(this.parking_form.value).subscribe(
      (data) => {
        this.router_service.navigate(['/dashboard']);
      },
      (error) => {
        console.log(error);
      }
    );
  }

}
