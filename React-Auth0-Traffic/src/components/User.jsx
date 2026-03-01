import React, { useEffect, useState } from 'react'
import { useAuth0 } from "@auth0/auth0-react";
import LogoutButton from './LogoutButton.jsx'
import FileUpload from './FileUpload.jsx'
import axios from 'axios'

function User() {

    const { user } = useAuth0();
    const username = user.nickname;

    // const getUserData = () => {
    //     axios.get(`http://localhost:5000/user/${username}`)
    //     .then(response => {

    //     })
    //     .catch(error => {
    //         console.error('There was an error retrieving the data', error);
    //     })
    // }

    // const saveNewUserData = (dataObj) => {
    //     console.log(dataObj);
    //     console.log(dataObj[0]);
    //     setUserResData([dataObj]);
    // }

    return (
        <div className='vh-100 bg-dark-subtle bg-gradient'>
            <nav className="navbar bg-light bg-gradient">
                <div className="container-fluid">
                    <span className="navbar-brand text-secondary mb-0 h1">Flowbot</span>
                    <span className="text-primary mb-0 h4">Welcome, { username }</span>
                <LogoutButton />
                </div>
            </nav>

            <FileUpload />
        </div>
    )
}

export default User
