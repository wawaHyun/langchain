'use client'

import { stringify } from "querystring"
import { useState } from "react"
import { SubmitHandler, useForm } from "react-hook-form"

export default function pythonPage() {
    const [message, setMessage] = useState('')
    const [view, setView] = useState('무엇이든 물어보세요! ')
    const [category, setCategory] = useState('')
  
    type Inputs = {
      question: string
      category?: string
      exampleRequired?: string
    }
  
    const {
      register,
      handleSubmit,
      watch,
      formState: { errors },
    } = useForm<Inputs>()

    const onSubmit = (data:any) => {
      if (category == "") alert("카테고리 버튼을 눌러주세요")
  
      console.log("input qusetion: ", watch("question"))
  
      fetch('http://localhost:8000/api/sample/' + `${category}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data)
      })
        .then((response) => response.json())
        .then((data) => setMessage(data.answer))
        .catch((error) => console.log("error: ", error));
    }
  
    const handleRadio = (e: any) => {
      setCategory(e.target.value)
      switch (category){
        case "bmi":
            setView("bmi 랜덤 추출")
          break;
        case "leapyear":
            setView("leapyear 인지 아닌지 물어보세요")
          break;
        case "rps":
            setView("가위바위보!")
          break;
        default:
            setView("무엇이든 물어보세요")
          break;
      }
      setMessage("")
      console.log("select button : ", e.target.value)
    }


    function result (category:string) {
        switch (category){
            case "bmi":
                <div>bmi is :  {message}</div>
              break;
            case "leapyear":
                <div>leapyear is :  {message}</div>
              break;
            case "rps":
                <div>rps is :  {message}</div>
              break;
          }
        }

return (

<div>
<input type="radio" name="category" onClick={handleRadio} value="bmi" className="w-5 h-5"/> BMI <br />
<input type="radio" name="category" onClick={handleRadio} value="leapyear" className="w-5 h-5"/>윤년<br />
<input type="radio" name="category" onClick={handleRadio} value="rps" className="w-5 h-5"/>가위바위보!<br />
<input type="radio" name="category" onClick={handleRadio} value="rps" className="w-5 h-5"/>RPS!<br />
<input type="radio" name="category" onClick={handleRadio} value="rps" className="w-5 h-5"/>RPS!<br />

<form onSubmit={handleSubmit(onSubmit)} className="">
          <div className="self-stretch text-black text-[64px] font-bold font-['Inter']">{view}</div>
          <div className="flex justify-start min-h-full rounded-xl h-20 mb-3">
            <input className="p-5 w-[95%] rounded-xl border " onClick={() => {setMessage(""), setView("무엇이든 물어보세요")}} type="sumit" placeholder="      Message ChatGPT" {...register("question", { required: true })} />
          </div>
        </form >

<div className="text-xl h-[200px] p-5 text-[23px] rounded-xl  bg-gray-100 shadow-xl shadow-gray-500">
{!message ?  "result" :
  <p className="animate-bounce h-full opacity-50 text-[50px] content-center text-center ">Wait for input . . .</p>
}
</div>
</div>

)
}