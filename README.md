# Infrastructure-Monitoring
## This is the first task in a set of tasks to refresh Python Skills.
### Project: Build a Python tool that monitors your infrastructure and alerts you if a static threshold is breached. 

### Pre-Requisites
If you wish to use this script to check your local system and send and email alert you need to meet the following requirments:

1. Install python3
2. Install the following libaries: boto3 and psutil
3. Have an AWS account with an SNS topic configured and an email subscribed to that topic 
4. You will need to add your topic ARN to the infrastructure.py script where directed.
5. You will need a configured AWS role or user with SNS persmissions

Once you have all this you can run the script from your local machine and change any of the threshold in the script to monitor. 
