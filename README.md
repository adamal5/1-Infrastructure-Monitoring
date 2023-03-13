# Infrastructure-Monitoring
## This is the first task in a set of tasks to refresh Python Skills.
### Project: Build a Python tool that monitors your infrastructure and alerts you if a static threshold is breached. 


### Brief:
Build a Python tool that monitors your infrastructure and alerts you when issues arise. The tool should be able to monitor things like CPU usage, memory usage and disk space. When an issue is detected, the tool should notify you via email or text message.

### My Approach:
**Steps:**
1. Aquire current system metric values
2. Define a threshold for these metrics
3. Check if the threshold has been breached
4. Send an alert via SNS if an issue is detected 


### Pre-Requisites
If you wish to use this script to check your local system and send and email alert you need to meet the following requirments:

1. Install python3
2. Install the following libaries: boto3 and psutil
3. Have an AWS account with an SNS topic configured and an email subscribed to that topic 
4. You will need to add your topic ARN to the infrastructure.py script where directed.
5. You will need a configured AWS role or user with SNS persmissions

Once you have all this you can run the script from your local machine and change any of the threshold in the script to monitor. 

### Improvements & Alteratives

1. Using a lambda to run this code and use eventbridge to schedule events at a required interval such as every 5 minutes
    - This would require further development as the script we need to access the host machine and run part of this script on the machine.
2. Another option is simply to create a cronjob to run this at the desired frequency
