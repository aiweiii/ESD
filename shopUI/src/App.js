import Template from "./template/Template";
import ProductDetail from "./products/detail/ProductDetail";
import { Switch, Route } from "react-router-dom";
import Landing from "./landing/Landing";
import ProductList from "./products/ProductList";
import Cart from "./products/detail/Cart";

import React, { useState, useEffect } from "react";


function App() {

  // const [show, setShow] = useState(true);
  const [cart, setCart] = useState([]);

  const doClick = (item) => {
    if (cart.indexOf(item) !== -1) return;
    setCart([...cart, item]);
  };

  const handleChange = (item, d) => {
    const ind = cart.indexOf(item);
    const arr = cart;
    arr[ind].quantity += d

    if (arr[ind].quantity === 0) arr[ind].quantity = 1;
    setCart([...arr]);
  };

  return (
    <Template>
      <Switch>
        <Route path="/" exact>
          <Landing doClick={doClick}/>
        </Route>
        <Route path="/products/:slug">
          <ProductDetail/>
        </Route>
        <Route path="/cart" exact>
          <Cart cart={cart} setCart={setCart} handleChange={handleChange} />
        </Route>
        {/* <Route path="/products" exact>
          <ProductList />
        </Route> */}
      </Switch>
    </Template>
  );
}

export default App;
