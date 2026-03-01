import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import App from './App.jsx'
import Auth0WithNavigate from "./Auth0WithNavigate.jsx"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BrowserRouter>
      <Auth0WithNavigate>
        <App />
      </Auth0WithNavigate>
    </BrowserRouter>
  </StrictMode>
)
