import * as React from 'react';
import styles from './PhotoWithFaces.module.css';
import {Face, Rect} from '../photo-preview/PhotoPreview';

export type FullPhoto = {
  id: string;
  title: string;
  sizes: {
    large: {
      url: string;
      width: number;
      height: number;
    };
  };
  faces: Face[];
};

export interface PhotoWithFacesProps {
  photo: FullPhoto;
}

const calculateRect = (rect: Rect, ratio: number): Rect => {
  return {
    top: rect.top * ratio,
    left: rect.left * ratio,
    width: rect.width * ratio,
    height: rect.height * ratio,
  };
};

const PhotoWithFaces: React.SFC<PhotoWithFacesProps> = ({photo}) => {
  return (
    <div className={styles.root}>
      <img className={styles.photo} src={photo.sizes.large.url} />
      {photo.faces.map((face) => {
        const rect = calculateRect(
          face.faceRectangle,
          840 / photo.sizes.large.width,
        );
        const emotions = face.emotion
          .filter((emotion) => emotion.factor >= 30)
          .sort((a, b) => b.factor - a.factor);
        return (
          <div
            className={styles.face}
            style={{
              top: `${rect.top}px`,
              left: `${rect.left}px`,
              width: `${rect.width}px`,
              height: `${rect.height}px`,
            }}
          >
            <div className={styles.emotionList}>
              {emotions.map((emotion) => (
                <div
                  className={styles.emotion}
                  style={{opacity: (emotion.factor + 20) / 100}}
                >
                  {emotion.title}
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default PhotoWithFaces;
