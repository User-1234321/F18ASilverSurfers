import { Link } from 'react-router-dom';
import { useState } from 'react';
import Header from '../layout/Header';

function Home() {
  const [inputValue, setInputValue] = useState('');
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(inputValue);
    setInputValue('');
  }

  return (
    <div className="App">
      <Header />

      <p>This is the Home page</p>
      hello world
      
      <form onSubmit={handleSubmit}>
        <input 
          type="text"
          placeholder="Enter info"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)} 
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Home;