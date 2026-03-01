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
            <div className="text-center lead px-lg-5 pt-5">
                <h2>FlowBot by Traffic Crusaders</h2>
                <h4>Make Models, Make Change</h4>
                <p>We set out to help make a Smart City and we decided to help tackle one of the most frustrating aspects of modern city life- traffic. With commutes spending upwards of several hours in each direction to reach their place of work or school, small changes to flow controls can make a huge impact not just on happiness and stress reduction; but also the environment. Cars are at their most fuel inefficient when in the idling, stop and go traffic of the modern city. Small improvements to infrastructure can reduce emissions and decrease gas consumption. To address this issue, we created a foundational model called FlowBot which can be fine-tuned on traffic flow patterns of a given city to help inform light cycles and improve infrastructure.</p>
            </div>
            <div className="d-grid gap-2 col-2 mx-auto p-2 mt-3">
                <LoginButton />
                <SignupButton />
            </div>
        </div>
    )
}

export default Home
