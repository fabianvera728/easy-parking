import { Component, OnInit } from '@angular/core';

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

  constructor() { }

  ngOnInit() {
  }

  compareWith(o1: any, o2: any) {
    return o1 && o2 ? o1.id === o2.id : o1 === o2;
  }

}
