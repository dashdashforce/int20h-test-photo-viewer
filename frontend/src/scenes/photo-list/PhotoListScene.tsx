import * as React from 'react';
import {RouteComponentProps} from '@reach/router';
import {Query} from 'react-apollo';
import gql from 'graphql-tag';
import ContentContainer from '../../components/content-container/ContentContainer';
import Loader from '../../components/loader/Loader';
import PhotoPreview, {Photo} from '../../components/photo-preview/PhotoPreview';
import Grid from '../../components/grid/Grid';
import GridItem from '../../components/grid/GridItem';

export interface PhotoListSceneProps extends RouteComponentProps {}

const PHOTO_LIST = gql`
  {
    photos {
      title
      id
      sizes {
        medium {
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
    }
  }
`;

const PhotoListScene: React.SFC<PhotoListSceneProps> = () => {
  return (
    <ContentContainer>
      <h2>Photo list</h2>
      <Query query={PHOTO_LIST}>
        {({loading, error, data}) => {
          if (loading) return <Loader />;
          if (error) return <p>Error :( {error}</p>;

          return (
            <Grid>
              {data.photos.map((photo: Photo) => (
                <GridItem>
                  <PhotoPreview photo={photo} />
                </GridItem>
              ))}
            </Grid>
          );
        }}
      </Query>
    </ContentContainer>
  );
};

export default PhotoListScene;
