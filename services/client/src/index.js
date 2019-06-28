import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

import AddUser from './components/AddUser';
import UsersList from './components/UsersList';
import AddDoctor from './components/AddDoctor';
import DoctorsList from './components/DoctorsList';


class App extends Component {
  // nuevo
  constructor() {
    super();
    // nuevo
    this.state = {
      users: [],
      doctors: []
    };
  };
  // nuevo
  componentDidMount() {
    this.getUsers();
    this.getDoctors();
  };

  getUsers() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)  // nuevo http://localhost:5001
    .then((res) => { this.setState({ users: res.data.data.users }); })
    .catch((err) => { console.log(err); });
  };

  addUser(event) {
    event.preventDefault();
    console.log('sanity check!');
  };
  getDoctors() {
    axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/doctors`)  // nuevo http://localhost:5001
    .then((res) => { this.setState({ doctors: res.data.data.doctors }); })
    .catch((err) => { console.log(err); });
  };

  addDoctor(event) {
    event.preventDefault();
    console.log('sanity check!');
  };

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns">
            <div className="column is-half">
              <br/>
              <h1 className="title is-1">Todos los usuarios</h1>
              <hr/><br/>
              <AddDoctor addDoctor={this.addDoctor}/>
              <br/><br/>
              <DoctorsList doctors={this.state.doctors}/>
            </div>
          </div>
        </div>
      </section>
    )
  }
};


ReactDOM.render(<App />, document.getElementById('root'));
