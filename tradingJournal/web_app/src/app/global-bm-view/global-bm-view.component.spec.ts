import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GlobalBmViewComponent } from './global-bm-view.component';

describe('GlobalBmViewComponent', () => {
  let component: GlobalBmViewComponent;
  let fixture: ComponentFixture<GlobalBmViewComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GlobalBmViewComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GlobalBmViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
