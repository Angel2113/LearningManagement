import axios from "axios";


const baseURL = "http://localhost:8000";

export async function login(username: string, password: string) {

    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    try {
        const response = await axios.post(`${baseURL}/auth/login`,  params, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });
        return response.data;

    } catch (error: any ) {
        throw new Error(error.response.data.detail);
    }
}

