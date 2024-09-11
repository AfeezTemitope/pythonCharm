import React, {useState} from "react";
//import {useHistory} from 'react-router-dom'
import '../../containers/home/style/body.css'
import LoginForm from "./LoginForm";

const Login = () => {
    const [message, setMessage] = useState('')
    //const history = useHistory()
    const handleLogin = async (username, password) => {
        try {
            const response = await fetch('http://127.0.0.1:5000/login',{
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({username, password}),
            })
            const result = await response.json()
            if (response.ok){
                setMessage(`User ${username} logged in successfully`)

            } else { setMessage(result.message || 'Something went wrong') }
        }  catch(e) {
            setMessage('an error occur: ' + e.message)
        }
    }
    return(
            <div className= "login_form">
                <LoginForm onSubmit={handleLogin} message={message} />
            </div>
)
}

export default Login;