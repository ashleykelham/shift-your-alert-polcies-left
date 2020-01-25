# shift-your-alert-polcies-left

This repository is based on the [Medium article here](https://medium.com/@ashley.kelham/shift-your-policies-left-2893246aeeee)

### Requirements
* Google Cloud Account
* Firestore in Datastore mode enabled on the Google Cloud Project
* GCloud installed
* Azure Devops 

Most of the files need the values assigned for 

* $env - This is your deployment environment eg dev, test or prod
* $gcpProjectId - The Google Cloud project Id of the project you are deploying to

The project is split into directories each relating to a different component

### slowfunction
This is a Google Cloud Function written in python 3.7 that simulates a slow responding API. 

### alertlistener
This is a Google Cloud Function written in python 3.7 that stpres Stackdriver alert notifications and can return how many active alerts exist.

### notifications
These are Stackdriver notification channels that will call our alertlistener function when a policy is triggered

### policies
These are Stackdriver policies that will trigger when our slow function is used and use the notification channels set up.  You have to edit these to use the names assigned to the notification channels created when you deployed them.
