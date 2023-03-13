'''
Build a Python tool that monitors your infrastructure and alerts you when issues arise. 
The tool should be able to monitor things like CPU usage, memory usage, disk space, and 
network connectivity. When an issue is detected, the tool should notify you via email or text message.

Steps:

1. Access the operating system and gain the key metrics. (AWS Instance)
2. Define a threshold for these metrics
3. Send an alert when the issue is detected 

I'm going to use SES as my notification system 

'''

import psutil

# Define the metrics we will monitor

cpu_usage = psutil.cpu_percent(interval=1)
memory_percentage_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# Define the thresholds

cpu_threshold = 30.0
memory_threshold = 85.0
disk_threshold = 50

# Define a message 

message = ''' Hey Adama,

It looks like you're system is experiencing some issues. 
Please see the following breaches in your system thresholds:

Kind regards,
Also Adama

'''

# Conditional alerting

if cpu_usage > cpu_threshold:



# Print the Outcomes to check 
print("CPU usage: {}%".format(cpu_usage))
print("Memory usage: {}%".format(memory_percentage_usage))
print("Disk usage: {}%".format(disk_usage))
