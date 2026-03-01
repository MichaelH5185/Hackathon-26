import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'
import 'bootstrap/dist/css/bootstrap.min.css'

function LoginButton() {
  const { loginWithRedirect } = useAuth0();

  const handleLogin = async () => {
    await loginWithRedirect({
      appState: {
        returnTo: "/user",
      },
    });
  };

  return (
    <button className="btn btn-primary p-2" type="button" onClick={handleLogin}>
      Log In
    </button>
  );
};

export default LoginButton
