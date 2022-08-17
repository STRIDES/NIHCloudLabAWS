# Guide to implementing auto-shutdown features in virtual machines (EC2 or Sagemaker)

## Autoshutdown EC2 instance

There already exists a [great guide](https://successengineer.medium.com/how-to-automatically-turn-off-your-ec2-instance-in-2021-b73374e51090) on how to configure autoshutdown on EC2.
Just note that when you set the Alarm Thresholds, you may want to set the threshold percent to be higher than 2% to increase the sensitivity and make it easier for your machine to shut down. 

## Autoshudown Sagemaker instance

Configuring auto shutdown on Sagemaker instances is also relatively simple. 

### Configuring a new instance

1. On the Sagemaker page, click **Create notebook instance**.

<img src="/docs/images/create_notebook_instance.jpeg" width="450" height="250">

2. Under *Additional Configuration* click the box under *Lifecycle configuration - optional*, then select **Create a new lifecycle configuration**.

<img src="/docs/images/click_configuration.png" width="450" height="250">

3. Name your configuration something like `idle-shutdown-sagemaker` and then paste in the following code under *Start notebook*. This code snippet will shutdown your VM after 3600 seconds (1 hr) of inactivity. If you want that time to be shorter, change it to something like 1800 (30 min).

```
#!/bin/bash

set -e

# PARAMETERS
IDLE_TIME=3600

echo "Fetching the autostop script"
wget https://raw.githubusercontent.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples/master/scripts/auto-stop-idle/autostop.py

echo "Starting the SageMaker autostop script in cron"

(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/bin/python $PWD/autostop.py --time $IDLE_TIME --ignore-connections") | crontab -
```

<img src="/docs/images/add_script.png" width="450" height="250">

4. Click **Create configuration**, then click **Create notebook instance**

### Configuring an existing instance

The instructions for adding auto-shutdown to an existing instance are almost identical. 

1. Select the instance you want to modify, and click **Edit** in the top right. Your instance does need to be stopped.

<img src="/docs/images/edit_instance_aws.png" width="450" height="250">

2. Now under *Additional configuration* select *Lifecycle configuration - optional* and follow the instructions above for 2–4.

3. Restart your instance and confirm that it will shut down after the specified amount of time. 

