import React from 'react'
import { Router, Route, Link } from 'react-router'
import createBrowserHistory from 'history/lib/createBrowserHistory'
import App from './app'
import HandleAuth from './handle_auth'
import NoMatch from './nomatch'

const browserHistory = createBrowserHistory()

ReactDOM.render((
  <Router history={browserHistory}>
    <Route path="/" component={App}>
        <Route path="handleauth" component={HandleAuth}/>
        <Route path="*" component={NoMatch}/>
    </Route>
  </Router>)
  , document.getElementById('content'));