/* eslint-disable @typescript-eslint/naming-convention */
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../../../environments/environment';
import { Address } from '../../../interfaces/parking/address';
import { Price } from '../../../interfaces/parking/price';
import { Parking } from '../../../interfaces/parking/parking';
import { StorageService } from '../../auth/storage/storage.service';
import { TypesVehicle } from '../../../interfaces/parking/types';


@Injectable({
  providedIn: 'root'
})
export class ParkingService {

  BASE_URL_API = environment.BASE_URL_API;


  constructor(private http: HttpClient, private storage_service: StorageService) { }

  listparkings() {
    return this.http.get<Parking[]>(`${this.BASE_URL_API}parkings/`);
  }

  createParking(parking: any) {
    const owner = this.storage_service.getCurrentSession().user.user.id;
    /* let address: number;
    let price: number;

    this.createAddress(parking.address).subscribe(
      (data) => {
        address = data.id;
      }
    );
    this.createPrice(parking.price).subscribe(
      (data) => {
        price = data.id;
      }
    ); */

    const parking_data: any = {
      ...parking.parking,
      address: parking.address,
      price: parking.price,
      owner: owner
    };
    console.log(parking_data);

    return this.http.post<Parking>(this.BASE_URL_API + 'parkings/', parking_data);
  }

  listTypesVehicle(){
    return this.http.get<TypesVehicle[]>(`${this.BASE_URL_API}types/`);
  }

  createReservation(data: any){
    return this.http.post<any>(`${this.BASE_URL_API}reservations/`, data);
  }

  /* createAddress(address: Address) {
    return this.http.post<Address>(this.BASE_URL_API + 'addresses/', address);
  }

  createPrice(price: Price) {
    return this.http.post<Price>(this.BASE_URL_API + 'prices/', price);
  } */

}
