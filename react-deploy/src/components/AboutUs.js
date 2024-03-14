import "../styles/aboutus.css";
import Header from "./Header.js";
import React, { useEffect } from "react";

function AboutUs() {
  useEffect(() => {
    return () => {
      document.title = "About Us";
    };
  }, []);

  return (
    <>
      <div className="AboutUs" id="AboutUs">
        <div className="aboutus-container">
          <Header />
          <div className="content">
            <h1>ABOUT US</h1>
            <p>Welcome to HireMeHorizon, your personalized career compass!</p>
            <h3>Our Mission</h3>
            <p>Empowering Futures, One Placement at a Time</p>
            <p>
              At HireMeHorizon, we're on a mission to simplify the career
              journey for students. Using cutting-edge Machine Learning models,
              we predict placement opportunities and estimate salaries to guide
              students towards success.
            </p>
            <h3>What Sets Us Apart</h3>
            <ul>
              <li>
                Data-Driven Precision: Our algorithms analyze diverse factors
                for accurate, personalized predictions.
              </li>
              <li>
                Transparency: We believe in openness about our methods, ensuring
                trust in the insights we provide.
              </li>
            </ul>
            <h3>Join Us!</h3>
            <p>
              Whether you're a student or an employer, join us in shaping a
              future where every student steps confidently into the professional
              world. Discover your horizon with HireMeHorizon!
            </p>
            <h3>Meet the Team</h3>
            <p>
              Our team is a blend of seasoned professionals, technologists, and
              data scientists dedicated to revolutionizing how students approach
              their careers.
            </p>
          </div>
        </div>
      </div>
    </>
  );
}

export default AboutUs;
