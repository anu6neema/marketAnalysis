import { Injectable } from '@angular/core';
import 'rxjs/add/operator/map';
import { HttpClient } from '@angular/common/http'; 
import { HttpModule } from '@angular/http';

@Injectable()
export class PlantDataService {

 constructor(private _http:HttpClient) {}

 getDataObservable(url:string) {
  return this._http.get(url)
  .map(data => {    
      return data;
   
  }); 
}

}
