import {Navigate, Route, Routes} from "react-router-dom";
import {AdminHomePage} from "@/admin/components/AdminHomePage";
import {UserHomePage} from "@/user/components/UserHomePage";
import LoginPage from "@/auth/components/Login";
import ProtectRoutes from "@/router/ProtectRoutes.tsx";
import {useAuthStore} from "@/auth/store/auth.store.tsx";

export const AppRouter = () => {
    const {role} = useAuthStore();
    return (
        <>
            <Routes>
                {/* Public */}
                <Route path='/' element={<LoginPage/>}/>
                <Route path='/login' element={<LoginPage/>}/>
                {/* Protected Routes*/}
                <Route
                    path="/home"
                    element={
                        role === "admin" ? <AdminHomePage/> :
                            role === "user" ? <UserHomePage/> :
                                <Navigate to="/login" replace/>
                    }
                />

            </Routes>
        </>
    )
}