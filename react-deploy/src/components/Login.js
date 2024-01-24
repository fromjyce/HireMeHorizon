import logo from "./LogoTrans.png";

function Login() {
  return (
    <>
      <title>Sign In</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <meta httpEquiv="X-UA-Compatible" content="ie=edge" />
      <link href="login.css" rel="stylesheet" />
      <header>
        <img alt={"logo"} src={logo} height={75} width={210} />
        <nav>
          <ul className='main-nav'>
            <li className="first">
              <a href="premain.html" className="aboutus">
                About Us
              </a>
            </li>
            <li>
              <form action="register.html">
                <button className="register">Register</button>
              </form>
            </li>
          </ul>
        </nav>
      </header>
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
