import "../styles/Header.css";

import logo from '../assets/LogoTrans.png'

function Header() {

    return (
      <div className="Header" id="Header">
        <div className="header-container">
          <div className="header-blue-rectangle">
            <img alt={"logo"} src={logo} height={75} width={210} />
          </div>
        </div>
      </div>
    );
}

export default Header;