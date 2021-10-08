import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthService } from '../../../core/services/auth/auth.service';
import { Router } from '@angular/router';
import { StorageService } from '../../../core/services/auth/storage/storage.service';
import { Session } from '../../../core/interfaces/utils/Session';

@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {

  loginForm!: FormGroup;


  // eslint-disable-next-line @typescript-eslint/naming-convention
  constructor(private auth_service: AuthService, private router_service: Router, private storage_service: StorageService) { }

  ngOnInit() {
    this.initLoginForm();
  }

  initLoginForm(){
    this.loginForm = new FormGroup({
      username: new FormControl(),
      password: new FormControl()
    });
  }
  onSubmit() {
    this.auth_service.login(this.loginForm.value).subscribe(
      (data) => {
        console.log(data);
        const session: Session =({user: data}) ;
        console.log(session);
        this.router_service.navigate(['/tabs']);
        this.storage_service.setCurrentSession(session);
      },
      (error) => {
        console.log(error);
      }
    );
  }

}
