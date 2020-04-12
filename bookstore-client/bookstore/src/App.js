import React from "react";
import "./App.scss";
import Auth from "./components/Auth/Auth";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Layout from "./components/Common/Layout/Layout";

function App() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={Auth}></Route>
        <Route path="/effect/:slug">
          <Layout />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
