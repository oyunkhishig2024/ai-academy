import { Col, Row } from "react-bootstrap";
import React, { useEffect, useState } from "react";
import ProductCard from "./ProductCard";


const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("https://dummyjson.com/products")
      .then((res) => res.json())
      .then((data) => setProducts(data.products));
  }, []);

  return (
    <Row className="product-list">
      {products.map((product) => (
        <Col key={product.id} md={4} className="mb-3 product-col">
          <ProductCard product={product} />
        </Col>
      ))}
    </Row>
  );
};

export default ProductList;
