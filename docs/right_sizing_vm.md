# Guide to right-sizing your VM

## Monitor your CPU usage on EC2

1. Go to the EC2 console, and select the instance ID of the instance you want to monitor. 

<img src="/docs/images/1_EC2_homepage.png" width="550" height="125">

2. Scroll down and select the *Monitoring* tab.

<img src="/docs/images/1_EC2_homepage.png" width="550" height="150">

3. If you would like more information for a given metric, click the three dots and select *View in metrics*.

<img src="/docs/images/3_view_metrics.png" width="550" height="300">

4. Now you are on the CloudWatch page, and from here, you can go deep into a wide variety of metrics. Follow [this AWS guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingStarted.html) for more information.

5. If you need to change the size of your VM based on over- or under- CPU or memory utilization, first stop the instance.

<img src="/docs/images/4_stop_instance.png" width="550" height="300">

6. Change the instance type. In the top right, click *Actions > Instance settings > Change instance type.* 

<img src="/docs/images/5_edit_instance.png" width="550" height="300">

7. In the dropdown, select a new instance type and click **Apply**.

<img src="/docs/images/6_change_instance_type.png" width="550" height="300">

## Monitor your CPU usage on a Sagemaker instance

You can monitor some aspects of Sagemaker jobs in [CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html#cloudwatch-metrics-jobs), but unfortunately, you can not yet monitor CPU usage. If you want to monitor CPU or memory usage of a Sagemaker notebook, you will need to use Sagemaker Studio, but we do not yet have a guide on this product.
