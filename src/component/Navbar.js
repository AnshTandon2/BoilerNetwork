import { Nav, NavLogo, NavLink, Bars, NavMenu } from "../NavbarElements";

const NavComponent = () => {
  // Light tan color
  const lightTan = "#F5DEB3";

  return (
    <>
      <Nav
        style={{ background: `linear-gradient(to right, black, ${lightTan})` }}
      >
        <NavLogo to="/">Boiler Network</NavLogo>

        <NavMenu>
          <NavLink to="/" activeStyle={{ color: "black" }}>
            Home
          </NavLink>
          <NavLink to="/pumpkins" activeStyle={{ color: "black" }}>
            Sign In
          </NavLink>
          <NavLink to="/game" activeStyle={{ color: "black" }}>
            Platform
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};

export default NavComponent;
