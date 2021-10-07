/* eslint-disable @typescript-eslint/naming-convention */
import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
import { AuthService } from '../../core/services/auth/auth.service';
import { StorageService } from '../../core/services/auth/storage/storage.service';
import { Session } from '../../core/interfaces/utils/Session';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.page.html',
  styleUrls: ['./register.page.scss'],
})
export class RegisterPage implements OnInit {

  users: any[] = [
    {
      id: 1,
      rol: 'Client',
    },
    {
      id: 2,
      rol: 'Admin parking',
    }
  ];

  register_form!: FormGroup;

  constructor(private auth_service: AuthService, private router_service: Router, private storage_service: StorageService) { }

  ngOnInit() {
    this.initRegisterForm();
  }

  compareWith(o1: any, o2: any) {
    return o1 && o2 ? o1.id === o2.id : o1 === o2;
  }

  initRegisterForm() {
    this.register_form = new FormGroup({
      phone_number: new FormControl(),
      picture: new FormControl('"https://www.pixsy.com/wp-content/uploads/2021/04/ben-sweet-2LowviVHZ-E-unsplash-1.jpeg"'),
      biography: new FormControl(),
      user: new FormGroup({
        password: new FormControl(),
        is_superuser: new FormControl(),
        username: new FormControl(),
        first_name: new FormControl(),
        last_name: new FormControl(),
        email: new FormControl(),
      })
    });
  }

  onSubmit() {
    console.log(this.register_form);
    this.auth_service.register(this.register_form.value).subscribe(
      (data) => {
        console.log(data);
        const session: Session = data.data;
        this.router_service.navigate([session.user.user.is_superuser ? '/register-parking' : '/home']);
        this.storage_service.setCurrentSession(session);
      },
      (error) => {
        console.log(error);
      }
    );
  }
}
