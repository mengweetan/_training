import logo from './download.jpg';
import './App.css';
import Login from './login.js';
import Viz from './Viz.js';
import { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);

  useEffect(() => {
  document.title = `visualisation exercise`;

},);

  return (
    <div className="App">
      <header className="App-header">

      <br/>
      <br/>
      <Viz />
      <br/>
      <br/>
        <img src={logo} className="App-logo" alt="logo" />

        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn Python - but why are we doing React?
        </a>
        <br/>
        <br/>
        <p>LOGIN</p>
        <Login />
      </header>

    </div>

  );
}

export default App;
