import {create} from 'zustand'
import {persist} from "zustand/middleware";
import {login} from "@/services/auth.tsx";
import {jwtDecode} from "jwt-decode";

type JwtPayload = {
    user_id: string;
    username: string;
    email: string;
    role: string;
    expiration: string;
};

type AuthState = {
    // Properties
    user_id: string | null;
    username: string | null;
    email: string | null;
    role: string | null;
    expiration: string | null;
    token: string | null;

    // Getters

    // Actions
    login: (username: string, password: string) => Promise<boolean>;
    logout: () => void;
};

export const useAuthStore = create<AuthState>()(
    persist(
        (set) => ({
            user_id: null,
            username: null,
            email: null,
            role: null,
            expiration: null,
            token: localStorage.getItem("token") || null,

            // Login Action
            login: async (username: string, password: string) => {
                try {
                    const data = await login(username, password);
                    localStorage.setItem("token", data.access_token);

                    const token_data = jwtDecode<JwtPayload>(data.access_token);

                    set({
                        token: data.access_token,
                        user_id: token_data.user_id,
                        username: token_data.username,
                        email: token_data.email,
                        role: token_data.role,
                        expiration: token_data.expiration,
                    });
                    return true;
                } catch (error) {
                    console.error("Login failed:", error);
                    localStorage.removeItem("token");
                    set({token: null, username: null, role: null, user_id: null});

                    return false;
                }
            },
            logout: () => {
                localStorage.removeItem("token");
                localStorage.removeItem("auth-storage");
            },
        }),
        {
            name: "auth-storage",
        }
    )
);
