import React from 'react'
import ReactDOM from 'react-dom/client'
import {BrowserRouter} from "react-router-dom";
import {AppRouter} from "./router/AppRouter";
import './index.css'
import "@radix-ui/themes/styles.css";
import { Theme } from "@radix-ui/themes";

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
      <Theme appearance="dark" scaling="90%">
          <BrowserRouter>
            <AppRouter  />
          </BrowserRouter>
      </Theme>
  </React.StrictMode>,
)
