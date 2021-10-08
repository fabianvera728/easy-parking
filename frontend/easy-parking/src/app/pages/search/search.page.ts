/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit } from '@angular/core';
import { ParkingService } from '../../core/services/parking/parking/parking.service';
import { Parking } from '../../core/interfaces/parking/parking';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-search',
  templateUrl: './search.page.html',
  styleUrls: ['./search.page.scss'],
})
export class SearchPage implements OnInit {

  parkings: Parking[] = [];
  search = '';
  search_form: FormGroup;

  constructor(private parking_service: ParkingService) { }

  ngOnInit() {
    this.initSearchForm();
  }


  initSearchForm(){
    this.search_form = new FormGroup({
      search: new FormControl('')
    });
  }

  onSubmit(){
    this.parking_service.searchParking(this.search_form.value.search).subscribe(
      (data) => {
        this.parkings = data;
      },
      (error) => {
        console.log(error);
      }
    );
  }

}
