import React from 'react'
import LoginButton from './LoginButton.jsx'
import SignupButton from './SignupButton.jsx'
import 'bootstrap/dist/css/bootstrap.min.css'

function Home() {

    return (
        <div className='bg-dark-subtle bg-gradient vh-100'>
            <nav className="navbar bg-light bg-gradient border-bottom border-1 border-secondary-subtle">
                <div className="container-fluid">
                    <span className="navbar-brand text-secondary mb-0 h1">Flowbot</span>
                </div>
            </nav>
            
            <div className="d-grid gap-2 col-2 mx-auto p-2 mt-3">
                <LoginButton />
                <SignupButton />
            </div>
        </div>
    )
}

export default Home
