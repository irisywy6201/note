import {InputText} from 'primereact/inputtext'
import { Button } from 'primereact/button'
import { Toast } from 'primereact/toast'
import 'primereact/resources/themes/arya-blue/theme.css'
import 'primereact/resources/primereact.min.css'
import 'primeicons/primeicons.css'
import { useRef, useState } from 'react'
import styles from './SearchFilter.module.css';
import { MdExpandMore } from 'react-icons/md';

interface Articles {
    id: number,
    title: string
}
interface ArticlesProps{
  articles: Articles[]
}


export default function Test({articles}:ArticlesProps) {
    const [text, setText] = useState('')
    var toastRef = useRef<any>()

    const cehck = () =>{
        if (text)
            toastRef.current.show({severity: 'success', summary: 'Success Message ' , detail: text})
        else
            toastRef.current.show({severity: 'warn', summary: 'Warn Message', detail: 'There are unsaved changes'})

    }
   
    const active = 'price' as string;
    console.log(active)
    const [openDropdown, setOpenDropdown] = useState(false);
    const [selected, setSelected] = useState(!active ? null : getActive(active));
    const handleDropdown = (val: string) => {
      setOpenDropdown(false);
      setSelected(getActive(val));
    };
    function getActive(active: string) {
      return active === 'price' ? 'Price:  Low to High' : 'Price:  High to Low';
    }
    return (
      <>
      <div>
        <Toast ref={toastRef} />
            <InputText value={text} onChange={e => setText(e.target.value)} />
            <p>{text}</p>
            <Button label="Click" icon="pi pi-check" onClick={cehck}/>
      </div>
      {articles.map((a) => (
        <p  key={a.id} >{a.title}</p>
      ))}
      {articles[0]['id']}
      <div className={styles.filterContainer}>
      <span className={styles.label}> Sort by </span>
      <div className={styles.select}>
        <button
          className={styles.selectItem}
          onClick={() => setOpenDropdown(!openDropdown)}
          type="button"
        >
          <span>{!selected ? 'Price' : selected}</span>
          <span>
            <MdExpandMore size={24} />
          </span>
        </button>
        {openDropdown && (
          <div className={styles.dropdown}>
            <button className={styles.item} type="button" onClick={() => handleDropdown('price')}>
              Low to High
            </button>
            <button className={styles.item} type="button" onClick={() => handleDropdown('-price')}>
              High to Low
            </button>
          </div>
        )}
      </div>
    </div>
      </>
      
    )
  }

  export const getStaticProps = async () => {
    const res = await fetch(`https://jsonplaceholder.typicode.com/posts?_limit=6`)
    const articles = await res.json()

    return{
      props:{
        articles
      }
        
    }
  }