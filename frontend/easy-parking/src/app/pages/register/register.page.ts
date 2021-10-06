import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

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

  registerForm!: FormGroup;

  constructor() { }

  ngOnInit() {
  }

  compareWith(o1: any, o2: any) {
    return o1 && o2 ? o1.id === o2.id : o1 === o2;
  }

  initRegisterForm(){
    this.registerForm = new FormGroup({
      first_name: new FormControl()
    });
  }

}
