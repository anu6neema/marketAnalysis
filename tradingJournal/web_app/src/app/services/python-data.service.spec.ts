import { TestBed, inject } from '@angular/core/testing';

import { PythonDataService } from './python-data.service';

describe('PythonDataService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [PythonDataService]
    });
  });

  it('should be created', inject([PythonDataService], (service: PythonDataService) => {
    expect(service).toBeTruthy();
  }));
});
