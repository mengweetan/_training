import React, {Component} from "react";
import axios from "axios";

export default class Login extends Component {
  constructor(props) {
    super(props);

    this.state = {
      token: null,
      id: null,
      pw: null
    };
  }

  handleChange_id = e => {
    console.log(e.target.value);
    this.setState({id: e.target.value});
  };

  handleChange_pw = e => {
    console.log(e.target.value);
    this.setState({pw: e.target.value});
  };

  submitform = () => {
    console.log(this.state);
    const data = this.state;


    axios.post("http://localhost:8000/app/login/", data).then(response => {


          if(response.data.token !== '')

          {

            console.log(response)
            this.setState({ token: response.data.token });

          }else{
              alert('Login Failed');
          }
      }).catch(error => {
          console.log(error);
          alert('Something went wrong');
        });







  }


    changeUserName = (e) => {

      var url =  "http://localhost:8000/app/change/";
      var change_data = {"name": "mary"};
      var  headers =  {
          "Authorization": "Token " + this.state.token,
          "Content-Type": "application/json"
        }
      console.log(headers)
      fetch(url, {
        method: "POST",
        withCredentials: true,
        headers: headers,
        body: JSON.stringify(change_data)
      })
        .then(response => {
          return response.json();
        })
        .then(res => {
          console.log(res.message);
        })
        .catch(error => {
          console.log(error);
        });
    }

  showtoken = () => {
    alert (this.state.token)
  }

  render() {
    return (
      <div>

        <input placeholder="id" onChange={e => this.handleChange_id(e)} />
        <br />
        <input placeholder="password" onChange={e => this.handleChange_pw(e)} />
        <br />
        <input type="submit" onClick={e => this.submitform()} />
        <br />
        <br />
        <input type="submit" onClick={e => this.showtoken()} value="token?" />

  <br />
        <input type="submit" onClick={e => this.changeUserName(e)}  />


      </div>
    );
  }
}
