// src/services/userService.ts
import { User } from "../types/User";
import instance from "@/services/instance.tsx";
import {AddUser} from "@/types/AddUser.ts";
import axios from "axios";

// Get All Users
export const getAllUsers = async (): Promise<User[]> => {
    const response = await instance.get("/users");
    return response.data;
};

// Create a new user
export const createUser = async (user: AddUser): Promise<number> => {
    const response = await instance.post("/users", user);
    return response.status;
};

// Update a user
export const updateUser = async (id: string, user: Partial<User>): Promise<User> => {
    const response = await instance.put(`/users/${id}`, user);
    return response.data;
};

export const deleteUser = async (id: string): Promise<number> => {
    const response = await instance.delete(`/users/${id}`);
    return response.status;
}

export const registerUser = async(user: AddUser): Promise<number> => {

        try {
            const response = await axios.post("http://localhost:8000/register",
                {
                    username: user.username,
                    email: user.email,
                    password: user.password,
                    password_confirmation: user.password_confirmation,
                    role: user.role,
                },
                {
                    headers: {
                        'Content-Type': 'application/json',
                    },
                });
            console.log(response.status);
            return response.status;
        } catch (error: any) {
            throw new Error(error.response.data.detail);
        }
}