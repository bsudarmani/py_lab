import { Component, signal } from '@angular/core';
// import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  // protected readonly title = signal('table');
  // // num:string=""
  // table:string[]=[]
  // cal(val:string):void {
  //   const num=Number(val)
  //   this.table=[]
  //   for(let i=1;i<=10;i++)
  //   {
  //     this.table.push(`${i}*${num}=${i*num}`)
  //   }
  // }

  //one-way-binding
  //  arr:boolean[]=[false,false,false]
  // click(e:Event,n:number):void
  // {
  //   const ref=e.target as HTMLInputElement
  //   this.arr[n]=ref.checked
  // }
}
