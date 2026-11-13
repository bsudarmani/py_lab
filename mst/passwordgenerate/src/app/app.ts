
import { Component } from '@angular/core';

import {
  FormGroup,
  ReactiveFormsModule,
  FormBuilder,
  Validators
} from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [ReactiveFormsModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})

export class App {

  passForm: FormGroup;

  result: string = "";

  constructor(private fb: FormBuilder) {

    this.passForm = this.fb.group({

      password: ['', [
        Validators.required,
        Validators.minLength(4),
        Validators.maxLength(10)
      ]]

    });

  }

  handlesubmit() {

    if (this.passForm.valid) {

      const val = this.passForm.value.password as string;

      const special = ['$', '@'];

      this.result = "";

      for (let i = 0; i < val.length; i++) {

        this.result +=
          val.charAt(i) +
          special[Math.floor(Math.random() * special.length)];

      }

    }
    else {
      this.result = "Please enter 4 to 10 characters";
    }

  }

}
