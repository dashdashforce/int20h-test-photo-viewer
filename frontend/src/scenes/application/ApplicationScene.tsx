import * as React from 'react';
import Header from '../../components/header/Header';
import PhotoListScene from '../photo-list/PhotoListScene';
import {Router, Redirect} from '@reach/router';
import PhotoScene from '../photo/PhotoScene';
import ApplicationLayout from '../../components/application-layout/ApplicationLayout';

import * as routes from '../../routes';

export interface ApplicationSceneProps {}

const ApplicationScene: React.SFC<ApplicationSceneProps> = () => {
  return (
    <ApplicationLayout>
      <Router>
        <Redirect from="/" to="photo-viewer" noThrow />
        <PhotoListScene path={routes.photoList.path} />
        <PhotoScene path={routes.photo.path} />
      </Router>
    </ApplicationLayout>
  );
};

export default ApplicationScene;
