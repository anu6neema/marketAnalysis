import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TradeLogDialogComponent } from './trade-log-dialog.component';

describe('TradeLogDialogComponent', () => {
  let component: TradeLogDialogComponent;
  let fixture: ComponentFixture<TradeLogDialogComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TradeLogDialogComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TradeLogDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
