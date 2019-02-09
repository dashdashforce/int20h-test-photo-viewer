import * as React from 'react';
import Header from '../../components/header/Header';
import PhotoListScene from '../photo-list/PhotoListScene';
import {Router} from '@reach/router';
import PhotoScene from '../photo/PhotoScene';
import ApplicationLayout from '../../components/application-layout/ApplicationLayout';

export interface ApplicationSceneProps {}

const ApplicationScene: React.SFC<ApplicationSceneProps> = () => {
  return (
    <ApplicationLayout>
      <Router>
        <PhotoListScene path="/" />
        <PhotoScene path="/photo/:id" />
      </Router>
    </ApplicationLayout>
  );
};

export default ApplicationScene;
