import * as React from 'react';
import styles from './PhotoWithFaces.module.css';
import {Face, Rect} from '../photo-preview/PhotoPreview';
import {distanceInWordsToNow} from 'date-fns';
import pluralize from 'pluralize';

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
  uploadDate: string;
  views: number;
  tags: string[];
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
    <>
      <div className={styles.layout}>
        <div className={styles.leftCol}>
          <div className={styles.root}>
            <img className={styles.photo} src={photo.sizes.large.url} />
            {photo.faces.map((face) => {
              const rect = calculateRect(
                face.faceRectangle,
                640 / photo.sizes.large.width,
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
        </div>

        <div className={styles.rightCol}>
          <h2>
            {photo.title} ({photo.faces.length}{' '}
            {pluralize('faces', photo.faces.length)})
          </h2>
          <h4>Uploaded {distanceInWordsToNow(photo.uploadDate)} ago</h4>
          <h5>
            {photo.tags.map((tag) => (
              <>
                <span>#{tag}</span>{' '}
              </>
            ))}
          </h5>
        </div>
      </div>
    </>
  );
};

export default PhotoWithFaces;
