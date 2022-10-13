
// Note: please restart the page if syntax highlighting works bad.
let el = document.querySelector('#header')

let msg: string = 'Hi friend, try edit me!'
el.innerHTML = msg
const fDay=(day:string)=>{
  let y = Number(day.slice(0,4))
  let m = Number(day.slice(-2)) - 1
  let m2 = Number(day.slice(-2)) 
  
  let f = new Date(y, m, 1)
  
  console.log(f)
  if(m2 == 12){
    m2 = 0
    y += 1
  }
  let l = new Date(y, m2, 0)
  console.log(l)
  console.log(new Date(2022,0,31))
  //2022/12
}

console.log(fDay('202201'))
