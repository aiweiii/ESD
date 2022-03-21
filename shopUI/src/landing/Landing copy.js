import Banner from "./Banner";
import FeatureProduct from "./FeatureProduct";
import ScrollToTopOnMount from "../template/ScrollToTopOnMount";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Link } from "react-router-dom";
import axios from 'axios'

function Landing() {

  // var config = {
  //   method: 'get',
  //   // url: 'http://localhost:7070/items',
  //   url: 'https:jsonplaceholder.typicode.com/todos',
  //   headers: { }
  // };

  // axios(config)
  // .then(function (response) {
  //   console.log(JSON.stringify(response.data));
  //   const todos = response.data;

  // })
  // .catch(function (error) {
  //   console.log(error);
  // });


  let data = [
    {
        "productName": "ORANGE",
        "quantity": 20,
        "price": 80,
        "sellerId": 1,
        "id": 1
    },
    {
        "productName": "PINEAPPLE",
        "quantity": 50,
        "price": 70,
        "sellerId": 1,
        "id": 2
    },
    {
        "productName": "APPLE",
        "quantity": 30,
        "price": 60,
        "sellerId": 2,
        "id": 3
    },
    {
        "productName": "STRAWBERRY",
        "quantity": 17,
        "price": 50,
        "sellerId": 2,
        "id": 4
    },
    {
        "productName": "BLUEBERRY",
        "quantity": 30,
        "price": 40,
        "sellerId": 2,
        "id": 5
    },
    {
        "productName": "WATERMELON",
        "quantity": 30,
        "price": 30,
        "sellerId": 2,
        "id": 6
    }
]
  return (
    <>
      <ScrollToTopOnMount />
      <Banner />
      <div className="d-flex flex-column bg-white py-4">
        <p className="text-center px-5">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </p>
        <div className="d-flex justify-content-center">
          <Link to="/products" className="btn btn-primary" replace>
            Browse products
          </Link>
        </div>
      </div>
      <h2 className="text-muted text-center mt-4 mb-3">New Arrival</h2>
      <div className="container pb-5 px-lg-5">
        <div className="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4 px-md-5">
          <FeatureProduct />
        </div>
      </div>
      <div className="d-flex flex-column bg-white py-4">
        <h5 className="text-center mb-3">Follow us on</h5>
        <div className="d-flex justify-content-center">
          <a href="!#" className="me-3">
            <FontAwesomeIcon icon={["fab", "facebook"]} size="2x" />
          </a>
          <a href="!#">
            <FontAwesomeIcon icon={["fab", "instagram"]} size="2x" />
          </a>
          <a href="!#" className="ms-3">
            <FontAwesomeIcon icon={["fab", "twitter"]} size="2x" />
          </a>
        </div>
      </div>
    </>
  );
}

export default Landing;
