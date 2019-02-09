import * as React from 'react';
import {RouteComponentProps} from '@reach/router';

export interface PhotoSceneProps extends RouteComponentProps {
  id?: Number;
}

const PhotoScene: React.SFC<PhotoSceneProps> = ({id}) => {
  return <h2>Photo scene {id}</h2>;
};

export default PhotoScene;
