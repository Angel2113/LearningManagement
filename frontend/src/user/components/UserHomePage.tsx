import {AddUser} from "@/types/AddUser.ts";
import {useEffect, useState} from "react";
import {getAllGoals} from "@/services/goalsService..tsx";

export const UserHomePage = () => {

    const [goals, setGoals] = useState<Goal[]>([]);

    const fetchGoals = async () => {
        try {
            const response = await getAllGoals();
            setGoals(response);
        } catch (error ){
            throw new Error('Error fetching goals');
        }

    }

    useEffect(() => {
        fetchGoals()
    }, []);

    return (
        <>
            <div className="container mt-5">
                    <h1 className="mb-4 text-center text-white  rounded p-3 shadow">
                        Admin Dashboard
                    </h1>
            </div>
            <div className="card shadow-lg border-light">
                        <div
                            className="card-header bg-primary text-white d-flex justify-content-between align-items-center">
                            <h4 className="mb-0">My Goals</h4>
                            <button
                                className="btn btn-sm btn-success"
                                onClick={() =>{
                                    setAddUser({
                                        username: "",
                                        email: "",
                                        role: "user",
                                        password: "",
                                        password_confirmation: ""
                                    } as AddUser)
                                    setShowAddModal(true)
                                }}
                                title="Add User"
                            >Add Goal</button>
                        </div>
            </div>
        </>
    );
}