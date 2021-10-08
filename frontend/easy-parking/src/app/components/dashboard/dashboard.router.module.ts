import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardPage } from './dashboard.page';
import { IonicModule } from '@ionic/angular';

const routes: Routes = [
  {
    path: 'dashboard',
    component: DashboardPage,
    children: [
      {
        path: 'dashboard',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/admin/dashboard/dashboard.module').then( m => m.DashboardPageModule)
          }
        ]
      },
      {
        path: 'search',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/client/search/search.module').then( m => m.SearchPageModule)
          }
        ]
      },
      {
        path: 'vehicles',
        children: [
          {
            path: '',
            loadChildren: () => import('../../pages/client/vehicles/vehicles.module').then( m => m.VehiclesPageModule)
          }
        ]
      },
      {
        path: '',
        redirectTo: '/dashboard/dashboard',
        pathMatch: 'full'
      }
    ]
  },
  {
    path: '',
    redirectTo: '/dashboard/dashboard',
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
export class TabsPageRoutingModule {}
