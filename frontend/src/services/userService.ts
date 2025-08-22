// src/services/userService.ts
import api from "./api";
import { User } from "../types/User";
import instance from "@/services/instance.tsx";

// Get All Users
export const getAllUsers = async (): Promise<User[]> => {
    const response = await instance.get("/all_users");
    return response.data;
};

// Create a new user
export const createUser = async (user: User): Promise<User> => {
    const response = await api.post("/users", user);
    return response.data;
};

// Updata a user
export const updateUser = async (id: string, user: Partial<User>): Promise<User> => {
    const response = await api.put(`/users/${id}`, user);
    return response.data;
};

export const deleteUser = async (id: string): Promise<void> => {
    await api.delete(`/users/${id}`);
}