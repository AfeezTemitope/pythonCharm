import Todo from '../../asset/todo.png'
import React, {useState} from "react";
import RegistrationForm from "../../components/RegistrationForm";
import './style/body.css'
import {useNavigate} from "react-router-dom";
//import  Login from '../../pages/loginPage/LoginForm'


const Body = () => {
    const navigate = useNavigate();
    const [message, setMessage] = useState('')
    const handleRegistration = async (username, password) => {
        try {
            const response = await fetch('http://127.0.0.1:5000/register',{
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({username, password}),
            })
            setTimeout(()=> {
                    navigate("/login");
                },2000)
            const result = await response.json()
            if (response.ok){
                setMessage(`User ${username} now has a todo list`)

            // history.push('Login')
            } else { setMessage(result.message || 'Something went wrong') }
        }  catch(e) {
            setMessage('an error occur: ' + e.message)
        }
    }
    return(
        <div className="container">
            <div className="image-section"> <img src={Todo} alt="todo" /></div>
            <div><RegistrationForm onSubmit={handleRegistration} message={message} />
        </div>
            </div>
)
}

export default Body;