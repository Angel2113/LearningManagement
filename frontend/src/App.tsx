import LoginForm from "./features/auth/components/LoginForm";
import axios from "axios";
import React from "react";




function App() {
    const baseURL = "http://localhost:8000/all_users";

    type User = {

        id: string,
        email: string,
        username: string,
        role: string
    }
    const [post, setPost] = React.useState<User[]>([]);
    React.useEffect(() => {
        axios.get(baseURL).then((response) => {
          setPost(response.data);
        }).catch((error) => console.error("Error obteniendo los datos:", error));
    }, []);

    if(!post) return null;


    return <div className="container-fluid">
        <div className='row justify-content-center min-vh-100'>
            <div className='col-2'/>
            <div className='col-8'>
                <LoginForm />
            </div>
            <div className='col-2'/>
        </div>
    </div>
}

export default App;