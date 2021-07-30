import React, { useEffect, useState } from 'react';
import axios from 'axios';

const BASE_URL = 'https://dummyapi.io/data/api';
const APP_ID = '{APP_ID}';

const SERVER_BASE = '';

export default function MainForm() {

    const [loading, setLoading] = useState(false);
    const [data, setData] = useState(""); 
    const [result,setResult] = useState("....");

    function handleChange(e){
        setData(e.target.value);
    }

    function submitHandler(e){
        e.preventDefault();      
        console.log("SUBMIT",data)
        axios.get(SERVER_BASE+'/solve',{params:{data:data},headers:{'Access-Control-Allow-Origin':'*'}}).then(res => {
          console.log(res.data)  
          setData("");
          setResult(res.data.data);
        })
    }

    return (
        <div>

            {/* <div>
            {loading && "Loading..."}
            {JSON.stringify(data)}
            </div> */}
            <form onSubmit={submitHandler}>
                x≡
                <input id="data" name="data" value={data} placeholder="b1modn1,b2modn2,..." type="text" onChange={handleChange}/>
                {/* <input type="submit" value="submit"/> */}
            </form>
            <h3>x = {result} </h3>

        </div>
    )
}
