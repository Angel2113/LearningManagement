import AdminNavBar from "@/admin/components/AdminNavBar.tsx";
import {getAllUsers} from "@/services/userService.ts";
import {useEffect, useState} from "react";
import {User} from "@/types/User";

export const AdminHomePage = () => {
    const [users, setUsers] = useState<User[]>([]);


    useEffect(() => {
        async function fetchUsers() {
            try {
                const response = await getAllUsers();
                setUsers(response);
            } catch (err) {
                throw new Error('Error fetching users');
            }
        }

        fetchUsers()
    }, []);

    return (
        <>
            <AdminNavBar/>
            <div className="container mt-4">
                <h1 className="mb-4">Admin Home Page</h1>

                <div className="card shadow-sm">
                    <div className="card-header bg-primary text-white">
                        User List
                    </div>
                    <ul className="list-group list-group-flush">
                        {users.map((u) => (
                            <li key={u.username}
                                className="list-group-item d-flex justify-content-between align-items-center">
                                <div>
                                    <strong>{u.email}</strong>
                                    <div className="text-muted">Role: {u.role}</div>
                                </div>
                                <span className={`badge ${u.role === "admin" ? "bg-danger" : "bg-secondary"}`}>
                  {u.role}
                </span>
                            </li>
                        ))}
                    </ul>
                </div>
            </div>

        </>
    );
}