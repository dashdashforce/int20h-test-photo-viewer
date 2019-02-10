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

export const photoList = Location('/');

export interface PhotoLocationParameters {
  id: string;
}

export const photo = Location(
  '/photo/:id',
  ({id}: PhotoLocationParameters) => `/photo/${id}`,
);
