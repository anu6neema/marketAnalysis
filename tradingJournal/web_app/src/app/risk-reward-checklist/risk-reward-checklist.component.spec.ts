import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RiskRewardChecklistComponent } from './risk-reward-checklist.component';

describe('RiskRewardChecklistComponent', () => {
  let component: RiskRewardChecklistComponent;
  let fixture: ComponentFixture<RiskRewardChecklistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RiskRewardChecklistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RiskRewardChecklistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
