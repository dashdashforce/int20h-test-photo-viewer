import * as React from 'react';
import {RouteComponentProps} from '@reach/router';
import {Query} from 'react-apollo';
import gql from 'graphql-tag';
import ContentContainer from '../../components/content-container/ContentContainer';
import Loader from '../../components/loader/Loader';
import PhotoPreview, {Photo} from '../../components/photo-preview/PhotoPreview';
import Grid from '../../components/grid/Grid';
import GridItem from '../../components/grid/GridItem';
import EmotionFilter from '../../components/emotion-filter/EmotionFilter';
import EmotionButton from '../../components/emotion-button/EmotionButton';

export interface PhotoListSceneProps extends RouteComponentProps {}

const PHOTO_LIST = gql`
  query Photos($first: Int, $after: String, $emotions: [String]) {
    photos(filters: $emotions, first: $first, after: $after) {
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
  const [emotion, setEmotion] = React.useState<string | null>(null);

  return (
    <ContentContainer>
      <h2>Photo list</h2>
      <div style={{marginBottom: '24px'}}>
        <EmotionFilter
          current={emotion}
          onChange={(emotion) => setEmotion(emotion)}
        />
      </div>
      <Query
        query={PHOTO_LIST}
        variables={{emotions: emotion ? [emotion] : [], first: 20, after: null}}
      >
        {({loading, error, data, fetchMore}) => {
          if (loading) return <Loader />;
          if (error) return <p>Error :( {error}</p>;

          const lastId = data.photos[data.photos.length - 1].id;

          return (
            <>
              <Grid>
                {data.photos.map((photo: Photo) => (
                  <GridItem>
                    <PhotoPreview photo={photo} />
                  </GridItem>
                ))}
              </Grid>

              <p>
                <EmotionButton
                  caption="Load more"
                  onClick={() =>
                    fetchMore({
                      variables: {
                        after: lastId,
                      },
                      updateQuery: (prev, {fetchMoreResult}) => {
                        if (!fetchMoreResult) return prev;
                        return Object.assign({}, prev, {
                          photos: [...prev.photos, ...fetchMoreResult.photos],
                        });
                      },
                    })
                  }
                />
              </p>
            </>
          );
        }}
      </Query>
    </ContentContainer>
  );
};

export default PhotoListScene;
