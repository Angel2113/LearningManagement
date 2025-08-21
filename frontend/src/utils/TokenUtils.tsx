import { jwtDecode } from "jwt-decode";

const getJWT = () => {
    return localStorage.getItem("jwt") ?? "";
}

const decodeJWT = (jwt: any) => {
    return jwtDecode(jwt);
}

const logout = () => {
    localStorage.removeItem("jwt");
}

const isTokenValid = () => {
    const jwt = getJWT();
    if(jwt) {
        return isTokenExpired(jwt);
    } else {
        console.log("JWT is expired");
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
    isTokenValid,
    isTokenExpired
}

export default TokenUtils;