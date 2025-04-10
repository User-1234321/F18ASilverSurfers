import { Link } from 'react-router-dom';
import { useState } from 'react';
import Header from '../layout/Header';

function Order() {
  const [orderId, setOrderId] = useState('');
  const [despatchType, setDespatchType] = useState('Delivery');
  const [fulfillment, setFulfillment] = useState('Full');

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = {
      orderId,
      despatchType,
      fulfillment,
    };
    
    console.log("Form Submitted:", formData);
    setOrderId('');
    setDespatchType('Delivery');
    setFulfillment('Full');
  };

    return (
      <div className="App">
        <Header />
        <p>This is the Order Page</p>
        <form onSubmit={handleSubmit}>
        <label htmlFor="orderId">Order ID:</label>
        <input
          type="text"
          id="orderId"
          value={orderId}
          onChange={(e) => setOrderId(e.target.value)}
          required
        />

        <label htmlFor="despatchType">Despatch Advice Type:</label>
        <select
          id="despatchType"
          value={despatchType}
          onChange={(e) => setDespatchType(e.target.value)}
        >
          <option value="Delivery">Delivery</option>
          <option value="Return">Return</option>
          <option value="Cancel">Cancel</option>
        </select>

        <label htmlFor="fulfillment">Fulfillment:</label>
        <select
          id="fulfillment"
          value={fulfillment}
          onChange={(e) => setFulfillment(e.target.value)}
        >
          <option value="Full">Full</option>
          <option value="Partial">Partial</option>
        </select>

        <button type="submit">Submit</button>
      </form>
      </div>
    );
  }
  
  export default Order;