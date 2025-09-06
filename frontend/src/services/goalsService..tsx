

// Get all the goals
import instance from "@/services/instance.tsx";

export const getAllGoals = async () => {
    const response =await  instance.get("goals");
    return response.data;
}