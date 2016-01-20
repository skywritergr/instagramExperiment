import React from 'react'
import { Router, Route, Link, browserHistory } from 'react-router'
import App from './app'
import HandleAuth from './handle_auth'
import NoMatch from './nomatch'

ReactDOM.render((
  <Router history={browserHistory}>
    <Route path="/" component={App}>
        <Route path="handle_auth" component={HandleAuth}/>
        <Route path="*" component={NoMatch}/>
    </Route>
  </Router>)
  , document.getElementById('content'));