### How to connect to NIH Cloud Lab EC2 instances on AWS
Connecting to instances is a little different in Cloud Lab because external IP addresses are not allowed, such as your laptop's IP, and when on the VPN,
your private IP is changed. 

There are two ways you can connect to an instance in Cloud Lab.

First, when launching an instance, we can set a broad IP range for the security group that will encompass the VPN's private IP, without allowing traffic from the whole internet. Second, we can grant an IAM role that allows SSM (Session Manager) access if that is preferred over SSH.

To launch an instance, click the orange `Launch Instances` button in the top right. 


![launch_instance](/docs/images/launch_instance.png)



