import React, { useEffect } from "react";

function Home() {
    useEffect(() => {
        return () => {
          document.title = "HireMeHorizon";
        };
      }, []);
    return (
        <h1>HII</h1>
    );
}

export default Home;