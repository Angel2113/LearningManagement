import {Route, Routes} from "react-router-dom";
import {AdminHomePage} from "../admin/components/AdminHomePage";
import LoginPage from "../auth/components/Login";
import ProtectRoutes from "@/router/ProtectRoutes.tsx";

export const AppRouter = () => {

    return (
        <>
            <Routes>
                {/* Public */}
                <Route path='/' element={<LoginPage />} />
                <Route path='/login' element={<LoginPage />} />
                {/* Protected Routes*/}
                <Route element={<ProtectRoutes />}>
                    <Route path="/home" element={<AdminHomePage />} />
                </Route>
            </Routes>
        </>
    )

}