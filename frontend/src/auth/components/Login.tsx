import {useState} from "react";
import {useNavigate} from "react-router-dom";
import {useAuthStore} from "@/auth/store/auth.store.tsx";
import {Button, Heading, Box, Flex, Card, TextField, Text, Container} from "@radix-ui/themes";

export const LoginPage = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const navigate = useNavigate();
    const {login} = useAuthStore();

    async function handleSubmit(e: React.FormEvent) {
        e.preventDefault();
        setError("");
        const isValid = await login(username, password);
        if (isValid) {
            navigate("/home");
        } else {
            setError("Invalid credentials");
        }
    }

    return (
        <Flex
            align="center"
            justify="center"
            className="min-h-screen"

        >
            <Card
                variant="surface"
                size="4"
                className="w-full"

            >
                <Heading size="4" className="text-center mb-4">
                    Login
                </Heading>
                <br></br>
                <form onSubmit={handleSubmit}>
                    <Flex direction="column" gap="4">
                        <Container width="100%" className="mt-2">
                            <Text>Username</Text>
                            <TextField.Root
                                placeholder="Enter your username"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                            />
                        </Container>
                        <Container width="100%" className="mt-2">
                            <Text size="2">Password</Text>
                            <TextField.Root
                                type="password"
                                placeholder="Enter your password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </Container>

                        {/* Mensaje de error */}
                        {error && (
                            <Container
                                className="text-danger"

                            >
                                {error}
                            </Container>
                        )}
                        <Button type="submit" className="w-full" variant="surface">
                            Login
                        </Button>
                    </Flex>
                </form>

                <Flex direction="column" gap="4">
                    <Button
                        className="w-full"
                        variant="surface"
                        onClick={() => navigate("/register")}
                    >
                        Register
                    </Button>
                </Flex>
            </Card>
        </Flex>
    );
};

export default LoginPage;