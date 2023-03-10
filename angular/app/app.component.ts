import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'leftovers';
  getHelloWorld(): Observable<any> {
    return this.http.get("/api")
  }
  constructor(private http: HttpClient) {
    this.getHelloWorld().subscribe(data => {
      this.title = data.message || this.title;
    })
  }
}
