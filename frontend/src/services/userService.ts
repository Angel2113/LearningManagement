// src/services/userService.ts
import { User } from "../types/User";
import instance from "@/services/instance.tsx";
import {AddUser} from "@/types/AddUser.ts";

// Get All Users
export const getAllUsers = async (): Promise<User[]> => {
    const response = await instance.get("/all_users");
    return response.data;
};

// Create a new user
export const createUser = async (user: AddUser): Promise<User> => {
    const response = await instance.post("/user", user);
    return response.data;
};

// Updata a user
export const updateUser = async (id: string, user: Partial<User>): Promise<User> => {
    const response = await instance.put(`/user/${id}`, user);
    return response.data;
};

export const deleteUser = async (id: string): Promise<number> => {
    const response = await instance.delete(`/user/${id}`);
    return response.status;
}