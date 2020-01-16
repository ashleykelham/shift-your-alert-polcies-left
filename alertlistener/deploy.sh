gcloud functions deploy alertlistener-$env --allow-unauthenticated --entry-point alerts --runtime python37 --trigger-http --project $gcpProjectId --memory 128MB --set-env-vars ENV=$env
