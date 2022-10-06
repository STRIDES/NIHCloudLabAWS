# Connect to your EC2 instance in Cloud Lab
Connecting to instances is a little different in Cloud Lab because external IP addresses are not allowed, such as your laptop's IP, and when on the VPN,
your private IP is changed. 

There are two ways you can connect to an instance in Cloud Lab:
+ When launching an instance, we can set a broad IP range for the security group that will encompass the VPN's private IP, without allowing traffic from the whole internet.
+ We can grant an IAM role that allows SSM (Session Manager) access if that is preferred over SSH.

### Launch an instance

1. To launch an instance, click the orange `Launch Instances` button in the top right. 

![launch_instance](/docs/images/launch_instance.png)

2. Name your instance under `Name and tags`.

3. Under `Application and OS Images (Amazon Machine Image` you can select your base machine image (AMI). Usually, the Amazon base image will work fine, but for some instances you may want to use a different base image. Also, some Marketplace solutions will use different base images. One reason this matters is that to use the session manager (SSM) to connect to your instance, you will need to select an Amazon AMI here. If you need a different AMI and also need to connect via SSM, please email CloudLab@nih.gov and we can help you write a startup script to launch SSM.

![AMI](/docs/images/AMI.png)

4. Next, under `Instance  type`, select your instance type. You can click `Compare instance types` to see the full specs of all available instances. 

![instance_type](/docs/images/instance_type.png)

5. Under `Key pair (login)` select your key pair. If you need to generate a new key pair, click `Create new key pair`, then give your key a name, select `RSA` and `.pem`, then `Create key pair`. Make sure you secure your key and never share with other users or make available on Github. 

![new_key](/docs/images/new_key.png)

6. Now, under `Network settings` we wil set our security group that allows us to SSH into the instance. You can either create a security group and then select `Select existing security group`, or leave the default selected for `Create security group`. Leave the box checked that says `Allow SSH traffic from` and then in the dropdown select `Custom` and then in the search box type `10.0.0.0/8`. This provides a range of IP addresses that should encompass your VPN's private IP. This may not work, if your IP is not in that range, so scroll down to `Additional Troubleshooting`. 

![security_group](/docs/images/security_group.png)

7. Go to `Configure storage` and set the GB that you will need. You can always resize later by editing the instance.

8. If you plan to only connect via SSH, and not SSM, go ahead and click `Launch Instance` on the bottom right part of the screen. However, if you would like to have SSM access available, and are using an Amazon AMI, then click the `Advanced details` drop down arrow. Under `IAM instance profile`, select `SSM-Role-For-EC2`. You may need to search for it. 

![IAM](/docs/images/IAM_SSM_role.png)

9. Now click launch. 

### Connect to you instance

1. Once your instance is running, and *Status check* says *2/2 checks passed*. Click on the instance ID to look at the details for that instance.

<img src="/docs/images/1_select_instance_ID.png" width="550" height="100">

2. Click **Connect**

<img src="/docs/images/2_click_connect.png" width="550" height="250">

3. SSH and Session Manager should both be available under the `Connect` menu once your instance is running. If you can not access Session Manager go back up to Step #8 and add the IAM Role.

4. Now let's try connecting via SSH. Select *SSH client*, and then copy the example given at the bottom. Note that the example username is typically `ec2-user` but if you are using Ubuntu as the operating system, the username is `ubuntu`, and you may need to modify the example EC2 gives you. 

<img src="/docs/images/4_connect_ssh.png" width="550" height="400">

5. Open a terminal on Mac or Linux. On Windows connect [using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html). Paste in the command from #4. If everything works, you will now be SSH'd into your EC2 machine.

<img src="/docs/images/5_terminal.png" width="550" height="250">

### Additional Troubleshooting
If your assigned IP is outside the range of 10.0.0.0/8, then you will need to update your security group to include your assigned IP. Unfortunately, you will need to do this every time you sign in to the VPN. To keep things simple, you can go to Network and Security > Security Groups on the left of the EC2 menu, select the Security group ID associated with your instance, click Actions at the top, and click `Edit inbound rules`. Click Add rule, select SSH, custom, and then paste in your IP followed by /32. This should allow you to SSH into the instance.

If you are on campus, your IP may remain stable, you will need to check. To find your current IP, run ifconfig( macOS/linux user) or ipconfig(Windows user) and identify the assigned IP address. For Windows, look for DNS suffix `nih.gov` which will show up if you are connected to the VPN. 

![windows](/docs/images/windows.jpg)

For macOS: Look for utun(number) where number is the highest number of the utun series, which should have an IP assigned. This could be utun1-3. You can also identify which interface is the wired connection by running “networksetup -listallhardwareports” which tells you the port type along the ID. For example, “en0” or “en1” might be the wired connection on your machine. Once you determine which ID this is, run “ifconfig” and find the corresponding ID.  That will give you the private IP that is assigned to that port and that would need to be used in the security group to allow ssh access.

![mac](/docs/images/mac.png)

Once you have your IP, update the security group as described above and then try and SSH into the instance again. 


