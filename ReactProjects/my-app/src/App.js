import "bootstrap/dist/css/bootstrap.min.css";
import "./App.css";

import { Col, Container, Row } from "react-bootstrap";
import React, { createContext, useReducer } from "react";

import CartList from "./components/CartList";
import ProductList from "./components/ProductList";

const CartContext = createContext();

const cartReducer = (state, action) => {
  switch (action.type) {
    case "ADD_TO_CART":
      const existingItem = state.cart.find(
        (item) => item.id === action.payload.id
      );
      if (existingItem) {
        return {
          ...state,
          cart: state.cart.map((item) =>
            item.id === action.payload.id
              ? { ...item, quantity: item.quantity + action.payload.quantity }
              : item
          ),
        };
      } else {
        return { ...state, cart: [...state.cart, action.payload] };
      }
    case "UPDATE_QUANTITY":
      return {
        ...state,
        cart: state.cart.map((item) =>
          item.id === action.payload.id
            ? { ...item, quantity: action.payload.quantity }
            : item
        ),
      };
    case "REMOVE_FROM_CART":
      return {
        ...state,
        cart: state.cart.filter((item) => item.id !== action.payload),
      };
    case "CLEAR_CART": // New action to clear the cart
      return {
        ...state,
        cart: [],
      };
    default:
      return state;
  }
};

const App = () => {
  const [state, dispatch] = useReducer(cartReducer, {
    cart: [],
  });

  return (
    <CartContext.Provider value={{ state, dispatch }}>
      <Container fluid>
        <Row>
          <Col md={8} >
            <h2 id="topic-top">Product List</h2>
            <ProductList />
          </Col>
          <Col md={4}>
            <h2 id="topic-cart">in your cart: </h2>
            <CartList />
          </Col>
        </Row>
      </Container>
    </CartContext.Provider>
  );
};

export { CartContext };

export default App;