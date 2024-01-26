import "../styles/login.css";
import React, { useEffect } from "react";

function Login() {
  useEffect(() => {
    return () => {
      document.title = "Sign In";
    };
  }, []);

  return (
    <>
      <div className="Login" id="Login">
        <div className="login-container">
          <div className="container">
            <p className="heading">Sign In to HIREMEHORIZON</p>
            {/* {% if error_message %}
      <p class="errormessage">{{ error_message }}</p>
      {% endif %} */}
            <form method="post">
              <input
                type="text"
                name="username"
                placeholder="Username"
                required=""
              />
              <br />
              <input
                type="password"
                name="password"
                placeholder="Password"
                required=""
              />
              <br />
              <button className="login" type="submit">
                Sign In
              </button>
            </form>
            <p className="registercontent">Forgot your password?</p>
          </div>
        </div>
      </div>
    </>
  );
}

export default Login;
