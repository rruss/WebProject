import { Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { IAuthResponse, IQuestions, ITitle, IAnswer, IUser, IOkAnswer, IOkAnswers, IResult, IUserResults } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
   }

   getTitles(): Promise<ITitle[]>{
     return this.get('http://localhost:8000/api/title/', {});
   }

   getProfile(id:number): Promise<IUser> {
     return this.get(`http://127.0.0.1:8000/api/users/${id}/`,{});
   }

  //  getProfile(id: number)

   getTitle(id: number):Promise<ITitle> {
     return this.get(`http://localhost:8000/api/title/${id}/`,{});
   }
   getOkAnswer(id: number) :Promise<IOkAnswers> {
     return this.get(`http://localhost:8000/api/okanswer/${id}/`,{})
   }
   getUserResults(id:number):Promise<IUserResults> {
      return this.get(`http://127.0.0.1:8000/api/user/${id}/result/`,{});
   }

   auth(login: string, password: string): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: login,
      password: password
    });
  }
  createResult(test_name:any, test_result:any, user:any): Promise<IResult> {
    return this.post('http://localhost:8000/api/user_result/', {
      test_name:test_name,
      test_result:test_result,
      user: user
    });
  }
 
  updateProfile(user: IUser): Promise<IUser> {
    return this.put(`http://localhost:8000/api/users/update/${user.id}/`, {
      first_name: user.first_name,
      last_name: user.last_name,
      age: user.age,
      email: user.email
    });
  }

  register(username: string, first_name: string, last_name: string, password: string, age:number, email: string, is_superuser: boolean, ): Promise<IUser>{
    return this.post('http://localhost:8000/api/users/', {
      username: username,
      first_name: first_name,
      last_name: last_name,
      age: age,
      password: password,
      email: email,
      is_superuser: is_superuser
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {});
  }

}
