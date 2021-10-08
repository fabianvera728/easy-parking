/* eslint-disable @typescript-eslint/ban-types */
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
import { Place } from '../../../interfaces/parking/place';


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
    const parking_data: any = {
      ...parking.parking,
      address: parking.address,
      price: parking.price,
      places: parking.places,
      owner
    };
    console.log(parking_data);

    return this.http.post<Parking>(this.BASE_URL_API + 'parkings/', parking_data);
  }

  getParking(slug_name: string){
    return this.http.get<Parking>(`${this.BASE_URL_API}parkings/${slug_name}/`);
  }


  listTypesVehicle(){
    return this.http.get<TypesVehicle[]>(`${this.BASE_URL_API}types/`);
  }

  createReservation(data: any){
    return this.http.post<any>(`${this.BASE_URL_API}reservations/`, data);
  }

  getReservations(){
    const owner = this.storage_service.getCurrentSession();
    return this.http.get<any>(`${this.BASE_URL_API}users/${owner.user.user.username}/reservations/`);
  }

  searchParking(keyword: String){
    return this.http.get<Parking[]>(`${this.BASE_URL_API}parkings/?search=${keyword}`);
  }

  getParkingPlaces(slug_name: string){
    return this.http.get<Place>(`${this.BASE_URL_API}parkings/${slug_name}/places`);
  }


}
