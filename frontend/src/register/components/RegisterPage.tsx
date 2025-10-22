import {useState} from "react";
import {AddUser} from "@/types/AddUser.ts";
import {registerUser} from "@/services/userService.ts";
import {useNavigate} from "react-router-dom";
import {Dialog, Button, Grid, Heading, Card, Flex, Badge, Text, TextArea} from '@radix-ui/themes';


export const RegisterPage = () => {
    const [user, setUser] = useState<AddUser>({
        username: "",
        email: "",
        role: "user",
        password: "",
        password_confirmation: ""
    });
    const navigate = useNavigate();

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();
        if (!user?.username || user.username.length < 5) {
           alert('User length must be at least 5 characters long');
           return;
       }

       if (!user.email || user.email.length < 5) {
           alert('Email has not the correct format');
           return;
       }

       if (!user.password || user.password.length < 8) {
           alert('Password must be at least 8 characters long');
           return;
       }

       if (user.password !== user.password_confirmation) {
           alert('The passwords do not match');
           return;
       }


        if(user){
            try {
                const response = await registerUser(user);
                if (response === 200) {
                    navigate('/login');
                }
            } catch (error) {
                console.error('Error adding user:', error.message);
                throw new Error('Error adding user');
            }
        }
    }
    return (
        <>
            <div className="flex min-h-screen flex-col items-center justify-center p-24">
                <br/>
                <Card>
                    <form onSubmit={handleSubmit}>
                    <Flex justify="start" my="4">
                        <Heading as="h2">Add User</Heading>
                    </Flex>
                    <Flex justify="start" my="2">
                        <Grid columns="2" gap="4">
                            <Flex gap="3" my="2">
                                <label htmlFor="title" className="form-label">
                                    Title
                                </label>
                            </Flex>
                            <Flex gap="3" my="2">
                                <input
                                    type="text"
                                    id="username"
                                    className="form-control"
                                    value={user?.username || ""}
                                    onChange={(e)=>{
                                        setUser({
                                            ...user,
                                            username: e.target.value,
                                        } as AddUser)
                                    }}
                                />
                            </Flex>
                        </Grid>
                    </Flex>
                    <Flex justify="start" my="2">
                        <Grid columns="2" gap="4">
                            <Flex gap="3" my="2">
                                <label htmlFor="email" className="form-label">
                                    Email
                                </label>
                            </Flex>
                            <Flex gap="3" my="2">
                                <input
                                    type="email"
                                    id="email"
                                    className="form-control"
                                    value={user?.email || ""}
                                    onChange={(e)=>{
                                        setUser({
                                            ...user,
                                            email: e.target.value,
                                        } as AddUser)
                                    }}
                                />
                            </Flex>
                        </Grid>
                    </Flex>
                    <Flex justify="start" my="2">
                        <Grid columns="2" gap="4">
                            <Flex gap="3" my="2">
                                <label htmlFor="role" className="form-label">
                                    Role
                                </label>
                            </Flex>
                            <Flex gap="3" my="2">
                                <select
                                    id="role"
                                    className="form-select"
                                    value={user?.role || ""}
                                    onChange={(e) => {
                                        setUser({
                                            ...user,
                                            role: e.target.value,
                                        } as AddUser)
                                    }}
                                >
                                    <option value="user">User</option>
                                </select>
                            </Flex>
                        </Grid>
                    </Flex>
                    <Flex justify="start" my="2">
                        <Grid columns="2" gap="4">
                            <Flex gap="3" my="2">
                                <label htmlFor="role" className="form-label">
                                    Password
                                </label>
                            </Flex>
                            <Flex gap="3" my="2">
                                <input
                                    type="password"
                                    id="password"
                                    title="Password"
                                    className="form-control"
                                    value={user?.password || ""}
                                    onChange={(e)=>{
                                        setUser({
                                            ...user,
                                            password: e.target.value,
                                        } as AddUser)
                                    }}
                                />
                            </Flex>
                        </Grid>
                    </Flex>
                    <Flex justify="start" my="2">
                        <Grid columns="2" gap="4">
                            <Flex gap="3" my="2">
                                <label htmlFor="role" className="form-label">
                                    Confirmation Password
                                </label>
                            </Flex>
                            <Flex gap="3" my="2">
                                <input
                                    type="password"
                                    id="confirm_password"
                                    title="confirm_password"
                                    className="form-control"
                                    value={user?.password_confirmation || ""}
                                    onChange={(e)=>{
                                        setUser({
                                            ...user,
                                            password_confirmation: e.target.value,
                                        } as AddUser)
                                    }}
                                />
                            </Flex>
                        </Grid>
                    </Flex>
                    <Flex justify="start" my="2">
                        <Grid columns="2" gap="4">
                            <Flex gap="3" my="2">
                                <button className="btn btn-primary" type="submit">
                                    Save
                                </button>
                            </Flex>
                            <Flex gap="3" my="2">
                            </Flex>
                        </Grid>
                    </Flex>
                    </form>
                </Card>
            </div>

        </>
    )

}