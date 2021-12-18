import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import {RouterModule, Routes} from '@angular/router';
import { HeaderViewComponent } from './header-view/header-view.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {MatButtonModule} from '@angular/material/button';
import {MatDialogModule} from "@angular/material";
import {MatButtonToggleModule} from "@angular/material";
import { routes }  from './app-routing.module';
import { HomeViewComponent } from './home-view/home-view.component';
import { SearchViewComponent } from './search-view/search-view.component';
import { AlertViewComponent } from './alert-view/alert-view.component';
import { MessageViewComponent } from './message-view/message-view.component';
import { GlobalBmViewComponent } from './global-bm-view/global-bm-view.component';
import { PowerbiViewComponent } from './powerbi-view/powerbi-view.component';
import {PlantDataService} from './services/plant-data.service';
import {PythonDataService} from './services/python-data.service';
import { HttpClientModule } from '@angular/common/http';
import { ChartsModule } from 'ng2-charts/ng2-charts';
import { BarChartComponent } from './bar-chart/bar-chart.component';
/* import { MapsViewDirective } from './maps-view.directive'; */
import { TradingLogComponent } from './trading-log/trading-log.component';
import { BackTestComponent } from './back-test/back-test.component';
import { TradeWatchlistComponent } from './trade-watchlist/trade-watchlist.component';
import { RiskRewardChecklistComponent } from './risk-reward-checklist/risk-reward-checklist.component';
import { TradingSystemsComponent } from './trading-systems/trading-systems.component';
import { PaperTradingComponent } from './paper-trading/paper-trading.component'; 
import { FormsModule } from '@angular/forms';
import { TradeLogDialogComponent } from './trade-log-dialog/trade-log-dialog.component';
import { TradeDetailComponent } from './trade-log-dialog/trade-detail/trade-detail.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderViewComponent,BarChartComponent,
    HomeViewComponent,
    SearchViewComponent,
    AlertViewComponent,
    MessageViewComponent,
    GlobalBmViewComponent,
    PowerbiViewComponent,
    /* MapsViewDirective, */
    TradingLogComponent,
    BackTestComponent,
    TradeWatchlistComponent,
    RiskRewardChecklistComponent,
    TradingSystemsComponent,
    PaperTradingComponent,
    TradeLogDialogComponent,
    TradeDetailComponent
    
    ],
  imports: [
    BrowserModule,
    RouterModule,
    RouterModule.forRoot(routes, {useHash: true}),
    BrowserAnimationsModule,
    MatButtonModule,
    HttpClientModule,
    ChartsModule,
    FormsModule    ,
    MatDialogModule,MatButtonToggleModule
  ],
  entryComponents:[
    TradingLogComponent
  ],
  providers: [PlantDataService,PythonDataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
