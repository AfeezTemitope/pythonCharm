import Home from "../containers/home";
import RegistrationForm from "../components/RegistrationForm";
import Login from "../pages/loginPage/login";

export const ROUTES = [
    {
        path: '/',
        element: <Home/>,
        children: [
            {
                path: '/home',
                element: <Home />,
            },
             {
                path: '/home',
                element: <RegistrationForm/>,
            },
            {
                path: '/login',
                element: <Login/>,
            },


        ]

    }
];