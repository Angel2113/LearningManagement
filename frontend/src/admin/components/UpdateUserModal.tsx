import React, { useState } from "react";
import { User } from "@/types/User";

interface UpdateUserModalProps {
    user: User | null;
    visible: boolean;
    onClose: () => void;
    onSave: (updatedUser: User) => void;
}

export const UpdateUserModal: React.FC<UpdateUserModalProps> = ({ user, visible, onClose, onSave }) => {
    const [editedUser, setEditedUser] = useState<User | null>(user);

    if (!visible || !user) return null;

    const handleSave = () => {
        if (editedUser) {
            onSave(editedUser);
        }
    };

    return (
        <div className="modal show d-block" tabIndex={-1} style={{ backgroundColor: "rgba(0,0,0,0.5)" }}>
            <div className="modal-dialog">
                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title">Update User</h5>
                        <button type="button" className="btn-close" aria-label="Close" onClick={onClose}></button>
                    </div>
                    <div className="modal-body">
                        <div className="mb-3">
                            <label htmlFor="username" className="form-label">Username</label>
                            <input
                                type="text"
                                id="username"
                                className="form-control"
                                value={editedUser?.username || ""}
                                onChange={(e) =>
                                    setEditedUser({ ...editedUser, username: e.target.value } as User)
                                }
                            />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="role" className="form-label">Role</label>
                            <select
                                id="role"
                                className="form-select"
                                value={editedUser?.role || ""}
                                onChange={(e) =>
                                    setEditedUser({ ...editedUser, role: e.target.value } as User)
                                }
                            >
                                <option value="user">User</option>
                                <option value="admin">Admin</option>
                            </select>
                        </div>
                    </div>
                    <div className="modal-footer">
                        <button className="btn btn-secondary" onClick={onClose}>Cancel</button>
                        <button className="btn btn-primary" onClick={handleSave}>Save Changes</button>
                    </div>
                </div>
            </div>
        </div>
    );
};