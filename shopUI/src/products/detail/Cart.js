import React, { useState, useEffect } from "react";
import Image from "../../nillkin-case.webp";
import "./cart.css";



const Cart = ({ cart, setCart, handleChange }) => {
    const [price, setPrice] = useState(0);

    const handleRemove = (id) => {
        const arr = cart.filter((item) => item.id !== id);
        setCart(arr);
        handlePrice();
    };

    const handlePrice = () => {
        let ans = 0;
        cart.map((item) => (ans += item.quantity * item.itemPrice));
        setPrice(ans);
    };

    useEffect(() => {
        handlePrice();
    });

    return (
        <article>
        {cart.map((item) => (
            <div className="cart_box" key={item.id}>
            <div className="cart_img">
                <img src={Image} alt="item image here" />
                <p>{item.productName}</p>
            </div>
            <div>
                <button onClick={() => handleChange(item, 1)}>+</button>
                <button>{item.quantity}</button>
                <button onClick={() => handleChange(item, -1)}>-</button>
            </div>
            <div>
                <span>{item.itemPrice}</span>
                <button onClick={() => handleRemove(item.id)}>Remove</button>
            </div>
            </div>
        ))}
        <div className="total">
            <span>Total Price of your Cart</span>
            <span>SGD {price}</span>
        </div>
        </article>
    );
};

export default Cart;
