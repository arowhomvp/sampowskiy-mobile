import './App.css';
import logo from './assets/logo.png';

function App() {
  return (
    <header className="header">
      <div className="container">
        <div className="header_wrap">
          <img className="header_logo" src={logo} alt="Sampowskiy-mobile logo" />
          <input className="header_input" type="search" placeholder="Search" aria-label="Search"/>
          <button className='header_button' type="button">Enter</button>
          <div className="header_number">+888 75 987 2792</div>
          <nav className="header_nav">
              <a href="/news">News</a>
              <a href="/phones">Phones</a>
              <a href="/reviews">Reviews</a>
              <a href="/brands">Brands</a>
          </nav>
        </div>
      </div>
    </header>
  );
}

export default App;