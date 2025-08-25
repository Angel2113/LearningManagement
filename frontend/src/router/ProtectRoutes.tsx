import {Outlet, Navigate } from "react-router-dom";
import {useAuthStore} from "@/auth/store/auth.store.tsx";


export default function ProtectRoutes() {
    const { token } = useAuthStore();


    if(!token) {
        console.log('Dude you need to login');
        return <Navigate to="/login" replace />;
    } else {
        console.log('Dude you are logged in');
        return <Navigate to="/home" replace />;
    }

    return <Outlet />;
}