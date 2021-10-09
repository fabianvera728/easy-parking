import { Router } from '@angular/router';
import { Injectable } from '@angular/core';
import { Session } from '../../../interfaces/utils/Session';
import { User } from '../../../interfaces/user/user';

@Injectable({
  providedIn: 'root',
})
export class StorageService {
  private localStorageService;
  private currentSession!: Session | null;

  constructor(private router: Router) {
    this.localStorageService = localStorage;
    this.currentSession = this.loadSessionData();
  }

  setCurrentSession(session: Session): void {
    this.currentSession = session;
    this.localStorageService.setItem('currentUser', JSON.stringify(session));
  }

  loadSessionData(): Session | null {
    const sessionStr = this.localStorageService.getItem('currentUser');
    // eslint-disable-next-line @typescript-eslint/consistent-type-assertions
    return sessionStr ? <Session>JSON.parse(sessionStr) : null;
  }

  getCurrentSession(): Session | null {
    return this.loadSessionData();
  }

  removeCurrentSession(): void {
    this.localStorageService.removeItem('currentUser');
    this.currentSession = null;
  }

  getCurrentUser(): User | null {
    const session: Session | null = this.getCurrentSession();
    return session && session.user ? session.user : null;
  }

  isAuthenticated(): boolean {
    /* return this.getCurrentToken() != null ? true : true; */
    return this.getCurrentUser() != null ? true : false;
  }

  getCurrentToken(): string | null {
    const session = this.getCurrentSession();
    return session && session.token ? session.token : null;
  }

  logout(): void {
    this.removeCurrentSession();
    this.router.navigate(['/login']);
  }

 /*  generateHeaders(): HttpHeaders {
    const auth_token = this.getCurrentSession()?.token;
    return new HttpHeaders({
      "Content-Type": "application/json",
      Authorization: `Bearer ${auth_token}`,
    });
  }

  isVisibleByRoles(roles: string[]): boolean {

    const user = this.getCurrentUser();
    if (user) {
      return roles.some((rol) => user.role._id?.$oid == rol);
    }
    return false;
  } */
}
