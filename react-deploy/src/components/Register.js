import "../styles/register.css";
import React, { useEffect } from "react";

function Register() {
  useEffect(() => {
    return () => {
      document.title = "Register";
    };
  }, []);

  return (
    <>
      <div className="Register" id="Register">
        <div className="register-container">
          <h1>REGISTRATION PAGE</h1>
          <div className="box">
            <div className="left">
              <div className="info">
                <div className="acc">
                  <div className="circle1">
                    <p className="numbers">1</p>
                  </div>
                  <p className="info-word">Account information</p>
                </div>
                <div className="personal">
                  <div className="circle1">
                    <p className="numbers">2</p>
                  </div>
                  <p className="info-word">Personal information</p>
                </div>
                <div className="edu">
                  <div className="circle1">
                    <p className="numbers">3</p>
                  </div>
                  <p className="info-word">Educational information</p>
                </div>
              </div>
            </div>
            <form className="accinfo">
              <p className="acc-para">Account Information</p>
              <div className="input-acc">
                <p>Email</p>
                <input
                  type="text"
                  name="email"
                  placeholder="Your Email"
                  required
                />
                <p>Username</p>
                <input
                  type="text"
                  name="username"
                  placeholder="Your Username"
                  required
                />
                <p>Password</p>
                <input
                  type="password"
                  name="password"
                  placeholder="Your Password"
                  required
                />
                <p>Confirm Password</p>
                <input
                  type="password"
                  name="confpassword"
                  placeholder="Confirm Password"
                  required
                />
              </div>
              <button className="save" type="submit">
                Save and Next
              </button>
            </form>
            <form className="persoinfo">
              <p className="perso-para">Personal Information</p>
              <ul className="input-perso">
                <li>
                <p>First Name</p>
                <input
                  type="text"
                  name="firstname"
                  placeholder="Your First Name"
                  required
                />
                </li>
                <li>
                <p>Middle Name</p>
                <input
                  type="text"
                  name="middlename"
                  placeholder="Your Middle Name"
                />
                </li>
                <li>
                <p>Last Name</p>
                <input
                  type="text"
                  name="lastname"
                  placeholder="Your Last Name"
                  required
                />
                </li>
                <li>
                <p>Date of Birth</p>
                <input
                  type="text"
                  name="date"
                  placeholder="DD-MM-YYYY"
                  required
                />
                </li>
                <li>
                <p>Phone Number</p>
                <input
                  type="text"
                  name="phoneno"
                  placeholder="Your Phone Number"
                  required
                />
                </li>
                <li>
                <p>Alternate Phone Number</p>
                <input
                  type="text"
                  name="alterph"
                  placeholder="Your Alternate Phone Number"
                />
                </li>
                <li>
                <p>Country</p>
                <input
                  type="text"
                  name="country"
                  placeholder="Your Country"
                  required
                />
                </li>
                <li>
                <p>State</p>
                <input
                  type="text"
                  name="state"
                  placeholder="Your State"
                  required
                />
                </li>
                <li>
                <p>City</p>
                <input
                  type="text"
                  name="city"
                  placeholder="Your City"
                  required
                />
                </li>
                <button className="save" type="submit">
                  Save and Next
                </button>
              </ul>
            </form>
            <form className="eduinfo">
            <p className="edu-para">Educational Information</p>
            <ul className="input-edu">
              <li>
              <p>Stream/Domain</p>
              <input
                type="text"
                name="stream"
                placeholder="Your Stream/Domain"
                required
              />
              </li>
              <li>
              <p>Institution</p>
              <input
                type="text"
                name="institution"
                placeholder="Your Institution"
                required
              />
              </li>
              <li>
              <p>Year of Graduation</p>
              <input
                type="text"
                name="grad"
                placeholder="Your Year of Graduation"
                required
              />
              </li>
              <button className="save" type="submit">
                  Save and Next
                </button>
              </ul>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}

export default Register;
