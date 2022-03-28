import axios from 'axios';
import { useEffect, useState } from "react";

function Items() {
    
    const [items,setItem] = useState([])

    useEffect(() => {
        axios.get("http://127.0.0.1:9090/items")
        .then(res => {
        console.log(res.data)
        setItem(res.data)
        })
        .catch(err => console.log(err))
    },[])

    return (
        {items}
    );
}

export default Items;
