import React, {useState} from "react";
import InputField from "../../components/InputField";

const LoginForm = ({onSubmit, message}) => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (e) => { e.preventDefault(); onSubmit(username, password); };
    return(
        <div className= "form-section">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <InputField
                    id="username"
                    label="Username"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required/>
                <InputField
                    id="password"
                    label="Password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Login</button>
            </form>
             {message && <p>{message}</p>}
        </div>
    )
}

export default LoginForm;