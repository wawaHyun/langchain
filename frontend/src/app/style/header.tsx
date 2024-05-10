'use client';

import Link from 'next/link';
import movebutton from '../atoms/button/movebutton';


function Header() {


const menus =[
  {id:0, title:'1번메뉴', patch:'링크'},
  {id:1, title:'2번메뉴', patch:'링크'},
  {id:2, title:'3번메뉴', patch:'링크'},
  {id:3, title:'4번메뉴', patch:'링크'},
]

  return (
<div className="TabList w-[255px] h-14 p-2 bg-neutral-100 rounded-xl justify-start items-start gap-2 inline-flex">
  <div>
  </div>
</div>
  )   
}
export default Header;