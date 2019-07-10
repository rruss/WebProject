export interface ITitle{
    id:number;
    name:string;
    questions: IQuestions[];
}
export interface IQuestions{
    id:number;
    question:string;
    answers: IAnswer[];  
}
export interface IResult{
    id:number;
    test_name:string;
    test_result:number;
    user:number;
}
export interface IOkAnswer{
    id:number;
    ok_answer:string;
    quesId:number;
}
export interface IOkAnswers{
    id:number;
    okanswers:IOkAnswer[]
}

export interface IAnswer{
    id: number;
    answer: string;
}

export interface IAuthResponse {
    token: string;
    id: number;
}
export interface Iresults{
    id:number;
    test_name:string;
    test_result:number;
}

export interface IUserResults{
    id:number;
    results: Iresults[];
}



export interface IUser {
    id: number;
    username: string;
    first_name: string;
    last_name:string;
    age: number;
    password: string;
    email: string;
    is_superuser: boolean;
}
