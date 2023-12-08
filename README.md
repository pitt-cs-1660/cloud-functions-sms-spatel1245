## Sending SMS Text Via Cloud Functions

In this lab we will send a text message via Google Cloud Functions when a new file is uploaded to a Cloud Storage bucket. We will use the Twilio API to send the text message.

Please note that to successfully complete this lab you will need a mobile phone number and sign up for a [free](https://www.twilio.com/try-twilio) Twilio account.

## Twilio Setup
Once you sign up for Twilio you will be provided credits to use. For the purposes of this lab you should use the `test` credentials. You can find these credentials by clicking [Account > Keys & Credentials > API Keys and tokens](./images/api-token-nav.png).

You will need to use the [test number](./images/test-creds.png) provided in the code.

## Cloud Storage Setup
Create a Cloud Storage bucket to trigger a Cloud Function when a file is uploaded.
- make the bucket public

## Cloud Function Setup
Create a Cloud Function that will be triggered when a file is uploaded to the Cloud Storage bucket.

### Enable APIs
Below are the list of APIs I have enabled for this project. Enable them via the console or the shell.

```shell
❯ gcloud services list --enabled
NAME                              TITLE
artifactregistry.googleapis.com   Artifact Registry API
bigquery.googleapis.com           BigQuery API
bigquerymigration.googleapis.com  BigQuery Migration API
bigquerystorage.googleapis.com    BigQuery Storage API
cloudapis.googleapis.com          Google Cloud APIs
cloudbuild.googleapis.com         Cloud Build API
cloudfunctions.googleapis.com     Cloud Functions API
cloudtrace.googleapis.com         Cloud Trace API
containerregistry.googleapis.com  Container Registry API
datastore.googleapis.com          Cloud Datastore API
eventarc.googleapis.com           Eventarc API
logging.googleapis.com            Cloud Logging API
monitoring.googleapis.com         Cloud Monitoring API
pubsub.googleapis.com             Cloud Pub/Sub API
run.googleapis.com                Cloud Run Admin API
servicemanagement.googleapis.com  Service Management API
serviceusage.googleapis.com       Service Usage API
source.googleapis.com             Legacy Cloud Source Repositories API
sql-component.googleapis.com      Cloud SQL
storage-api.googleapis.com        Google Cloud Storage JSON API
storage-component.googleapis.com  Cloud Storage
storage.googleapis.com            Cloud Storage API

# you can enable APIs with the following command or use the console:
gcloud services enable <api1> <api2> ....
```

### Steps

- Use the `python3.11` runtime
- Allow unauthenticated invocations
- Create a `Cloud Storage Trigger` when a new object is created in the bucket
  - Use the `Finalize/Create` event type (google.cloud.storage.object.v1.finalized)
  - use the bucket you created earlier
- use the code in `main.py` and `requirements.txt` to complete the Cloud Function
  - NOTE: you can use the TEST functionality in the console

**you can also test with cURL if you function is unauthorized**

```shell
# @note: the test data in the POST body was taken from the TEST functionality in the console
curl -X POST -H 'Content-Type: application/json' https://us-east1-dansc0de-serverless.cloudfunctions.net/sms-example \
-d '{
  "data": {
    "name": "folder/Test.cs",
    "bucket": "some-bucket",
    "contentType": "application/json",
    "metageneration": "1",
    "timeCreated": "2020-04-23T07:38:57.230Z",
    "updated": "2020-04-23T07:38:57.230Z"
  },
  "type": "google.cloud.storage.object.v1.finalized",
  "specversion": "1.0",
  "source": "//pubsub.googleapis.com/",
  "id": "1234567890"
}'
```

### Submission
Submit screenshots/files of the following to Canvas in a ZIP file:
- Cloud Function Trigger (2.5 points)
- Cloud Function Metrics (2.5 points)
- Cloud Function Logs (2.5 points)
- Cloud Functions Details (2.5 points)