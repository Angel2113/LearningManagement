import {Button, Dialog, Flex} from "@radix-ui/themes/dist/esm";
import {useState} from "react";


const DeleteDialog = () => {
    const [showDeleteModal, setShowDeleteModal] = useState(false);

    return (
        <>
            <Dialog.Content className="DialogContent">
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
        </>
    )
}