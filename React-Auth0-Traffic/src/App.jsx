import React from 'react'
import { Route, Routes } from "react-router-dom"
import Home from './components/Home.jsx'
import Callback from './components/Callback.jsx'
import User from './components/User.jsx'

function App() {
  
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/callback" element={<Callback />} />
      <Route path="/user" element={<User />} />
    </Routes>
  )
}

export default App
