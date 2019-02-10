import * as React from 'react';
import {RouteComponentProps} from '@reach/router';
import gql from 'graphql-tag';
import {Query} from 'react-apollo';
import Loader from '../../components/loader/Loader';
import PhotoWithFaces from '../../components/photo-with-faces/PhotoWithFaces';
import ContentContainer from '../../components/content-container/ContentContainer';
import EmotionButton from '../../components/emotion-button/EmotionButton';
import BackIcon from '../../components/emotion-button/BackIcon';
import {navigate} from '@reach/router';
import {photoList} from '../../routes';

export interface PhotoSceneProps extends RouteComponentProps {
  id?: Number;
}

const PHOTO_BY_ID = gql`
  query Photo($id: String) {
    photo(id: $id) {
      id
      title
      sizes {
        large {
          url
          width
          height
        }
      }
      faces {
        faceRectangle {
          top
          left
          width
          height
        }
        emotion {
          title
          factor
        }
      }
      uploadDate
      views
      tags
    }
  }
`;

const PhotoScene: React.SFC<PhotoSceneProps> = ({id}) => {
  return (
    <>
      <ContentContainer>
        <EmotionButton
          icon={<BackIcon />}
          caption="Go back"
          onClick={() => navigate(photoList.getUrl({}))}
        />

        <Query query={PHOTO_BY_ID} variables={{id}}>
          {({loading, error, data}) => {
            if (loading) return <Loader />;
            if (error) return <p>Error :(</p>;

            return <PhotoWithFaces photo={data.photo} />;
          }}
        </Query>
      </ContentContainer>
    </>
  );
};

export default PhotoScene;
