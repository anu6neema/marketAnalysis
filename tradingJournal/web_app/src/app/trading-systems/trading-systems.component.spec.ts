import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TradingSystemsComponent } from './trading-systems.component';

describe('TradingSystemsComponent', () => {
  let component: TradingSystemsComponent;
  let fixture: ComponentFixture<TradingSystemsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TradingSystemsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TradingSystemsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
