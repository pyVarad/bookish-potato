import React from "react";
import Header from "../Header/Header";
import Footer from "../Footer/Footer";
import { useParams } from "react-router-dom";

const Layout = () => {
  const { slug } = useParams();

  return (
    <div>
      <Header />
      <p>I am fron slug {slug}</p>
      <Footer />
    </div>
  );
};

export default Layout;
