import { create } from 'zustand'
import {login} from "@/services/auth.tsx";

type AuthState = {
    // Properties
    user: string | null,
    token: string | null,
    role: string | null,

    // Getters

    // Actions
    login: (username: string, password:string) => Promise<boolean>;
    logout: () => void;
};

export const useAuthStore = create<AuthState>()((set) => ({
    user: null,
    token: null,
    role: null,

    // actions
    login: async(username: string, password:string) => {
        console.log('usernamen: ' + username + ' password: ' + password);

        try {
            const data = await login(username, password);
            localStorage.setItem("token", data.access_token);
            set({token: data.token})
            return true;
        } catch (error) {
            localStorage.removeItem("token");
            set({token: null, user: null, role: null})
            return false;
        }
    },
    logout: () => {
        localStorage.removeItem("token");
        set({token: null, user: null, role: null})
    }
}))
