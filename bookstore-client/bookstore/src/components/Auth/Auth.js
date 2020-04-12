import React from "react";
import "./Auth.css";
import { Redirect } from "react-router-dom";

class Auth extends React.Component {
  constructor() {
    super();
    this.state = {
      email: "",
      password: "",
      redirectToHome: localStorage.getItem("token") !== null ? true : false,
    };
  }

  getAuthInfo = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  authenticate = (e) => {
    e.preventDefault();
    const requestOptions = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: this.state.email,
        password: this.state.password,
      }),
    };

    fetch("http://localhost:8080/api/login", requestOptions)
      .then(async (response) => {
        const data = await response.json();

        if (!response.ok) {
          const error = (data && data.message) || response.status;
          return Promise.reject(error);
        }

        localStorage.setItem("token", data.accessToken);
        this.setState({
          redirectToHome: true,
        });
      })
      .catch((error) => {
        this.setState({ errorMessage: error });
        console.error("There was an error!", error);
      });
  };

  render() {
    // const history = useHistory();
    const { email, password, redirectToHome } = this.state;

    return redirectToHome ? (
      <Redirect to="/effect/home" />
    ) : (
      <div className="landingPageBg">
        <div className="outer">
          <div className="middle">
            <div className="inner">
              <div className="columns">
                <div className="column is-offset-1 is-10">
                  <nav className="panel">
                    <form onSubmit={this.authenticate}>
                      <div className="field">
                        <p className="control has-icons-left has-icons-right">
                          <input
                            className="input"
                            type="email"
                            placeholder="Email"
                            name="email"
                            value={email}
                            onChange={this.getAuthInfo}
                          />
                          <span className="icon is-small is-left">
                            <i className="fas fa-envelope"></i>
                          </span>
                          <span className="icon is-small is-right">
                            <i className="fas fa-check"></i>
                          </span>
                        </p>
                      </div>
                      <div className="field">
                        <p className="control has-icons-left">
                          <input
                            className="input"
                            type="password"
                            placeholder="Password"
                            name="password"
                            value={password}
                            onChange={this.getAuthInfo}
                          />
                          <span className="icon is-small is-left">
                            <i className="fas fa-lock"></i>
                          </span>
                        </p>
                      </div>

                      <div className="columns is-mobile">
                        <div className="column is-half is-offset-one-quarter">
                          <button className="button is-link is-medium is-fullwidth  is-inverted">
                            Sign In
                          </button>
                        </div>
                      </div>
                    </form>
                  </nav>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Auth;
