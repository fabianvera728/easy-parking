/* eslint-disable @typescript-eslint/naming-convention */
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../../environments/environment';
import { User } from '../../interfaces/user/user';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  BASE_URL_API = environment.BASE_URL_API;


  constructor(private http: HttpClient) { }

  login(user: any): Observable<any> {
    return this.http.post<User>(`${this.BASE_URL_API}users/login/`,user);
   }

  logout() { }

  register(user: any): Observable<any> {
    console.log(user);
    /* const headers = new HttpHeaders({'content-type':'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW'});
    var formData = new FormData();
    formData.append('phone_number', user.phone_number);
    formData.append('user', user.user);
    formData.append('picture', user.picture);
    formData.append('biography', user.biography);
    console.log(formData); */
    return this.http.post<any>(this.BASE_URL_API + 'users/',
    user);
  }

}
