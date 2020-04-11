import React from "react";
import "./Auth.css";

const Auth = () => {
  return (
    <div className="outer">
      <div className="middle">
        <div className="inner">
          <div className="columns">
            <div className="column is-offset-1 is-10">
              <nav className="panel">
                {/* <div className="field">
                  <label className="label">Email</label>
                  <div className="control">
                    <input
                      className="input"
                      type="text"
                      placeholder="email@domain.com"
                    />
                  </div>
                </div>

                <div className="field">
                  <label className="label">Password</label>
                  <div className="control">
                    <input
                      className="input"
                      type="password"
                      placeholder="Password"
                    />
                  </div>
                </div> */}

                <div className="field">
                  <p className="control has-icons-left has-icons-right">
                    <input className="input" type="email" placeholder="Email" />
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
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Auth;
