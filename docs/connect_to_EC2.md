### How to connect to NIH Cloud Lab EC2 instances on AWS
Connecting to instances is a little different in Cloud Lab because external IP addresses are not allowed, such as your laptop's IP, and when on the VPN,
your private IP is changed. 

There are two ways you can connect to an instance in Cloud Lab:
+ When launching an instance, we can set a broad IP range for the security group that will encompass the VPN's private IP, without allowing traffic from the whole internet.
+ We can grant an IAM role that allows SSM (Session Manager) access if that is preferred over SSH.

To launch an instance, click the orange `Launch Instances` button in the top right. 

![launch_instance](/docs/images/launch_instance.png)

Name your instance under `Name and tags`.

Under `Application and OS Images (Amazon Machine Image` you can select your base machine image (AMI). Usually, the Amazon base image will work fine, but for some instances you may want to use a different base image. Also, some Marketplace solutions will use different base images. One reason this matters is that to use the session manager (SSM) to connect to your instance, you will need to select an Amazon AMI here. If you need a different AMI and also need to connect via SSM, please email CloudLab@nih.gov and we can help you write a startup script to launch SSM.

![AMI](/docs/images/AMI.png)

Next, under `Instance  type`, select your instance type. You can click `Compare instance types` to see the full specs of all available instances. 

![instance_type](/docs/images/instance_type.png)

Under `Key pair (login)` select your key pair. If you need to generate a new key pair, click `Create new key pair`, then give your key a name, select `RSA` and `.pem`, then `Create key pair`. Make sure you secure your key and never share with other users or make available on Github. 

![new_key](/docs/images/new_key.png)

Now, under `Network settings` we wil set our security group that allows us to SSH into the instance. You can either create a security group and then select `Select existing security group`, or leave the default selected for `Create security group`. Leave the box checked that says `Allow SSH traffic from` and then in the dropdown select `Custom` and then in the search box type `10.0.0.0/8`. This provides a range of IP addresses that should encompass your VPN's private IP. This may not work, if your IP is not in that range, so scroll down to `Additional Troubleshooting`. 

![security_group](/docs/images/security_group.png)

Now go to `Configure storage` and set the GB that you will need. You can always resize later by editing the instance.

If you plan to only connect via SSH, and not SSM, go ahead and click `Launch Instance` on the bottom right part of the screen. However, if you would like to have SSM access available, and are using an Amazon AMI, then click the `Advanced details` drop down arrow. Under `IAM instance profile`, select `SSM-Role-For-EC2`. You may need to search for it. 

![IAM](/docs/images/IAM_SSM_role.png)

Now you are ready to launch, and SSH and SSM should both be available under the `Connect` menu once your instance is running. 

![connect](/docs/images/connect_ec2.png)

Here is the view if you try and connect via SSM. It will open a terminal in your browser window. Once in, switch to the ec2-user by typing `sudo su ec2-user`

![SSM](/docs/images/SSM.png)

To connect via SSH, click this SSH option.

![SSH](/docs/images/SSH.png)

Then copy the example text under number four. For security reasons we don't include a screenshot, but it will be something like: 

`ssh -i "<PATH/TO/KEY_FILE>.pem" ec2-user@<INSTANCE-IP>`. Paste that into a terminal or Cloud Shell window. If not using an Amazon AMI, the user name will be different, for example, an Ubuntu image will have the username `ubuntu`. 

### Additional Troubleshooting
If your assigned IP is outside the range of 10.0.0.0/8, then you will need to update your security group to include your assigned IP. Unfortunately, you will need to do this every time you sign in to the VPN. To keep things simple, you can go to Network and Security > Security Groups on the left of the EC2 menu, select the Security group ID associated with your instance, click Actions at the top, and click `Edit inbound rules`. Click Add rule, select SSH, custom, and then paste in your IP followed by /32. This should allow you to SSH into the instance.

If you are on campus, your IP may remain stable, you will need to check. To find your current IP, run ifconfig( macOS/linux user) or ipconfig(Windows user) and identify the assigned IP address. For Windows, look for DNS suffix `nih.gov` which will show up if you are connected to the VPN. 

![windows](/docs/images/windows.jpg)

For macOS: Look for utun(number) where number is the highest number of the utun series, which should have an IP assigned. This could be utun1-3. 

![mac](/docs/images/mac.jpg)

Once you have your IP, update the security group as described above and then try and SSH into the instance again. 




