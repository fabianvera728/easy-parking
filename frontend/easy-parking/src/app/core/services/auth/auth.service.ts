/* eslint-disable @typescript-eslint/naming-convention */
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  BASE_URL_API = environment.BASE_URL_API;


  constructor(private http: HttpClient) { }

  login() { }

  logout() { }

  register(user: any): Observable<any> {
    console.log(user);
    const headers = new HttpHeaders({ 'Content-Type': 'multipart/form-data',});
    const formData: any = new FormData();
    formData.append('phone_number', user.phone_number);
    formData.append('user', user.user);
    formData.append('picture', user.picture);
    formData.append('biography', user.biography);
    return this.http.post<any>(this.BASE_URL_API + 'users/',
    formData, {headers});
  }

}
