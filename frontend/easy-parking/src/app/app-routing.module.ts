import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';
import { AuthorizedGuard } from './core/guards/authorized.guard';

const routes: Routes = [
  {
    path: 'welcome',
    loadChildren: () => import('./pages/welcome/welcome.module').then( m => m.WelcomePageModule),
    canActivate: [AuthorizedGuard],
    data: {
      access: []
    }
  },
  {
    path: '',
    redirectTo: 'welcome',
    pathMatch: 'full'
  },
  {
    path: '',
    loadChildren: ()  => import('./components/tabs/tabs.module').then( m=> m.TabsPageModule),
    canActivate: [AuthorizedGuard],
    data: {
      access: ['client']
    }
  },
  {
    path: '',
    loadChildren: ()  => import('./components/dashboard/dashboard.module').then( m=> m.DashboardPageModule),
    canActivate: [AuthorizedGuard],
    data: {
      access: ['admin']
    }
  },
/*   {
    path: 'home',
    loadChildren: () => import('./pages/home/home.module').then( m => m.HomePageModule)
  }, */
  {
    path: 'login',
    loadChildren: () => import('./pages/auth/login/login.module').then( m => m.LoginPageModule)
  },
  {
    path: 'register',
    loadChildren: () => import('./pages/auth/register/register.module').then( m => m.RegisterPageModule)
  },
  {
    path: 'register-parking',
    loadChildren: () => import('./pages/auth/register-parking/register-parking.module').then( m => m.RegisterParkingPageModule)
  },
  {
    path: 'history-reservations',
    loadChildren: () => import('./pages/client/history-reservations/history-reservations.module').then( m => m.HistoryReservationsPageModule)
  },
  {
    path: 'detail-parking/:slug_name',
    loadChildren: () => import('./pages/client/detail-parking/detail-parking.module').then( m => m.DetailParkingPageModule),
    canActivate: [AuthorizedGuard],
    data: {
      access: ['client']
    }
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
