'''
Build a Python tool that monitors your infrastructure and alerts you when issues arise. 
The tool should be able to monitor things like CPU usage, memory usage, disk space, and 
network connectivity. When an issue is detected, the tool should notify you via email or text message.

Steps:

1. Access the operating system and gain the key metrics. (AWS Instance)
2. Define a threshold for these metrics
3. Send an alert when the issue is detected 

I'm going to use SNS as my notification system 

'''

# Import the libary to get system metrics
import psutil

# Import boto3 to you amazon SNS
import boto3

# Define the metrics we will monitor

def list_metrics():
    names = ['CPU','Memory','Disk']
    return names

def get_current_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_percentage_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    metrics = [cpu_usage,memory_percentage_usage,disk_usage]
    return metrics

# Define the thresholds
def define_metric_thresholds():
    cpu_threshold = 1.0
    memory_threshold = 1.0
    disk_threshold = 1.0
    threholds = [cpu_threshold,memory_threshold,disk_threshold]
    return threholds

# Define a message 

message = '''Hey Adama,

It looks like you're system is experiencing some issues. 
Please see the following breaches in your system thresholds:

'''

signiture = '''Kind regards,
The SRE Team
'''


# Conditional alerting

def check_metric_thresholds(names,metrics,thresholds, message):
    for i in range(len(metrics)):
        if metrics[i] > thresholds[i]:
            message += "\n" + names[i] + " usage: {}%".format(metrics[i])
    
    print (message + "\n" +  "\n" +  signiture)
    return message


# send an alert using AWS SES

def send_message_via_sns(alert_message):
    client = boto3.client('sns')
    response = client.publish(
    TopicArn='ADD YOUR AWS TOPIC ARN HERE',
    Message= alert_message,
    Subject='System Threshold Breach',
    MessageAttributes={
        'myAttributes': {
            'DataType': 'String',
            'StringValue': 'myValue',
        }
    })

    print(response)


# Print the Outcomes to check 

names = list_metrics()
metrics = get_current_system_metrics()
thresholds = define_metric_thresholds()
alert_message = check_metric_thresholds(names, metrics, thresholds, message)
response_message= send_message_via_sns(alert_message)