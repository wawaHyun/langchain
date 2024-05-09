'use client'

import { SubmitHandler, useForm } from "react-hook-form";
// import AutorenewIcon from '@mui/icons-material/Autorenew';

export default function Home() {


  type Inputs = {
    question: string
    exampleRequired?: string
  }

  const {
    register,
    handleSubmit,
    watch,
    formState: { errors },
  } = useForm<Inputs>()
  const onSubmit: SubmitHandler<Inputs> = (data) => {
    console.log("input qusetion: ", watch("question")) // watch input value by passing the name of it
    fetch('http://localhost:8080/chat')
      .then((response) => console.log("response: ", response))
      .catch((error) => console.log("error: ", error));
  }


  return (
    <body className="">

      <h2 className="text-3xl font-bold mb-6">Chat GPT</h2>

      <div className="bg-gray-100 min-h-full rounded-t-lg mx-8 shadow-xl shadow-gray-500">
        <div className="overflow-y-auto text-xl">
          {/* 여기에 채팅 메시지를 표시하는 컴포넌트를 추가하세요 */}
          ddd
          dddccccccccccccccccc
          animate-spin
          {/* <AutorenewIcon /> */}
        </div>

        <div className="w-[97%] h-20 absolute bottom-[5%]">
          <form onSubmit={handleSubmit(onSubmit)} className="inline-flex rounded-xl w-full h-full">
            <input className="w-[95%] rounded-xl" type="text" placeholder="      Message ChatGPT"
              {...register("question", { required: true })} />
            <button className="bg-gray-100 rounded-xl w-[5%] border" type="submit">input!</button>
          </form>
        </div>

      </div>
    </body>
  );
}
