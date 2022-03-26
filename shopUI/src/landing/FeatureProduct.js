import Image from "../nillkin-case.webp";
import { Link, BrowserRouter as Router, Route, Switch } from "react-router-dom";
import ProductDetail from "../products/detail/ProductDetail";

function FeatureProduct({item}) {
  console.log("item",item)

  return (
    <div className="col">
      <div className="card shadow-sm">
        <img
          className="card-img-top bg-dark cover"
          height="240"
          alt=""
          src={Image}
        />
        <div className="card-body">
          <h5 className="card-title text-center">{item.productName}</h5>
          <p className="card-text text-center text-muted">$ {item.itemPrice}</p>
          <div className="d-grid gap-2">
            <Switch>
              <Route path="/products/:id">
                <ProductDetail sth={1} />
              </Route>
            </Switch>

            <Link to={`/products/${item.id}`} className="btn btn-outline-dark" replace>Details</Link>
            {/* I think the problem is within the ROUTE and LINK!!! */}

          </div>
        </div>
      </div>
    </div>
  );
}

export default FeatureProduct;
