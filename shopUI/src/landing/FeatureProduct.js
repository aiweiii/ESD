// import Image from "../nillkin-case.webp";
import { Link, BrowserRouter as Router, Route, Switch } from "react-router-dom";
import ProductDetail from "../products/detail/ProductDetail";
import { requirePropFactory } from "@mui/material";


function FeatureProduct({item, doClick}) {

  console.log("sellerid:",item.sellerId)
  console.log("itemid:",item.id)

  return (
    <div className="col">
      <div className="card shadow-sm">
        <img
          className="card-img-top bg-dark cover"
          height="240"
          alt=""
          // src={require(`./${item.id}-1.jpeg`)}
          src={item.productName}
          // src={Image}
        />
        <div className="card-body">
          <h5 className="card-title text-center">{item.productName}</h5>
          <p className="card-text text-center text-muted">$ {item.itemPrice}</p>
          <div className="d-grid gap-2">

            <Link to={`/products/${item.id}`} className="btn btn-outline-dark" replace >Details</Link>
            <button onClick={() => doClick(item)} className="btn btn-outline-dark" replace >Add to Cart</button>

            {/* I think the problem is within the ROUTE and LINK!!! */}

            <Switch>
              <Route exact path="/products/:id" component={ProductDetail}>
              </Route>
            </Switch>

          </div>
        </div>
      </div>
    </div>
  );
}

export default FeatureProduct;
