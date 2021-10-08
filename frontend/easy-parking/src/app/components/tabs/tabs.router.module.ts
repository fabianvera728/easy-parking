import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TabsPage } from './tabs.page';
import { IonicModule } from '@ionic/angular';
import { AuthorizedGuard } from '../../core/guards/authorized.guard';

const routes: Routes = [
  {
    path: 'tabs',
    canActivate: [AuthorizedGuard],
    data: {
      access: ['client', 'admin']
    },
    component: TabsPage,
    children: [
      {
        path: 'home',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/client/home/home.module').then(m => m.HomePageModule)
          }
        ],
        canActivate: [AuthorizedGuard],
        data: {
          access: ['client', 'admin']
        }
      },
      {
        path: 'search',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/client/search/search.module').then(m => m.SearchPageModule)
          }
        ]
      },
      {
        path: 'vehicles',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/client/vehicles/vehicles.module').then(m => m.VehiclesPageModule)
          }
        ]
      },
      {
        path: 'reservations',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/client/history-reservations/history-reservations.module').then(m => m.HistoryReservationsPageModule)
          }
        ]
      },
      {
        path: '',
        redirectTo: '/tabs/home',
        pathMatch: 'full'
      }
    ]
  },
  {
    path: '',
    redirectTo: '/tabs/home',
    pathMatch: 'full'
  }
];

@NgModule({
  imports: [
    IonicModule,
    RouterModule.forChild(routes)
  ],
  exports: [RouterModule]
})
export class TabsPageRoutingModule { }
