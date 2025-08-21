import {useState} from "react";
import {login} from "../../services/auth";
import {useNavigate} from "react-router-dom";
import './Login.model.css';


export default function LoginPage() {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();

    async function handleSubmit(e) {
        e.preventDefault();
        setError("");
        try {
            const data = await login(username, password);
            localStorage.setItem("token", data.access_token);

            navigate('/home');
        } catch (err) {
            setError("Invalid credentials");
        }
    }

    return (
        <div className="container mt-5">
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div className="mb-3">
                    <label>Username</label>
                    <input
                        className="form-control"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                    />
                </div>

                <div className="mb-3">
                    <label>Password</label>
                    <input
                        type="password"
                        className="form-control"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                    />
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
    );
}
