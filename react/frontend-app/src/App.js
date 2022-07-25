import logo from './download.jpg';
import './App.css';
import Login from './login.js';

function App() {
  return (
    <div className="App">
      <header className="App-header">
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
