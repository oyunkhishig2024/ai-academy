import { Button, FormControl, InputGroup, ListGroup } from "react-bootstrap";
import React, { useContext } from "react";

import { CartContext } from "../App";

const CartList = () => {
  const { state, dispatch } = useContext(CartContext);

  const handleQuantityChange = (id, amount) => {
    const cartItem = state.cart.find((item) => item.id === id);

    if (cartItem.quantity + amount > 0) {
      dispatch({
        type: "UPDATE_QUANTITY",
        payload: { id, quantity: cartItem.quantity + amount },
      });
    } else {
      dispatch({ type: "REMOVE_FROM_CART", payload: id });
    }
  };

  const handleClearCart = () => {
    dispatch({ type: "CLEAR_CART" });
  };

  // Calculate the total price
  const totalPrice = state.cart.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

  return (
    <div>
      <div className="d-flex justify-content-between align-items-center mb-3">
        <h5>Cart</h5>
        {state.cart.length > 0 && (
          <Button variant="danger" onClick={handleClearCart}>
            Clear Cart
          </Button>
        )}
      </div>
      <ListGroup>
        {state.cart.length === 0 ? (
          <ListGroup.Item>No items in the cart.</ListGroup.Item>
        ) : (
          state.cart.map((item) => (
            <ListGroup.Item key={item.id}>
              <div>
                <strong>{item.title}</strong> - ${item.price} x {item.quantity}{" "}
                = ${item.price * item.quantity}
              </div>
              <InputGroup>
                <Button
                  variant="outline-secondary"
                  onClick={() => handleQuantityChange(item.id, -1)}
                >
                  -
                </Button>
                <FormControl
                  value={item.quantity}
                  readOnly
                  style={{ width: "50px", textAlign: "center" }}
                />
                <Button
                  variant="outline-secondary"
                  onClick={() => handleQuantityChange(item.id, 1)}
                >
                  +
                </Button>
              </InputGroup>
            </ListGroup.Item>
          ))
        )}
      </ListGroup>
      {state.cart.length > 0 && (
        <div className="mt-3 text-end">
          <h5>Total: ${totalPrice.toFixed(2)}</h5>
        </div>
      )}
    </div>
  );
};

export default CartList;