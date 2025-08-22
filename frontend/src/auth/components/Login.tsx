import {useState} from "react";
import {login} from "../../services/auth";
import {useNavigate} from "react-router-dom";
import './Login.model.css';
import {useAuthStore} from "@/auth/store/auth.store.tsx";


export default function LoginPage() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();
    const { login } = useAuthStore()

    async function handleSubmit(e) {
        e.preventDefault();
        setError("");
        const isValid = await login(username, password)
        if( isValid ){
            navigate('/home');
        } else {
            setError("Invalid credentials");
        }
        /*
        try {
            //const data = await login(username, password);
            //localStorage.setItem("token", data.access_token);
            //login(username, password);
        } catch (err) {
            setError("Invalid credentials");
        }
        */

    }

    return (

        <main className="form-signin w-100 m-auto d-flex align-items-center justify-content-center vh-100 bg-light">

            <div className="container mt-5">
                <h2>Login</h2>
                <form onSubmit={handleSubmit}>
                    <div className="form-floating mb-3">

                        <input
                            className="form-control"
                            placeholder="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                        <label>Username</label>
                    </div>
                    <div className="form-floating mb-3">

                        <input
                            type="password"
                            className="form-control"
                            value={password}
                            placeholder="password"
                            onChange={(e) => setPassword(e.target.value)}
                        />
                        <label>Password</label>
                    </div>
                    {error && (
                        <div className="alert alert-danger" role="alert">
                            {error}
                        </div>)
                    }
                    <button className="btn btn-primary" type="submit">
                        Login
                    </button>
                </form>
            </div>
        </main>
    );
}
