import React from 'react';
import ReactDOM from 'react-dom';

import * as serviceWorker from './serviceWorker';

import ApplicationScene from './scenes/application/ApplicationScene';

import './assets/fonts/Muli.css';
import './index.css';

import ApolloClient from 'apollo-boost';
import {ApolloProvider} from 'react-apollo';

const client = new ApolloClient({
  uri: 'http://ddforce.nckcol.com/photo-viewer/api/graphql',
});

ReactDOM.render(
  <ApolloProvider client={client}>
    <ApplicationScene />
  </ApolloProvider>,
  document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();
