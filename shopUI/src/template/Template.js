import Header from "./Header";
import Content from "./Content";
import Footer from "./Footer";

import React, { useState, useEffect } from "react";
import CustomizedSnackbars from "../products/detail/SnackBar";

function Template(props) {

  return (
    <>
      <Header/>
      <Content> {props.children} </Content>
      <Footer />
    </>
  );
}

export default Template;
