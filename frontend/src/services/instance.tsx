import axios from "axios";
import TokenUtils from "@/utils/TokenUtils.tsx";

const instance = axios.create({
    baseURL: "http://localhost:8000",
    headers: {"Content-Type": "application/json"}
});

const isTokenExpired = (token: string) => {
    const token_data: any = TokenUtils.decodeJWT(token)
    const exp_date = token_data['expiration'];
    const current_date = new Date().toISOString();

    if(exp_date < current_date) {
        console.log('token is expired');
        TokenUtils.logout();
        return true;
    }
    return false;
}

instance.interceptors.request.use((config) => {
        console.log('intercepting ...');
        const token = TokenUtils.getJWT();

        if (token) {
            if(!isTokenExpired(token)){
                console.log('adding-header ...');
                config.headers.Authorization = "Bearer " + token;
            }
        } else {
            console.log('Token is invalid or not found');
        }
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
);

export default instance;