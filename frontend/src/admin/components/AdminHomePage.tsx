import AdminNavBar from "@/admin/components/AdminNavBar.tsx";
import {deleteUser, getAllUsers, updateUser} from "@/services/userService.ts";
import {useEffect, useState} from "react";
import {User} from "@/types/User";
import {LucideUser} from "lucide-react";
import {useAuthStore} from "@/auth/store/auth.store.tsx";

export const AdminHomePage = () => {
    const [users, setUsers] = useState<User[]>([]);
    const [selectedUser, setSelectedUser] = useState<User | null>(null);
    const [editedUser, setEditedUser] = useState<User | null>(null);
    const [showUpdateModal, setShowUpdateModal] = useState(false);
    const [showDeleteModal, setShowDeleteModal] = useState(false);

    useEffect(() => {
        async function fetchUsers() {
            try {
                const response = await getAllUsers();
                setUsers(response);
            } catch (err) {
                throw new Error('Error fetching users');
            }
        }

        fetchUsers();
    }, []);

    const handleUpdateUser = (username: string) => {
        console.log(`Updating user: ${username}`);
        if(editedUser){
            try {
                updateUser(editedUser.id, editedUser);
                setUsers(users.map((u) => (u.id === editedUser.id ? editedUser : u)));
                setShowUpdateModal(false);
            }catch (error) {
                throw new Error('Error updating user');
            }
        }
    };


    const handleDeleteUser = (username: string) => {
        console.log(`Dude, are you trying to delete the user: ${username} ?`);
        if(selectedUser){
            try {
                console.log(`Deleting user: ${selectedUser.username}`);
                deleteUser(selectedUser.id);
                setUsers(users.filter((u) => u.id !== selectedUser.id));
                setShowDeleteModal(false);
            } catch (err) {
                throw new Error('Error deleting user');
            }
        };
    };


    return (
        <>
            <AdminNavBar/>
            <div className="container mt-5">
                <h1 className="mb-4 text-center text-white  rounded p-3 shadow">
                    Admin Dashboard
                </h1>

                <div className="card shadow-lg border-light">
                    <div
                        className="card-header bg-primary text-white d-flex justify-content-between align-items-center">
                        <h4 className="mb-0">User List</h4>
                        <button className="btn btn-sm btn-success">Add User</button>
                    </div>
                    <ul className="list-group list-group-flush">
                        {users.map((u) => (
                            <li
                                key={u.username}
                                className="list-group-item d-flex justify-content-between align-items-center"
                                style={{
                                    padding: "1rem",
                                    transition: "transform 0.2s ease-in-out",
                                }}
                                onMouseEnter={(e) =>
                                    (e.currentTarget.style.transform = "scale(1.01)")
                                }
                                onMouseLeave={(e) =>
                                    (e.currentTarget.style.transform = "scale(1)")
                                }
                            >
                                <div className="d-flex align-items-center">
                                    <div
                                        className="avatar rounded-circle bg-light text-center d-flex align-items-center justify-content-center me-3"
                                        style={{
                                            width: "50px",
                                            height: "50px",
                                            fontSize: "1.5rem",
                                        }}
                                    >
                                        <LucideUser className="text-primary"/>
                                    </div>
                                    <div>
                                        <strong className="text-dark">{u.email}</strong>
                                        <div className="text-muted">
                                            Role: <strong>{u.role}</strong>
                                        </div>
                                    </div>
                                </div>
                                <div className="action-buttons d-flex gap-2">
                                    <button
                                        className="btn btn-sm btn-outline-primary"
                                        onClick={() => {
                                            setEditedUser(u);
                                            setShowUpdateModal(true);
                                        }}
                                        title="Update User"
                                    >
                                        <i className="fas fa-pencil-alt"></i>
                                    </button>
                                    <button
                                        className="btn btn-sm btn-outline-danger"
                                        onClick={() => {
                                            setSelectedUser(u);
                                            setShowDeleteModal(true);
                                        }}
                                        title="Delete User"
                                    >
                                        <i className="fas fa-trash"></i>
                                    </button>
                                </div>
                            </li>
                        ))}
                    </ul>
                </div>

                {/* Delete Modal */}
                {
                    showDeleteModal && (
                        <div className="modal show d-block" style={{ background: "rgba(0,0,0,0.5)" }}>
                            <div className="modal-dialog">
                                <div className="modal-content">
                                    <div className="modal-header">
                                        <h5 className="modal-title">Confirm Deletion</h5>
                                        <button className="btn-close" onClick={() => setShowDeleteModal(false)}></button>
                                    </div>
                                    <div className="modal-body">
                                        <p>
                                            Are you sure you want to delete user <strong>{selectedUser?.username}</strong>?
                                        </p>
                                    </div>
                                    <div className="modal-footer">
                                        <button
                                            className="btn btn-secondary"
                                            onClick={() => setShowDeleteModal(false)}
                                        >
                                            Cancel
                                        </button>
                                        <button className="btn btn-danger" onClick={handleDeleteUser}>
                                            Delete
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )
                }

                {/* Update Modal */}
                {showUpdateModal && (
                    <div className="modal show d-block" style={{ background: "rgba(0,0,0,0.5)" }}>
                        <div className="modal-dialog">
                            <div className="modal-content">
                                <div className="modal-header">
                                    <h5 className="modal-title">Update User</h5>
                                    <button
                                        className="btn-close"
                                        onClick={() => setShowUpdateModal(false)}
                                    ></button>
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
                                            value={editedUser?.username || ""}
                                            onChange={(e) =>
                                                setEditedUser({
                                                    ...editedUser,  // Copy properties from editedUser in a new user
                                                    username: e.target.value,
                                                } as User)
                                            }
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="email" className="form-label">
                                            Username
                                        </label>
                                        <input
                                            type="text"
                                            id="email"
                                            className="form-control"
                                            value={editedUser?.email || ""}
                                            onChange={(e) =>
                                                setEditedUser({
                                                    ...editedUser,  // Copy properties from editedUser in a new user
                                                    email: e.target.value,
                                                } as User)
                                            }
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label htmlFor="role" className="form-label">
                                            Role
                                        </label>
                                        <select
                                            id="role"
                                            className="form-select"
                                            value={editedUser?.role || ""}
                                            onChange={(e) =>
                                                setEditedUser({
                                                    ...editedUser,
                                                    role: e.target.value,
                                                } as User)
                                            }
                                        >
                                            <option value="user">User</option>
                                            <option value="admin">Admin</option>
                                        </select>
                                    </div>
                                </div>
                                <div className="modal-footer">
                                    <button
                                        className="btn btn-secondary"
                                        onClick={() => setShowUpdateModal(false)}
                                    >
                                        Cancel
                                    </button>
                                    <button className="btn btn-primary" onClick={handleUpdateUser}>
                                        Save Changes
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </>
    );
};