# Yoga app

## Developing
``` sh
scripts/setdev.sh
pip install -r requirements.txt
```
this will ensure that you are developing in the right python environment

## Running the backend:
`scripts/run_yoga_backend.sh` this will start the backend dev server

## Running the frontend:
`cd fe && npm i` to install the dependencies
`scripts/run_yoga_frontend.sh` this will start the front end dev server

### Both dev servers are hot reloading, meaning you only need to run these when you start developing and they will update as you save new changes
