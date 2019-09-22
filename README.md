## Overview
This is a brief tutorial to run container using Cloud Run on Google Cloud Platform. It is part of my presentation at a meet up organized by Google Cloud Group - San Francisco https://www.meetup.com/GDGSanFrancisco/

## Pre-requsites
You have installed `gcloud` and `docker` utility and `gcloud` is pointing to appropriate project in your GCP account. 

Following APIs should be enabled in your project:

- Cloud Build API
- Cloud Run API

Your authenticated account has appropriate permissions.

```
gcloud auth activate-service-account --key-file=./cloud-run-demo-c807c3bf0190.json 
```


## Steps
- Build and test application locally
- Repackage application as a Docker container
- Test Docker container on your local machine
- Deploy container on Cloud Run 
- Test Cloud Run features inncluding scalability 

### Buid and test application locally

#### Run locally in debug mode
```
FLASK_APP=app.py FLASK_DEBUG=1 python -m flask run
Point your browser to http://127.0.0.1:5000/ 
```
#### Run locally in non-debug mode
```
python app.py
Point your browser to http://127.0.0.1:8080/ 
```

#### Build docker image 

```
gcloud builds submit --tag gcr.io/cloud-run-demo-253718/cloud_run_demo .
```

#### Verify docker image is built successfully

```
gcloud container images list --repository=gcr.io/cloud-run-demo-253718
```

#### test docker image 
```
sudo docker pull gcr.io/cloud-run-demo-253718/cloud_run_demo
sudo docker images 
PORT=8080 && sudo docker run -p 8080:${PORT} -e PORT=${PORT} gcr.io/cloud-run-demo-253718/cloud_run_demo

Point your browser to 127.0.0.1:8080
```

#### Deploy it to Google Cloud Run
```
gcloud beta run deploy cloud-run-demo \
       --image gcr.io/cloud-run-demo-253718/cloud_run_demo \
       --platform=managed \
       --memory=64Mi \
       --allow-unauthenticated \
       --region=us-central1
```

#### List the service deployed and revisions
```
gcloud beta run services list --platform managed
gcloud beta run revisions list --platform managed
```

#### Stress test the service
```
ab -c 100 -n 10000 -r https://cloud-run-demo-rkde4t733q-uc.a.run.app/
```







