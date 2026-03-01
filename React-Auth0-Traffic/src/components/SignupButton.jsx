import React from 'react'
import { useAuth0 } from '@auth0/auth0-react'
import 'bootstrap/dist/css/bootstrap.min.css'

function SignupButton() {
  const { loginWithRedirect } = useAuth0();

  const handleSignup = async () => {
    await loginWithRedirect({
      appState: {
        returnTo: "/user",
      },
      authorizationParams: {
        screen_hint: "signup",
      },
    });
  };

  return (
    <button className="btn btn-secondary p-2" type="button" onClick={handleSignup}>
      Sign Up
    </button>
  );
};

export default SignupButton
