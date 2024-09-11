import React from 'react'
import {useRoutes} from "react-router-dom";
import {ROUTES} from "./Routes";

function App(){
    return(
        useRoutes(ROUTES)
    )
}
export default App;