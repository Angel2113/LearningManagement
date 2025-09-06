import {useState} from "react";
import {AddUser} from "@/types/AddUser.ts";
import {registerUser} from "@/services/userService.ts";
import {useNavigate} from "react-router-dom";


export const RegisterPage = () => {
    const [user, setUser] = useState<AddUser>({
        username: "",
        email: "",
        role: "user",
        password: "",
        password_confirmation: ""
    });
    const navigate = useNavigate();

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();
        if (!user?.username || user.username.length < 5) {
           alert('User length must be at least 5 characters long');
           return;
       }

       if (!user.email || user.email.length < 5) {
           alert('Email has not the correct format');
           return;
       }

       if (!user.password || user.password.length < 8) {
           alert('Password must be at least 8 characters long');
           return;
       }

       if (user.password !== user.password_confirmation) {
           alert('The passwords do not match');
           return;
       }


        if(user){
            try {
                const response = await registerUser(user);
                if (response === 200) {
                    navigate('/login');
                }
            } catch (error) {
                console.error('Error adding user:', error.message);
                throw new Error('Error adding user');
            }
        }
    }
    return (
        <>
            <form onSubmit={handleSubmit}>
                <div className="modal show d-block" style={{ background: "rgba(0,0,0,0.5)" }}>
                    <div className="modal-dialog">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title">Add User</h5>
                            </div>
                            <div className="modal-body">
                                <div className="mb-3">
                                    <label htmlFor="username" className="form-label">
                                        Username
                                    </label>
                                    <input
                                        type="text"
                                        id="username"
                                        className="form-control"
                                        value={user?.username || ""}
                                        onChange={(e)=>{
                                            setUser({
                                                ...user,
                                                username: e.target.value,
                                            } as AddUser)
                                        }}
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="email" className="form-label">
                                        Email
                                    </label>
                                    <input
                                        type="email"
                                        id="email"
                                        className="form-control"
                                        value={user?.email || ""}
                                        onChange={(e)=>{
                                            setUser({
                                                ...user,
                                                email: e.target.value,
                                            } as AddUser)
                                        }}
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="role" className="form-label">
                                        Role
                                    </label>
                                    <select
                                        id="role"
                                        className="form-select"
                                        value={user?.role || ""}
                                        onChange={(e) => {
                                            setUser({
                                                ...user,
                                                role: e.target.value,
                                            } as AddUser)
                                        }}
                                    >
                                        <option value="user">User</option>
                                    </select>
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="role" className="form-label">
                                        Password
                                    </label>
                                    <input
                                        type="password"
                                        id="password"
                                        title="Password"
                                        className="form-control"
                                        value={user?.password || ""}
                                        onChange={(e)=>{
                                            setUser({
                                                ...user,
                                                password: e.target.value,
                                            } as AddUser)
                                        }}
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="role" className="form-label">
                                        Confirmation Password
                                    </label>
                                    <input
                                        type="password"
                                        id="confirm_password"
                                        title="confirm_password"
                                        className="form-control"
                                        value={user?.password_confirmation || ""}
                                        onChange={(e)=>{
                                            setUser({
                                                ...user,
                                                password_confirmation: e.target.value,
                                            } as AddUser)
                                        }}
                                    />
                                </div>
                            </div>
                            <div className="modal-footer">
                                <button className="btn btn-primary" type="submit">
                                    Save
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </form>
        </>
    )

}