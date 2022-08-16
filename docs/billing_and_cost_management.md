Tagging
Billing Report
Creating Budget Alerts

# Guide to AWS Billing and Cost Management

Understanding how to manager your costs can be difficult in the cloud. For one thing, you have to keep track of how much you have spent with the obvious services, like EC2, Sagemaker and S3. On the other hand, how can you figure out how much you are being charged for your network (VPC)? 
Further, some Cloud Lab users are interested in understanding how to forcast cloud costs for a larger project. For example, if you want to understand the cost of calling somatic variants on 100 samples, but in Cloud Lab you plan to benchmark using five samples. How would you go about doing that? 
This guide aims to answer these questions. 

## 1. Resource Tagging

One of the first steps to understanding costs is resource tagging. Billing reports will be aggregated across time and services, and it can be hard to figure out how much did that variant calling pipeline cost to run? 
Tagging allows you attach metadata to resources that you can later filter for in Billing reports. AWS has a comprehensive Tagging guide [here](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
You can add a tag to pretty much any resource but let's look at a few examples. 

### Add tags to a storage bucket

1. Select the bucket and then click `Properties`. 

<img src="/docs/images/bucket_properties.png" width="350" height="75">

2. Scroll down to `Tags` and click `Edit`.

<img src="/docs/images/edit_tags_bucket.png" width="350" height="75">

3. Add a few tags that help identify the filtering you want to do later, feel free to look at the [AWS guide](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) for examples.

<img src="/docs/images/add_tags_bucket.png" width="350" height="200">

### Add tags to an EC2 instance

This assumes your instance already exists. You can also tag a new instance during creation using the same method.

1. Select the instance and click the `Tags` tab, then `Manage Tags`.

<img src="/docs/images/EC2_edit_tags.png" width="350" height="200">

2. Add your tags, then click `Save`.

<img src="/docs/images/EC2_add_tags.png" width="350" height="200">

### Add tags to a Sagemaker instance

1. Select the Sagemaker instance and scroll down to `Tags`.
2. Click `Edit`, then add tags as described above.

<img src="/docs/images/sagemaker_edit_tags2.png" width="350" height="200">

<img src="/docs/images/sagemaker_add_tags.png" width="350" height="200">

## 2. Explore Billing Reports



