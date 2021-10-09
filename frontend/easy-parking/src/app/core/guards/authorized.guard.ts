/* eslint-disable @typescript-eslint/naming-convention */
/* eslint-disable @typescript-eslint/dot-notation */
/* eslint-disable @typescript-eslint/quotes */
import { Injectable } from "@angular/core";
import { StorageService } from '../services/auth/storage/storage.service';
import {
  ActivatedRoute,
  ActivatedRouteSnapshot,
  CanActivate,
  Router,
  RouterStateSnapshot,
} from "@angular/router";

@Injectable({
  providedIn: "root",
})
export class AuthorizedGuard implements CanActivate {
  constructor(private router: Router, private storageService: StorageService) {}

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    if (!this.storageService.isAuthenticated()) {
      this.router.navigate(["/welcome"]);
      return false;
    }
    const user = this.storageService.getCurrentUser();
    console.log(user);
    const access = route.data["access"];
    const is_autorized = access.some(
        (acc: string) => (acc === "client" && !user.user.is_superuser ) || (acc === "admin" && user.user.is_superuser )
    );
    console.log(is_autorized);
    if (is_autorized) {
      return true;
    }
    this.router.navigate([user.user.is_superuser ? "/dashboard" : '/tabs']);
    return false;
  }
}
