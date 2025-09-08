
import {createUser, deleteUser, getAllUsers, updateUser} from "@/services/userService.ts";
import {useEffect, useState} from "react";
import {User} from "@/types/User";
import {AddUser} from "@/types/AddUser.ts";
import {Dialog, Button, Grid, Heading, Card,  Flex, Badge, Text} from '@radix-ui/themes';
import {NavigationMenu} from "radix-ui";
import {useAuthStore} from "@/auth/store/auth.store.tsx";
import "./AdminNavBar.css";
import { TrashIcon, Pencil2Icon } from "@radix-ui/react-icons"

export const AdminHomePage = () => {
    const { logout } = useAuthStore();
    const [users, setUsers] = useState<User[]>([]);
    const [addUser, setAddUser] = useState<AddUser |  null>(null);
    const [selectedUser, setSelectedUser] = useState<User | null>(null);
    const [editedUser, setEditedUser] = useState<User | null>(null);

    const [showAddModal, setShowAddModal] = useState(false)


    const fetchUsers = async () => {
        try {
            const response = await getAllUsers();
            setUsers(response);
        } catch (err) {
            throw new Error('Error fetching users');
        }
    }

    useEffect(() => {
        fetchUsers();
    }, []);

    const handleAddUser= async (username: string) => {
        console.log(`Adding user: ${username}`);
        if(addUser) {
            try {
                const response =  await createUser(addUser);
                setShowAddModal(false);
                console.log(`Response: ${response}`);
                if (response === 200) {
                    await fetchUsers();
                }
            } catch (error) {
                throw new Error('Error adding user');
            }
        }

    };

    const handleUpdateUser = async (username: string) => {
        console.log(`Updating user: ${username}`);
        if(editedUser){
            try {
                updateUser(editedUser.id, editedUser);
                await fetchUsers(); // <- Why this part is not working?
            }catch (error) {
                throw new Error('Error updating user');
            }
        }
    };

    const handleDeleteUser = async (username: string) => {
        console.log(`Dude, are you trying to delete the user: ${username} ?`);
        if(selectedUser){
            try {
                await deleteUser(selectedUser.id);
                await fetchUsers();
            } catch (err) {
                throw new Error('Error deleting user');
            }
        }
    };


    return (
        <>
            <NavigationMenu.Root className="NavigationMenuRoot">
                <NavigationMenu.List className="NavigationMenuList">
                    <NavigationMenu.Item>
                        <Heading as="h1" className="text-center mb-4">Admin Dashboard</Heading>
                    </NavigationMenu.Item>
                    <NavigationMenu.Item>
                        <NavigationMenu.Link
                            className="NavigationMenuLink"
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
                        >Add User</NavigationMenu.Link>
                    </NavigationMenu.Item>
                    <NavigationMenu.Item>
                        <NavigationMenu.Link
                            className="NavigationMenuLink"
                            onClick={logout}
                        >
                            Logout
                        </NavigationMenu.Link>
                    </NavigationMenu.Item>
                </NavigationMenu.List>
            </NavigationMenu.Root>
            <div className="flex min-h-screen flex-col items-center justify-center p-24">
                <br/>
                <Card>
                    <Flex justify="start" my="2">
                        <Heading as="h2">User List</Heading>
                    </Flex>
                    <Flex justify="end" my="2">
                        <Dialog.Root>
                            <Dialog.Trigger>
                                <Button>Add User</Button>
                            </Dialog.Trigger>
                            <Dialog.Content>
                                <Dialog.Title>Add User</Dialog.Title>
                                <Flex gap="3" my="2">
                                    <Grid columns="2" gap="4">
                                        <label htmlFor="username" className="form-label">
                                            Username
                                        </label>
                                        <input
                                            type="text"
                                            id="username"
                                            className="form-control"
                                            value={addUser?.username || ""}
                                            onChange={(e) =>
                                                setAddUser({
                                                    ...addUser,  // Copy properties from addUser on new user
                                                    username: e.target.value,
                                                } as AddUser)
                                            }
                                        />
                                    </Grid>
                                </Flex>
                                <Flex gap="3" my="2">
                                    <Grid columns="2" gap="4">
                                        <label htmlFor="email" className="form-label">
                                            Email
                                        </label>
                                        <input
                                            type="email"
                                            id="email"
                                            className="form-control"
                                            value={addUser?.email || ""}
                                            onChange={(e) =>
                                                setAddUser({
                                                    ...addUser,  // Copy properties from editedUser in a new user
                                                    email: e.target.value,
                                                } as AddUser)
                                            }
                                        />
                                    </Grid>
                                </Flex>
                                <Flex gap="3" my="2">
                                    <Grid columns="2" gap="4">
                                        <label htmlFor="role" className="form-label">
                                            Role
                                        </label>
                                        <select
                                            id="role"
                                            className="form-select"
                                            value={addUser?.role || ""}
                                            onChange={(e) =>
                                                setAddUser({
                                                    ...addUser,
                                                    role: e.target.value,
                                                } as AddUser)
                                            }
                                        >
                                            <option value="user">User</option>
                                            <option value="admin">Admin</option>
                                        </select>
                                    </Grid>
                                </Flex>
                                <Flex gap="3" my="2">
                                    <Grid columns="2" gap="4">
                                        <label htmlFor="role" className="form-label">
                                            Password
                                        </label>
                                        <input
                                            type="password"
                                            id="password"
                                            title="Password"
                                            className="form-control"
                                            value={ addUser?.password || ""}
                                            onChange={(e) =>
                                                setAddUser({
                                                    ...addUser,
                                                    password: e.target.value,
                                                } as AddUser)
                                            }
                                        />
                                    </Grid>
                                </Flex>
                                <Flex gap="3" my="2">
                                    <Grid columns="2" gap="4">
                                        <label htmlFor="role" className="form-label">
                                            Confirmation Password
                                        </label>
                                        <input
                                            type="password"
                                            id="confirm_password"
                                            title="confirm_password"
                                            className="form-control"
                                            value={ addUser?.password_confirmation || ""}
                                            onChange={(e) =>
                                                setAddUser({
                                                    ...addUser,
                                                    password_confirmation: e.target.value,
                                                } as AddUser)
                                            }
                                        />
                                    </Grid>
                                </Flex>
                                <Flex gap="3" justify="end">
                                    <Dialog.Close>
                                        <Button variant="soft">Cancel</Button>
                                    </Dialog.Close>
                                    <Dialog.Close>
                                        <Button onClick={handleAddUser}>
                                            Save Changes
                                        </Button>
                                    </Dialog.Close>
                                </Flex>
                            </Dialog.Content>
                        </Dialog.Root>
                    </Flex>
                </Card>
                <br/>
                <Grid columns="3" gap="4">
                    {users.map((u) => (
                        <Card className="hover:cursor-pointer hover:opacity-80" key={u.id}>
                            <Flex justify="between" align="center">
                                <Heading as="h3">{u.username}</Heading>
                                <Badge
                                    color={
                                        u.role == "admin" ? "red" : "yellow"
                                    }
                                >{u.role}</Badge>
                            </Flex>
                            <Flex justify="between" my="2">
                                <Text>Email: {u.email}</Text>
                            </Flex>
                            <Flex justify="between" my="2">
                                <Dialog.Root>
                                    <Dialog.Trigger>
                                        <Button
                                            onClick={() => {
                                                setEditedUser(u);
                                            }}
                                            title="Update User"
                                        >
                                            <Pencil2Icon />
                                        </Button>
                                    </Dialog.Trigger>
                                    <Dialog.Content>
                                        <Flex justify="center">
                                            <Dialog.Title className="DialogTitle" >
                                                Update User
                                            </Dialog.Title>
                                        </Flex>
                                        <Flex gap="3" my="2">
                                            <Grid columns="2" >
                                                <label htmlFor="username" className="form-label">
                                                    Username
                                                </label>
                                                <input
                                                    type="text"
                                                    id="username"
                                                    className="form-control"
                                                    value={editedUser?.username || ""}
                                                    onChange={(e) =>
                                                        setEditedUser({
                                                            ...editedUser,  // Copy properties from editedUser in a new user
                                                            username: e.target.value,
                                                        } as User)
                                                    }
                                                />
                                            </Grid>
                                        </Flex>
                                        <Flex gap="3" my="2">
                                            <Grid columns="2">
                                                <label htmlFor="email" className="form-label">
                                                    Email
                                                </label>
                                                <input
                                                    type="text"
                                                    id="email"
                                                    className="form-control"
                                                    value={editedUser?.email || ""}
                                                    onChange={(e) =>
                                                        setEditedUser({
                                                            ...editedUser,  // Copy properties from editedUser in a new user
                                                            email: e.target.value,
                                                        } as User)
                                                    }
                                                />
                                            </Grid>
                                        </Flex>
                                        <Flex gap="3" my="2">
                                            <Grid columns="2">
                                                <label htmlFor="role" className="form-label">
                                                    Role
                                                </label>
                                                <select
                                                    id="role"
                                                    className="form-select"
                                                    value={editedUser?.role || ""}
                                                    onChange={(e) =>
                                                        setEditedUser({
                                                            ...editedUser,
                                                            role: e.target.value,
                                                        } as User)
                                                    }
                                                >
                                                    <option value="user">User</option>
                                                    <option value="admin">Admin</option>
                                                </select>
                                            </Grid>
                                        </Flex>
                                        <Flex gap="3" justify="end">
                                            <Dialog.Close>
                                                <Button variant="soft">Cancel</Button>
                                            </Dialog.Close>
                                            <Dialog.Close>
                                                <Button onClick={handleUpdateUser}>
                                                    Save Changes
                                                </Button>
                                            </Dialog.Close>
                                        </Flex>
                                    </Dialog.Content>
                                </Dialog.Root>
                                <Dialog.Root>
                                    <Dialog.Trigger>
                                        <Button
                                            color="red"
                                            onClick={() => {
                                                setSelectedUser(u);
                                            }}
                                            title="Delete User"
                                        >
                                            <TrashIcon />
                                        </Button>
                                    </Dialog.Trigger>
                                    <Dialog.Content>
                                        <Flex>
                                            <Dialog.Title className="DialogTitle">
                                                Delete User
                                            </Dialog.Title>
                                        </Flex>
                                        <Flex>
                                            <Dialog.Description className="DialogDescription">
                                                Are you sure you want to delete user <strong>{selectedUser?.username}</strong>?
                                            </Dialog.Description>
                                        </Flex>

                                        <Flex gap="3" justify="end">
                                            <Dialog.Close>
                                                <Button onClick={handleDeleteUser}>Delete</Button>
                                            </Dialog.Close>
                                            <Dialog.Close>
                                                <Button variant="soft">Cancel</Button>
                                            </Dialog.Close>
                                        </Flex>
                                    </Dialog.Content>
                                </Dialog.Root>
                            </Flex>
                        </Card>
                    ))}
                </Grid>
            </div>
        </>
    );
};

export default AdminHomePage;