import instance from "@/services/instance.tsx";
import {Goal} from "@/types/Goal.ts";
import {AddGoal} from "@/types/AddGoal.ts";

// Get all goals
export const getAllGoals = async () => {
    const response = await  instance.get("goals");
    return response.data;
}

// Create a new goal
export const createGoal = async (goal: AddGoal): Promise<number> => {
    const response = await instance.post("goals", goal);
    return response.status;
}

// Update a goal
export const updateGoal = async (id: string, goal: Partial<Goal>): Promise<Goal> => {
    const response = await instance.put(`/goals/${id}`, goal);
    return response.data;
}

// Delete a goal
export const deleteGoal = async (id: string): Promise<number> => {
    const response = await instance.delete(`/goals/${id}`);
    return response.status;
}