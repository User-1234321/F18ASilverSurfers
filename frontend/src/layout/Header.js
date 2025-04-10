import { Link } from 'react-router-dom';

function Header() {
    return (
        <div className="navigation-container">
          <h3>Despatch Advice</h3>
          <Link to="/">Home</Link>
          <Link to="/order">Order</Link>
        </div>
    );
  }
  
  export default Header;  