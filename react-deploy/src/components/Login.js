import "../styles/login.css";
import Header from './Header.js';

function Login() {
  return (
    <>
    <Header />
      <div className="container">
        <p className="heading">Sign In HIREMEHORIZON</p>
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
    </>
  );
}

export default Login;
