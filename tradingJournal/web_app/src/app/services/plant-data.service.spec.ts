import { TestBed, inject } from '@angular/core/testing';

import { PlantDataService } from './plant-data.service';

describe('PlantDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [PlantDataService]
    });
  });

  it('should be created', inject([PlantDataService], (service: PlantDataService) => {
    expect(service).toBeTruthy();
  }));
});
