import "./App.css";
import logo from "./assets/logo.png";
import phone from "./images/phone.png";
import samsunga from "./images/samsunga.png";
import iphone from "./images/iphone.png";
import xiaomi from "./images/xiaomi.png";
import kayfot from "./images/samsungs25.png";

function App() {
  return (
    <>
      <header className="header">
        <div className="container">
          <div className="header_wrap">
            <img
              className="header_logo"
              src={logo}
              alt="Sampowskiy-mobile logo"
            />

            <div className="search_wrap">
              <input
                className="header_input"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />

              <button className="header_button" type="button">
                🔍
              </button>
            </div>

            <div className="header_number">+888 75 987 2792</div>

            <nav className="header_nav">
              <a href="http://localhost:8000/api/news/">News</a>
              <a href="http://localhost:8000/api/phones/">Phones</a>
              <a href="http://localhost:8000/api/reviews/">Reviews</a>
              <a href="http://localhost:8000/api/brands/">Brands</a>
            </nav>
          </div>
        </div>
      </header>

      <main className="main">
        <section className="hero">
          <div className="hero_content">
            <div className="hero_text">
              <p className="hero_brand">SAMSUNG</p>

              <h1>Galaxy A Series</h1>

              <p className="hero_description">
                Новый смартфон для учебы, игр и общения
              </p>

              <button className="hero_button">
                Подробнее
              </button>
            </div>

            <div className="hero_phone">
              <img src={phone} alt="" />
            </div>
          </div>
        </section>

        <section className="categories">
          <div className="category">
            <span>💻</span>
            <p>Computers</p>
          </div>

          <div className="category">
            <span>🎧</span>
            <p>Headphones</p>
          </div>

          <div className="category">
            <span>⌚</span>
            <p>Smart Watches</p>
          </div>

          <div className="category">
            <span>🎮</span>
            <p>Gaming</p>
          </div>

          <div className="category">
            <span>📷</span>
            <p>Cameras</p>
          </div>

          <div className="category">
            <span>📱</span>
            <p>Phones</p>
          </div>
        </section>

        <section className="products">
          <div className="products_title">
            <h2>Phones</h2>

            <a href="/phones">
              View all →
            </a>
          </div>

          <div className="product_grid">
            <article className="product_card">
              <div className="product_image">
                <img src={samsunga} alt="" height={150} width={130} />
              </div>

              <h3>Samsung Galaxy A56</h3>

              <p className="product_storage">
                8GB / 256GB
              </p>

              <p className="product_price">
                189 900 ֏
              </p>

              <button>Add to cart</button>
            </article>

            <article className="product_card">
              <div className="product_image"><img src={iphone} alt="Phone image" height={150} width={130} /></div>

              <h3>iPhone 16</h3>

              <p className="product_storage">
                128GB
              </p>

              <p className="product_price">
                349 900 ֏
              </p>

              <button>Add to cart</button>
            </article>

            <article className="product_card">
              <div className="product_image"><img src={kayfot} alt="" height={150} width={130} /></div>

              <h3>Samsung Galaxy S25</h3>

              <p className="product_storage">
                12GB / 256GB
              </p>

              <p className="product_price">
                399 900 ֏
              </p>

              <button>Add to cart</button>
            </article>

            <article className="product_card">
              <div className="product_image"><img src={xiaomi} alt="" height={150} width={130} /></div>

              <h3>Xiaomi Redmi Note</h3>

              <p className="product_storage">
                8GB / 256GB
              </p>

              <p className="product_price">
                129 900 ֏
              </p>

              <button>Add to cart</button>
            </article>
          </div>
        </section>
      </main>
    </>
  );
}

export default App;