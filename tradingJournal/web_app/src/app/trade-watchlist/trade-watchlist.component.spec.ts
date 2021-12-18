import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TradeWatchlistComponent } from './trade-watchlist.component';

describe('TradeWatchlistComponent', () => {
  let component: TradeWatchlistComponent;
  let fixture: ComponentFixture<TradeWatchlistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TradeWatchlistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TradeWatchlistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
