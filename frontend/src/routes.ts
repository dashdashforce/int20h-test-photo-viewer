function Location<T>(path: string, getUrl?: (parameters: T) => string) {
  return {
    path,
    getUrl(parameters: T): string {
      if (!getUrl) {
        return path;
      }
      return getUrl(parameters);
    },
  };
}

export const photoList = Location('/photo-viewer');

export interface PhotoLocationParameters {
  id: string;
}

export const photo = Location(
  '/photo-viewer/photo/:id',
  ({id}: PhotoLocationParameters) => `/photo-viewer/photo/${id}`,
);
