import instance from "@/services/instance.tsx";
import {AddGoal} from "@/types/AddGoal.ts";

export const getAISuggestion = async (goal: AddGoal) => {
    const response = await instance.post("chat", goal);
    return response.data;
}