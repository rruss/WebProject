import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IQuestions, ITitle, IAnswer, IAuthResponse, IOkAnswer, IOkAnswers, IResult, IUser, IUserResults } from '../shared/models/models';
import { Title } from '@angular/platform-browser';
import { AlertPromise } from 'selenium-webdriver';
import { UrlSerializer } from '@angular/router';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.scss']
})
export class ParentComponent implements OnInit {

  public ok=false;
  public ok2=false;
  public ok3=false;
  public ok5=false;
  public ok6=false;
  public ok4=false;
  public test=false;
  public userId: number;
  public userResults: IUserResults;
  public questions: IQuestions[] = [];
  public question: IQuestions;
  public title: ITitle;
  public answers: IAnswer[] = [];
  public answer: IAnswer;
  public titles: ITitle[] =[];
  public id: number;
  public check: any;
  public radios: any;
  public questionNameCheckerId:any[]=[];


  public name: any = '';

  public isLogged = false;

  public login = '';
  public password = '';
  public password_repeat = '';
  public email = '';
  public age:any;
  public first_name='';
  public last_name='';
  public profile: IUser;
  public okAnswer: IOkAnswers;
  public is_superuser = false;
  public checkOkAnswer: any[]= [];
  public test_name: string;
  public test_result:number;
  public user: number;
  public test_degree: string;
  public results: IResult[]=[];

  constructor(private provider: ProviderService) { }

  ngOnInit() {

        const token = localStorage.getItem('token');
        const userId = localStorage.getItem('id');

    if (token) {
      this.isLogged = true;
      console.log('token');
      document.getElementById("section_window").style.display="none";
      document.getElementById("section_window1").style.display="none";

    }
   
  }

  getTitle(id:number){
    this.provider.getTitle(id).then(res => {
      this.title = res;
    })
  }

  getProfile(id:number){
    this.provider.getProfile(id).then(res => {
      this.profile = res;
      
    })
  }

  getOkAnswer(id:number){
    this.provider.getOkAnswer(id).then(res => {
      this.okAnswer=res;
    })
  }
  
  toEnter(id: number){
    if(!this.isLogged){
      alert('Өтінемін, бірінші тіркеліңіз!');
    }
    else{
      this.getTitle(id);
      this.getOkAnswer(id);
      this.id = id;
      this.test = true;
      document.getElementById("test").style.display="block";
      alert('Сіз кірдіңіз');
    }
}
toLogin(){
    document.getElementById("section_window").style.display="block";
    document.getElementById("section_window").style.opacity="toggle";
}

createResut(test_name:string, test_result:number, user:number) {
    this.provider.createResult(test_name, test_result, user).then(res => {
      this.results.push(res);
    });

  }

  getUserResults(){
  this.provider.getUserResults(this.userId).then(res =>{
    this.userResults=res;
  })
}
  
  toCheck(){
    this.questionNameCheckerId = this.title.questions;
    var cnt = 0;

    for (var i = 0, length = this.questionNameCheckerId.length; i < length; i++)
      { 

        this.check = this.questionNameCheckerId[i].id;
        this.radios = document.getElementsByName(this.check);
        this.checkOkAnswer = this.okAnswer.okanswers;
          for (var ind = 0; ind < this.radios.length; ind++)
          {
            if (this.radios[ind].checked)
              {
                if(this.radios[ind].value == this.checkOkAnswer[i].ok_answer){
                  cnt += 1;
                  
                  console.log('right');
                }
                else{
                  console.log('wrong')
                }
                break;
              }
          }
          console.log(this.checkOkAnswer[i].ok_answer);
      }

      this.createResut(this.title.name, cnt, this.userId);
      this.test_result=cnt;
      document.getElementById("section_result").style.display="block";
      document.getElementById("section_result").style.opacity="toggle";
      if(this.id == 1 || this.id == 2){
        if(cnt <= 20 && cnt >= 17){
          this.test_degree = "Жоғары";
        }
        else if(cnt == 16){
          this.test_degree="Ортадан жоғары";
        }
        else if(cnt <= 14 && cnt >=11){
          this.test_degree="Орта";
        }
        else if(cnt == 8 || cnt == 9){
          this.test_degree="Ортадан төмен";
        }
        else{
          this.test_degree="Төмен";
        }

      }

  }

toReg(){
  document.getElementById("window_reg").style.display="block";
  document.getElementById("window_reg").style.opacity="toggle";
  
}

toGoProfile(){
  this.getProfile(this.userId);
  this.getUserResults();
  document.getElementById("section_profile").style.display="block";
  document.getElementById("section_profile").style.opacity="toggle";
}


changeProfile(){

  this.provider.updateProfile(this.profile).then(res =>{
    console.log(this.profile.username + " updated");
  })
}

hideModal(){
  document.getElementById("section_window").style.display="none";
  document.getElementById("window_reg").style.display="none";
  document.getElementById("section_profile").style.display="none";
}
hideModalBack(){
  document.getElementById("section_result").style.display="none";
  document.getElementById("test").style.display="none";
}



  f1(){
    this.ok=!this.ok;
     this.ok2=false;
    this.ok3=false;
    this.ok5=false;
    this.ok6=false;
    this.ok4=false;
  }
  f2(){
    this.ok2=!this.ok2;
    this.ok=false;
    this.ok3=false;
    this.ok5=false;
    this.ok6=false;
    this.ok4=false;
  }
  
  f3(){
    this.ok3=!this.ok3;
    this.ok2=false;
    this.ok=false;
    this.ok5=false;
    this.ok6=false;
    this.ok4=false;
  }
  f4(){
    this.ok4=!this.ok4;
    this.ok2=false;
    this.ok3=false;
    this.ok5=false;
    this.ok6=false;
    this.ok=false;
  }
  f5(){
    this.ok5=!this.ok5;
    this.ok2=false;
    this.ok3=false;
    this.ok=false;
    this.ok6=false;
    this.ok4=false;
  }
  f6(){
    this.ok6=!this.ok6;
    this.ok2=false;
    this.ok3=false;
    this.ok5=false;
    this.ok=false;
    this.ok4=false;
  }

  auth() {
    if (this.login !== '' && this.password !== '') {
      this.provider.auth(this.login, this.password).then(res => {
        localStorage.setItem('token', res.token);
        localStorage.setItem('id', res.id.toString());
        this.isLogged = true;
        this.userId=res.id;
        document.getElementById("section_window").style.display="none";
        document.getElementById("toReg").style.display="none";
        document.getElementById("toLogin").style.display="none";
        document.getElementById("profile").style.display="block"
        document.getElementById("logout").style.display="block"
      });
    
    }

  }

  register(){
    if(this.login !== '' && this.password !== '' && this.email !== '' && this.is_superuser !== null && this.password===this.password_repeat){
      this.provider.register(this.login, this.first_name, this.last_name, this.password,this.age, this.email, this.is_superuser).then(res =>{
        alert("Тіркелгеніңізге рақмет!")
        document.getElementById("window_reg").style.display="none";
        this.auth();
       
      })
    } 
  }

  logout() {
    this.provider.logout().then(res => {
      this.isLogged = false;
      localStorage.clear();
      document.getElementById("toReg").style.display="block";
      document.getElementById("toLogin").style.display="block";
      document.getElementById("profile").style.display="none"
      document.getElementById("logout").style.display="none"
      
    });
  }

}
