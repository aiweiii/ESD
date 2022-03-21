import Image from "../nillkin-case.webp";
import { Link, BrowserRouter as Router, Route } from "react-router-dom";
import ProductDetail from "../products/detail/ProductDetail";

function FeatureProduct(props) {
  const {name, id, data} = props

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
          <h5 className="card-title text-center">{name}</h5>
          <p className="card-text text-center text-muted">$ {id}</p>
          <div className="d-grid gap-2">
            <Router>
              <Route path="/products/:id">
                <ProductDetail data={data} />
              </Route>
            </Router>

            <Link to={`/products/${id}`} className="btn btn-outline-dark" replace>Details</Link>

          </div>
        </div>
      </div>
    </div>
  );
}

export default FeatureProduct;
