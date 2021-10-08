import { NgModule } from '@angular/core';
import { RouteReuseStrategy, RouterModule } from '@angular/router';
import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { MenuComponent } from './components/menu/menu.component';
import { ToolbarComponent } from './components/toolbar/toolbar.component';

@NgModule({
  declarations: [ MenuComponent, ToolbarComponent,],
  entryComponents: [ MenuComponent,],
  providers: [{ provide: RouteReuseStrategy, useClass: IonicRouteStrategy }],
  imports: [ReactiveFormsModule, RouterModule, FormsModule, IonicModule.forRoot() , HttpClientModule],
  exports: [MenuComponent, ToolbarComponent,],
})
export class ComponentsModule {}
