import {Routes} from '@angular/router';
import { HeaderViewComponent } from './header-view/header-view.component';
import { HomeViewComponent } from './home-view/home-view.component';
import { SearchViewComponent } from './search-view/search-view.component';
import { AlertViewComponent } from './alert-view/alert-view.component';
import { MessageViewComponent } from './message-view/message-view.component';
import { GlobalBmViewComponent } from './global-bm-view/global-bm-view.component';
import { PowerbiViewComponent } from './powerbi-view/powerbi-view.component';
import { TradingLogComponent } from './trading-log/trading-log.component'; 
import { BackTestComponent } from './back-test/back-test.component'; 
import { TradeWatchlistComponent } from './trade-watchlist/trade-watchlist.component';
import { RiskRewardChecklistComponent } from './risk-reward-checklist/risk-reward-checklist.component';
import { TradingSystemsComponent } from './trading-systems/trading-systems.component'; 
import { PaperTradingComponent } from './paper-trading/paper-trading.component'; 
import {TradeLogDialogComponent} from './trade-log-dialog/trade-log-dialog.component';

export const routes: Routes = [
    { path: '', redirectTo: '/home', pathMatch: 'full' },
    { path: 'home',  component: HomeViewComponent },
     { path: 'search',  component: SearchViewComponent } ,
     { path: 'alert',  component: AlertViewComponent } , 
      { path: 'message',  component: MessageViewComponent } ,
      { path: 'gpbm',  component: GlobalBmViewComponent } ,
      { path: 'powerbi',  component: PowerbiViewComponent},
      { path: 'tradelog',  component: TradeLogDialogComponent},
      { path: 'backtest',  component: BackTestComponent},
      { path: 'watchlist',  component: TradeWatchlistComponent},
      { path: 'RRcheck',  component: RiskRewardChecklistComponent},
      { path: 'tradesystem',  component: TradingSystemsComponent},
      { path: 'papertrade',  component: PaperTradingComponent}
     ];