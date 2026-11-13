import { HttpClient} from '@angular/common/http';
import { Component, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('front');
  username=''
  password=''
  message=''
  constructor(private http:HttpClient){}
  
login() {
  this.http.post(
    'http://localhost:3000/login',
    {
      username: this.username,
      password: this.password
    },
    {
      responseType: 'text'
    }
  ).subscribe({
    next: (result) => {
      console.log("Server Response:", result);
      this.message = result;
    },

    error: (err) => {
      console.log("Error Response:", err);
      this.message = err.error || "Something went wrong";
    }
  });
}

}
