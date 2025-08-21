import {Route, Routes} from "react-router-dom";
import {AdminHomePage} from "../admin/components/AdminHomePage";
import LoginPage from "../auth/components/Login";

export const AppRouter = () => {

    return (
        <>
            <Routes>
                <Route path='/' element={<LoginPage />} />
                <Route path='/home' element={<AdminHomePage />} />
            </Routes>
        </>
    )

}