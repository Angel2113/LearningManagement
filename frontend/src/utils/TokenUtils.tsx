import { jwtDecode } from "jwt-decode";

const getJWT = () => {
    return localStorage.getItem("token") ?? "";
}

const decodeJWT = (jwt: string) => {
    return jwtDecode(jwt);
}

const logout = () => {

    localStorage.removeItem("token");
    window.location.href = '/login';
}

const isTokenValid = () => {
    const jwt = getJWT();
    if(jwt) {
        return isTokenExpired(jwt);
    } else {
        console.log("token is expired");
        return false;
    }
}

const isTokenExpired = (jwt: any) => {
    const jwtDecoded:any = decodeJWT(jwt);
    const currentTime = Date.now() / 1000;
    return currentTime > jwtDecoded.expiration;
}

const TokenUtils = {
    getJWT,
    logout,
    decodeJWT,
    isTokenValid,
    isTokenExpired
}

export default TokenUtils;