# Photo viewer

[![CircleCI](https://circleci.com/gh/dashdashforce/int20h-test-photo-viewer/tree/master.svg?style=svg)](https://circleci.com/gh/dashdashforce/int20h-test-photo-viewer/tree/master)

## Web application start

### Backend

#### Base prepare

1. Clone repository from `https://github.com/dashdashforce/int20h-test-photo-viewer.git`
2. Go to the `backend` directory
3. Run `cp .env.dist .env`
4. Get `api key` and `api secret` from the Face++ service and copy them to `.env` file in `FACEPLUSPLUS_API_KEY` and `FACEPLUSPLUS_API_SECRET` fields

#### With Docker compose

In project root run command

`docker-compose up --build backend`

#### Manual backend install

You'll need Python 3.7 for starting app

1. Go to the `backend` directory in the project root
2. Run `make init` for initing python virtual env
3. Run `make install-dev` for installing project dependencies
4. Run `make run-dev`

Now `Photo viewer` API is running on localhost:8888
You can try to check api sandbox: [Local sandbox](http://localhost:8888/graphql)

### Frontend

For starting frontend app you'll need Node latest version

#### Manual frontend install

1. Go to the `frontend` directory in the project root
2. Run `yarn install` for installing frontend dependencies
3. If you want to use local api server - change Apollo Client
uri field in `project/frontend/src/index.tsx` to `localhost:8888`.
4. Run `yarn start` for starting frontend

Frontend is running on `localhost:3000`

Now go to [Local frontend](http://localhost:3000) for checking out our awesome web app.

## Deployed App

[Deployed Application](http://ddforce.nckcol.com/photo-viewer)
[Deployed API Sandbox](http://ddforce.nckcol.com/photo-viewer/api/graphql)

## Contributors

- [Oleg Lipskiy](https://github.com/acterics)
- [Nick Popov](https://github.com/nckcol)
- [Max Kostinskiy](https://github.com/promojjj)
- [Andrey Neklesa](https://github.com/alad1chek)
