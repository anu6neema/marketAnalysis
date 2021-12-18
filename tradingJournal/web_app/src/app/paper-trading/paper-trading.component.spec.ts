import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PaperTradingComponent } from './paper-trading.component';

describe('PaperTradingComponent', () => {
  let component: PaperTradingComponent;
  let fixture: ComponentFixture<PaperTradingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PaperTradingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PaperTradingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
