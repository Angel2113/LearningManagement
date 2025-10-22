import {useEffect, useState} from "react";
import {createGoal, deleteGoal, getAllGoals, updateGoal} from "@/services/goalsService..tsx";
import {NavigationMenu} from "radix-ui";
import {Dialog, Button, Grid, Heading, Card, Flex, Badge, Text, TextArea} from '@radix-ui/themes';
import {useAuthStore} from "@/auth/store/auth.store.tsx";
import {Goal} from "@/types/Goal.ts";
import {Pencil2Icon, TrashIcon} from "@radix-ui/react-icons";
import {AddGoal} from "@/types/AddGoal.ts";
import "react-datepicker/dist/react-datepicker.css";
import {getAISuggestion} from "@/services/ai_services.tsx";


export const UserHomePage = () => {
    const {logout} = useAuthStore();
    const [goals, setGoals] = useState<Goal[]>([]);
    const [deleteSelect, setdeleteSelect] = useState<Goal | null>(null);
    const [editSelect, setEditSelect] = useState<Goal | null>(null);
    const [AddGoal, setAddGoal] = useState<AddGoal>({
        title: "",
        current_level: "basic",
        resources: "",
        target_date: "",
        days_per_week: 0,
        hours_per_day: 0,
        status: "new",
        ia_suggestion: "hello!"
    });

    const fetchGoals = async () => {
        try {
            const response = await getAllGoals();
            setGoals(response);
        } catch (error) {
            throw new Error('Error fetching goals');
        }
    }

    useEffect(() => {
        fetchGoals()
    }, []);

    const newGoal = async() => {
        if(AddGoal) {
            try {
                const response = await createGoal(AddGoal);
                console.log(`Response: ${response}`);
                if (response === 200) {
                    await fetchGoals();
                }
            } catch (error) {
                throw new Error('Error adding goal');
            }
        }
    }

    const handleUpdateGoal = async () => {
        if(editSelect){
            try {
                const response = await updateGoal(editSelect.id, editSelect);
                if(response) {
                    alert("Goal updated successfully");
                } else {
                    alert("Error updating goal");
                    await fetchGoals();
                }
            } catch (error) {
                alert("Error updating goal");
                throw new Error('Error updating goal');
            }
        }

    }

    const handleDeleteGoal = async () => {
        if(deleteSelect) {
            try {
                const response = await deleteGoal(deleteSelect.id);
                if(response === 200) {
                    setdeleteSelect(null);
                    await fetchGoals();
                    alert("Goal deleted successfully");
                } else {
                    alert("Error deleting goal");
                }
            } catch (error) {
                alert("Error deleting goal");
                throw new Error('Error deleting goal');
            }
        }
    }

    const getSuggestion = async () => {
        if(AddGoal) {
            try {
                const response = await getAISuggestion(AddGoal);
                console.log(response);
                setAddGoal({
                            ...AddGoal,
                            ia_suggestion: response,
                        } as AddGoal)

            } catch (error) {
                throw new Error('Error getting suggestions');
            }

        }
    }
    return (
        <>
            <NavigationMenu.Root className="NavigationMenuRoot">
                <NavigationMenu.List className="flex NavigationMenuList gap-4">
                    <NavigationMenu.Item>
                        <Heading as="h1" className="text-center mb-4">User Dashboard</Heading>
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
                    <Flex justify="start" my="4">
                        <Heading as="h2">My Goals</Heading>
                    </Flex>
                    <Flex justify="end" my="2">
                        <Dialog.Root>
                            <Dialog.Trigger>
                                <Button>Add Goal</Button>
                            </Dialog.Trigger>
                            <Dialog.Content>
                                <Dialog.Title>Add Goal</Dialog.Title>
                                <Grid columns="2" gap="4">
                                    <Flex gap="3" my="2">
                                        <label htmlFor="title" className="form-label">
                                            Title
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <input
                                            type="text"
                                            id="title"
                                            className="form-control"
                                            value={AddGoal?.title || ""}
                                            onChange={(e) =>
                                                setAddGoal({
                                                    ...AddGoal,
                                                    title: e.target.value,
                                                } as AddGoal)
                                            }
                                        />
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <label htmlFor="current_level" className="form-label">
                                            Level
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <select
                                            id="current_level"
                                            className="form-select"
                                            value={AddGoal?.current_level || "basic"}
                                            onChange={(e) =>
                                                setAddGoal({
                                                    ...AddGoal,
                                                    current_level: e.target.value,
                                                } as AddGoal)
                                            }
                                        >
                                            <option value="basic">Basic</option>
                                            <option value="intermediate">Intermediate</option>
                                            <option value="advance">Advance</option>
                                        </select>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <label htmlFor="resources" className="form-label">
                                            Resources
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <input
                                            type="text"
                                            id="resources"
                                            className="form-control"
                                            value={AddGoal?.resources || ""}
                                            onChange={(e) =>
                                                setAddGoal({
                                                    ...AddGoal,
                                                    resources: e.target.value,
                                                } as AddGoal)
                                            }
                                        />
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <label htmlFor="target_date" className="form-label">
                                            Target Date
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <input
                                            type="date"
                                            id="target_date"
                                            className="form-control"
                                            value={
                                                AddGoal?.target_date || ""
                                            }
                                            onChange={(e) =>
                                                setAddGoal({
                                                    ...AddGoal,
                                                    target_date: e.target.value,
                                                } as AddGoal)
                                            }
                                        />
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <label htmlFor="days_per_week" className="form-label">
                                            Days Per Week
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <input
                                            type="number"
                                            min="1"
                                            max="7"
                                            id="days_per_week"
                                            className="form-control"
                                            value={AddGoal?.days_per_week || 1}
                                            onChange={(e) =>
                                                setAddGoal({
                                                    ...AddGoal,
                                                    days_per_week: parseInt(e.target.value),
                                                } as AddGoal)
                                            }
                                        />
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <label htmlFor="hours_per_week" className="form-label">
                                            Hours Per Day
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <input
                                            type="number"
                                            min="1"
                                            max="8"
                                            id="hours_per_week"
                                            className="form-control"
                                            value={AddGoal?.hours_per_day || 1}
                                            onChange={(e) =>
                                                setAddGoal({
                                                    ...AddGoal,
                                                    hours_per_day: parseInt(e.target.value),
                                                } as AddGoal)
                                            }
                                        />
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <label htmlFor="status" className="form-label">
                                            Status
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <select
                                            id="status"
                                            className="form-select"
                                            value={AddGoal?.status || "new"}
                                            onChange={(e) =>
                                                setAddGoal({
                                                    ...AddGoal,
                                                    status: e.target.value,
                                                } as AddGoal)
                                            }
                                        >
                                            <option value="new">New</option>
                                            <option value="in_progress">In Progress</option>
                                            <option value="completed">Completed</option>
                                        </select>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <label htmlFor="description" className="form-label">
                                            IA Suggestion
                                        </label>
                                    </Flex>
                                    <Flex gap="3" my="2">
                                        <TextArea
                                            placeholder="IA Suggestion"
                                            value={AddGoal?.ia_suggestion}
                                            onChange={(e) => setAddGoal({
                                                    ...AddGoal,
                                                    ia_suggestion: e.target.value,
                                                } as AddGoal)}
                                        />
                                    </Flex>
                                </Grid>
                                <Flex gap="3" justify="end">
                                        <Button onClick={getSuggestion}>Get Plan</Button>
                                    <Dialog.Close>
                                        <Button variant="soft">Cancel</Button>
                                    </Dialog.Close>
                                    <Dialog.Close>
                                        <Button onClick={newGoal}>
                                            Save Changes
                                        </Button>
                                    </Dialog.Close>
                                </Flex>
                            </Dialog.Content>
                        </Dialog.Root>
                    </Flex>
                </Card>
                <Flex justify="start" my="4">
                    <Grid columns="3" gap="4">
                        {goals.map((g) => (
                            <Card className="hover:cursor-pointer hover:opacity-80" key={g.id}>
                                <Flex justify="between" align="center" my="2">
                                    <Grid columns="2">
                                        <Heading as="h3">{g.title}</Heading>
                                        <Badge
                                            color={
                                                g.status === "new"
                                                ? "green"
                                                : g.status === "inProgress"
                                                ? "blue"
                                                : g.status === "cancel"
                                                ? "red"
                                                : g.status === "completed"
                                                ? "gray"
                                                : "yellow"
                                            }
                                        >{g.status}</Badge>
                                    </Grid>
                                </Flex>
                                <Flex justify="between" my="2" gap="3">
                                    <Text>End Date: {g.target_date}</Text>
                                </Flex>
                                <Flex justify="between" my="2" gap="3">
                                    <Dialog.Root>
                                        <Dialog.Trigger>
                                            <Button
                                                color="red"
                                                title="Delete User"
                                                onClick={()=>{
                                                    setdeleteSelect(g)
                                                }}
                                            >
                                                <TrashIcon />
                                            </Button>
                                        </Dialog.Trigger>
                                        <Dialog.Content>
                                            <Flex>
                                                <Dialog.Title className="DialogTitle">
                                                    Delete Goal
                                                </Dialog.Title>
                                            </Flex>
                                            <Flex>
                                                <Dialog.Description className="DialogDescription">
                                                    Are you sure you want to delete user <strong>{g?.title}</strong>?
                                                </Dialog.Description>
                                            </Flex>
                                            <Flex gap="3" justify="end">
                                                <Dialog.Close>
                                                    <Button variant="soft">Cancel</Button>
                                                </Dialog.Close>
                                                <Dialog.Close>
                                                    <Button onClick={handleDeleteGoal}>Delete</Button>
                                                </Dialog.Close>
                                            </Flex>
                                        </Dialog.Content>
                                    </Dialog.Root>
                                    <Dialog.Root>
                                        <Dialog.Trigger>
                                            <Button
                                                onClick={() => {
                                                    setEditSelect(g)
                                                }}
                                                title="Update User"
                                            >
                                                <Pencil2Icon />
                                            </Button>
                                        </Dialog.Trigger>
                                        <Dialog.Content>
                                            <Dialog.Title>
                                                Update Goal {g.title}
                                            </Dialog.Title>
                                            <Grid columns="2" gap="4">
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="title" className="form-label">
                                                        Title
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <input
                                                        type="text"
                                                        id="title"
                                                        className="form-control"
                                                        value={editSelect?.title || ""}
                                                        onChange={(e) =>
                                                            setEditSelect({
                                                                ...editSelect,
                                                                title: e.target.value,
                                                            } as Goal)
                                                        }
                                                    />
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="current_level" className="form-label">
                                                        Level
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <select
                                                        id="current_level"
                                                        className="form-select"
                                                        value={editSelect?.current_level || "basic"}
                                                        onChange={(e) =>
                                                            setEditSelect({
                                                                ...editSelect,
                                                                current_level: e.target.value,
                                                            } as Goal)
                                                        }
                                                    >
                                                        <option value="basic">Basic</option>
                                                        <option value="intermediate">Intermediate</option>
                                                        <option value="advance">Advance</option>
                                                    </select>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="resources" className="form-label">
                                                        Resources
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <input
                                                        type="text"
                                                        id="resources"
                                                        className="form-control"
                                                        value={editSelect?.resources || ""}
                                                        onChange={(e) =>
                                                            setEditSelect({
                                                                ...editSelect,
                                                                resources: e.target.value,
                                                            } as Goal)
                                                        }
                                                    />
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="target_date" className="form-label">
                                                        Target Date
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <input
                                                        type="date"
                                                        id="target_date"
                                                        className="form-control"
                                                        value={
                                                            editSelect?.target_date || ""
                                                        }
                                                        onChange={(e) =>
                                                            setEditSelect({
                                                                ...editSelect,
                                                                target_date: e.target.value,
                                                            } as Goal)
                                                        }
                                                    />
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="days_per_week" className="form-label">
                                                        Days Per Week
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <input
                                                        type="number"
                                                        min="1"
                                                        max="7"
                                                        id="days_per_week"
                                                        className="form-control"
                                                        value={editSelect?.days_per_week || 1}
                                                        onChange={(e) =>
                                                            setEditSelect({
                                                                ...editSelect,
                                                                days_per_week: parseInt(e.target.value),
                                                            } as Goal)
                                                        }
                                                    />
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="hours_per_week" className="form-label">
                                                        Hours Per Day
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <input
                                                        type="number"
                                                        min="1"
                                                        max="8"
                                                        id="hours_per_week"
                                                        className="form-control"
                                                        value={editSelect?.hours_per_day || 1}
                                                        onChange={(e) =>
                                                            setEditSelect({
                                                                ...editSelect,
                                                                hours_per_day: parseInt(e.target.value),
                                                            } as Goal)
                                                        }
                                                    />
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="status" className="form-label">
                                                        Status
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <select
                                                        id="status"
                                                        className="form-select"
                                                        value={editSelect?.status || "new"}
                                                        onChange={(e) =>
                                                            setEditSelect({
                                                                ...editSelect,
                                                                status: e.target.value,
                                                            } as Goal)
                                                        }
                                                    >
                                                        <option value="new">New</option>
                                                        <option value="in_progress">In Progress</option>
                                                        <option value="completed">Completed</option>
                                                    </select>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <label htmlFor="description" className="form-label">
                                                        IA Suggestion
                                                    </label>
                                                </Flex>
                                                <Flex gap="3" my="2">
                                                    <TextArea placeholder="IA Suggestion" />
                                                </Flex>
                                            </Grid>
                                            <Flex gap="3" justify="end">
                                                <Dialog.Close>
                                                    <Button variant="soft">Cancel</Button>
                                                </Dialog.Close>
                                                <Dialog.Close>
                                                    <Button onClick={handleUpdateGoal}>Save</Button>
                                                </Dialog.Close>
                                            </Flex>
                                        </Dialog.Content>
                                    </Dialog.Root>
                                </Flex>
                            </Card>
                        ))}
                    </Grid>
                </Flex>
            </div>
        </>
    );
}