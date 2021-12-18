import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TradingLogComponent } from './trading-log.component';

describe('TradingLogComponent', () => {
  let component: TradingLogComponent;
  let fixture: ComponentFixture<TradingLogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TradingLogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TradingLogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
