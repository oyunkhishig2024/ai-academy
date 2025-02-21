import { Button, Card, FormControl, InputGroup } from "react-bootstrap";
import React, { useContext, useState } from "react";
import { CartContext } from "../App";


const ProductCard = ({ product }) => {
  const { state, dispatch } = useContext(CartContext);
  const [quantity, setQuantity] = useState(1);

  const handleAddToCart = () => {
    dispatch({ type: "ADD_TO_CART", payload: { ...product, quantity } });
    setQuantity(1); // Reset quantity after adding to cart
  };

  const handleQuantityChange = (amount) => {
    const newQuantity = quantity + amount;
    if (newQuantity > 0) {
      setQuantity(newQuantity);
    }
  };

  return (
    <Card className="product-card">
      <Card.Img
        variant="top"
        src={product.thumbnail}
        className="product-img"
      />
      <Card.Body className="product-body">
        <Card.Title className="product-title">{product.title}</Card.Title>
        <Card.Text className="product-price">${product.price}</Card.Text>
        <InputGroup className="mb-3 quantity-group">
          <Button
            variant="outline-secondary"
            onClick={() => handleQuantityChange(-1)}
          >
            -
          </Button>
          <FormControl
            value={quantity}
            readOnly
            className="quantity-input"
          />
          <Button
            variant="outline-secondary"
            onClick={() => handleQuantityChange(1)}
          >
            +
          </Button>
        </InputGroup>
        <Button
          variant="primary"
          onClick={handleAddToCart}
          className="add-to-cart-btn" // Apply custom CSS class
        >
          Add to Cart
        </Button>
      </Card.Body>
    </Card>
  );
};

export default ProductCard;
