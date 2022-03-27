import * as React from 'react';
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Snackbar from '@mui/material/Snackbar';
import MuiAlert from '@mui/material/Alert';
import ProductDetail from './ProductDetail';

import axios from 'axios';
import { useEffect, useState } from "react";

const Alert = React.forwardRef(function Alert(props, ref) {
  return <MuiAlert elevation={6} ref={ref} variant="filled" {...props} />;
});

export default function CustomizedSnackbars({ id }) {

  const [items,setItem] = useState([])
  const [cart, setCart] = useState([]);
  const [open, setOpen] = React.useState(false);

  useEffect(() => {
    axios.get("http://127.0.0.1:9090/items")
    .then(res => {
      // console.log(res.data)
      setItem(res.data)
    })
    .catch(err => console.log(err))
  },[])

  const productName = items.filter((item) => item.id == id).map((item, index) => {
    return (
      item.productName
    )})

  const quantity = items.filter((item) => item.id == id).map((item, index) => {
    return (
      item.quantity
    )})


  const sellerId = items.filter((item) => item.id == id).map((item, index) => {
    return (
      item.sellerId
    )})

  const itemPrice = items.filter((item) => item.id == id).map((item, index) => {
    return (
      item.itemPrice
    )})

  // const description = items.filter((item) => data.id == id).map((item, index) => {
  //   return (
  //     item.description
  //   )})

  const item = {productName, quantity, sellerId, itemPrice, id}
  console.log("item from snackbar: ", item)

  const doClick = (item) => {
    if (cart.indexOf(item) !== -1) return;
    setCart([...cart, item]);
  };

  const handleClick = () => {
    setOpen(true);
  };

  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }

    setOpen(false);
  };

  return (
    <Stack spacing={2} sx={{ width: '100%' }}>
      <Button variant="outlined" onClick={() => {
          handleClick();
          doClick(item);
        }}>
        Add to cart
      </Button>
      <Snackbar open={open} autoHideDuration={3000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
          Added to Cart Successfully!
        </Alert>
      </Snackbar>
    </Stack>
  )
}
