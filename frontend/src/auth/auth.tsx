import axios from "axios";

const baseURL = "http://localhost:8000/auth/login";

export async function login(username:string, password:string) {
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);

    const response = await axios.post(baseURL, params, {
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },

    });
    return response.data;
}