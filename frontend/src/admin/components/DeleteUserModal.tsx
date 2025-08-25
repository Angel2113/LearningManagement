export const DeleteUserModal = () => {
    return (
        <div className="modal show d-block" style={{background: "rgba(0,0,0,0.5)"}}>
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