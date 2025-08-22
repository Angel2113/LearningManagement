import {Outlet, Navigate } from "react-router-dom";


export default function ProtectRoutes() {
    const token = localStorage.getItem('token');


    if(!token) {
        console.log('not logged in');
        return <Navigate to="/login" replace />;
    }
    return <Outlet />;
}