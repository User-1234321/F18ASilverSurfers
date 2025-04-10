import { useState } from 'react';
import Header from '../layout/Header';

function Order() {
  const [orderId, setOrderId] = useState('');
  const [despatchType, setDespatchType] = useState('Delivery');
  const [fulfillment, setFulfillment] = useState('Full');
  const [note, setNote] = useState('');
  const today = new Date().toISOString().split('T')[0];
  const [issueDate, setIssueDate] = useState(today);
  const [quantity, setQuantity] = useState(0);
  const [backorder, setBackorder] = useState('None');
  const [reason, setReason] = useState('');

  const [loading, setLoading] = useState(false);
  const [responseXml, setResponseXml] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponseXml(null);
    setError(null);

    const despatchData = {
      note,
      despatch_advice_type: despatchType,
      fulfillment,
      issue_date: issueDate,
      quantity,
      backorder,
      reason
    };

    try {
      const response = await fetch(`https://f18asilversurfers.onrender.com/despatch-advice/${orderId}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(despatchData)
      });

      if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.detail || 'Unknown error occurred');
      } else {
        const xml = await response.text();
        setResponseXml(xml);
      }
    } catch (err) {
      setError("Failed to connect: " + err.message);
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <Header />
      <p>This is the Order Page</p>
      <form className="form-container" onSubmit={handleSubmit}>
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

        <label htmlFor="note">Note:</label>
        <input
          type="text"
          id="note"
          value={note}
          onChange={(e) => setNote(e.target.value)}
          placeholder="Enter a note (optional)"
        />

        <label htmlFor="issueDate">Issue Date:</label>
        <input
          type="date"
          id="issueDate"
          value={issueDate}
          onChange={(e) => setIssueDate(e.target.value)}
        />

        <label htmlFor="quantity">Quantity:</label>
        <input
          type="number"
          id="quantity"
          value={quantity}
          onChange={(e) => setQuantity(Number(e.target.value))}
          min="1"
        />

        <label htmlFor="backorder">Backorder:</label>
        <select
          id="backorder"
          value={backorder}
          onChange={(e) => setBackorder(e.target.value)}
        >
          <option value="No">No</option>          
          <option value="Yes">Yes</option>
        </select>

        <label htmlFor="reason">Reason:</label>
        <input
          type="text"
          id="reason"
          value={reason}
          onChange={(e) => setReason(e.target.value)}
          placeholder="Enter a reason"
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Generating..." : "Submit"}
        </button>
      </form>

      {responseXml && (
        <div style={{ marginTop: '1rem', whiteSpace: 'pre-wrap' }}>
          <h3>Response XML:</h3>
          <code>{responseXml}</code>
        </div>
      )}

      {error && (
        <div style={{ color: 'red', marginTop: '1rem' }}>
          <strong>Error:</strong> {error}
        </div>
      )}
    </div>
  );
}

export default Order;