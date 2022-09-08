# Connect to your EC2 instance in Cloud Lab

1. Go to the EC2 console. Make sure your instance is running, and *Status check* says *2/2 checks passed*. Click on the instance ID to look at the details for that instance.

<img src="/docs/images/1_select_instance_ID.png" width="550" height="250">

2. Click **Connect**

<img src="/docs/images/2_click_connect.png" width="550" height="250">

3. Now we can connect via *Session Manager* or *SSH*. We will start with Session Manager. Make sure you select Session Manager at the top, then click **Connect**. Now you will have a terminal within your browser to use the EC2 instance.

<img src="/docs/images/3_session_manager.png" width="550" height="250">

4. Now let's try connecting via SSH. Select *SSH client*, and then copy the example given at the bottom. Note that the example username is typically `ec2-user` but if you are using Ubuntu as the operating system, the username is `ubuntu`, and you may need to modify the example EC2 gives you. 

<img src="/docs/images/4_connect_ssh.png" width="550" height="250">

5. Open a terminal on Mac or Linux. On Windows connect [using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html). Paste in the command from #4. If everything works, you will now be SSH'd into your EC2 machine.

<img src="/docs/images/5_terminal.png" width="550" height="250">



