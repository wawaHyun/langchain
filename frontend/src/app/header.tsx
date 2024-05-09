'use client';

import Link from 'next/link';


function Header() {

  return (<nav className="bg-white border-gray-200 dark:bg-gray-900">
    <div className="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
      <Link href="/" className="flex items-center space-x-3 rtl:space-x-reverse">
        <img src="https://flowbite.com/docs/images/logo.svg" className="h-8" alt="Flowbite Logo" />
        <span className="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Flowbite</span>
      </Link>
        <span className="sr-only">Open user menu</span>
        <img className="w-8 h-8 rounded-full" src="/public/img/images.png" alt="user photo" />
 
   
        <div className="flex px-4 py-3 float-end">
          <span className="block text-sm text-gray-900 dark:text-white">vfff</span>
          <span className="block text-sm  text-gray-500 truncate dark:text-gray-400 mx-5" >마이페이지</span>
          <span className="block text-sm  text-gray-500 truncate dark:text-gray-400" ><a href='#'></a> Logout </span> 
        </div>

      <div className="items-center justify-between hidden w-full md:flex md:w-auto md:order-1" id="navbar-user">
        <ul className="flex flex-col font-medium p-4 md:p-0 mt-4 border border-gray-100 rounded-lg bg-gray-50 md:space-x-8 rtl:space-x-reverse md:flex-row md:mt-0 md:border-0 md:bg-white dark:bg-gray-800 md:dark:bg-gray-900 dark:border-gray-700">
      
        </ul>
      </div>
    </div>
  </nav>);
}
export default Header;