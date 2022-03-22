import axios from 'axios';
import { useEffect, useState } from "react";

const [data,setDate] = useState([])

useEffect(() => {
axios.get("https://jsonplaceholder.typicode.com/users")
.then(res => {
    console.log(res.data)
    setDate(res.data)
    return res.data
})
.catch(err => console.log(err))
},[])