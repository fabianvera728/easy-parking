/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { IonSlides } from '@ionic/angular';
import { ParkingService } from '../../core/services/parking/parking/parking.service';

@Component({
  selector: 'app-register-parking',
  templateUrl: './register-parking.page.html',
  styleUrls: ['./register-parking.page.scss'],
})
export class RegisterParkingPage implements OnInit {

  @ViewChild('slideParkingRegister') slides: IonSlides;

  parking_form!: FormGroup;

  constructor(private parking_service: ParkingService) { }

  ngOnInit() {
    this.initParkingForm();
  }
  initParkingForm() {
    this.parking_form = new FormGroup({
      parking: new FormGroup({
        slug_name: new FormControl(),
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
        neighbothood: new FormControl(),
        description: new FormControl()
      })
    });
  }

  swipeNext(){
    this.slides.slideNext();
  }

  onSubmit(){
    this.parking_service.createParking(this.parking_form.value).subscribe(
      (data) => {},
      (error) => {
        console.log(error);
      }
    );
  }

}
