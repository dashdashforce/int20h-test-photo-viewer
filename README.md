# Photo viewer

[![CircleCI](https://circleci.com/gh/dashdashforce/int20h-test-photo-viewer/tree/master.svg?style=svg)](https://circleci.com/gh/dashdashforce/int20h-test-photo-viewer/tree/master)

## Web application start

### Backend

#### Base prepare

1. Clone repository from `https://github.com/dashdashforce/int20h-test-photo-viewer.git`
2. Go to backend directory
3. Run `cp .env.dist .env`
4. Get `api key` and `api secret` from Face++ service and copy them to `.env` file in `FACEPLUSPLUS_API_KEY` and `FACEPLUSPLUS_API_SECRET` fields

#### With Docker compose

In project root run command

`docker-compose up --build backend`

#### Manual

You'll need Python 3.7 for starting app

1. Go to `backend` directory in the project root
2. Run `make init` for initing python virtual env
3. Run `make install-dev` for installing project dependencies
4. Run `make run-dev`

Now `Photo viewer` API running on localhost:8888
You can try to check api sandbox: [Local sandbox](localhost:8888/graphql)

### Frontend

**TODO: Write frontend start instruction**
