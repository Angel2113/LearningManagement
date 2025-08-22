import axios from "axios";


const baseURL = "http://localhost:8000";

export async function login(username: string, password: string) {
    try {
        const response = await axios.post(`${baseURL}/auth/login`,
            {
                username: username,
                password: password,
            }, {
            headers: {
                'Content-Type': 'application/json',
            },
        });
        return response.data;

    } catch (error: any ) {
        throw new Error(error.response.data.detail);
    }
}

