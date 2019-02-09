import * as React from 'react';
import {RouteComponentProps} from '@reach/router';

export interface PhotoListSceneProps extends RouteComponentProps {}

const PhotoListScene: React.SFC<PhotoListSceneProps> = () => {
  return <h2>Photo list scene</h2>;
};

export default PhotoListScene;
