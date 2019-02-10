import * as React from 'react';
import cn from 'classnames';

import * as routes from '../../routes';
import {Link} from '@reach/router';

import styles from './PhotoPreview.module.css';

export type Rect = {
  top: number;
  left: number;
  width: number;
  height: number;
};

export type Emotion = {
  title: string;
  factor: number;
};

export type Face = {
  faceRectangle: Rect;
  emotion: Emotion;
};

export type Photo = {
  id: number;
  title: string;
  sizes: {
    medium: {
      url: string;
      width: number;
      height: number;
    };
  };
  faces: Face[];
};

export interface PhotoPreviewProps {
  photo: Photo;
}

const PhotoPreview: React.SFC<PhotoPreviewProps> = ({photo}) => {
  const noFaces = !photo.faces.length;
  return (
    <Link
      className={cn(styles.block, {[styles.blockBlur]: noFaces})}
      to={routes.photo.getUrl({id: photo.id})}
    >
      <img className={styles.photo} src={photo.sizes.medium.url} />
      {noFaces && <div className={styles.noPhotoCaption}>No faces</div>}
    </Link>
  );
};

export default PhotoPreview;
