import {useAuthStore} from "@/auth/store/auth.store.tsx";
import { NavigationMenu } from "radix-ui";
import { CaretDownIcon } from "@radix-ui/react-icons";
import "./AdminNavBar.css";

const AdminNavBar = () => {
    const { logout } = useAuthStore();

    return (

        <NavigationMenu.Root className="NavigationMenuRoot">
            <NavigationMenu.List className="NavigationMenuList">
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


    )

}

export default AdminNavBar;