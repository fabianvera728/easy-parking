/* eslint-disable @typescript-eslint/naming-convention */
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
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
    return this.http.post<any>(this.BASE_URL_API + 'users/', user);
  }

}
