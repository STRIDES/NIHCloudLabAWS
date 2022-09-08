### Obtaining your Short Term Access Keys for Intramural Cloud Lab Users

If you have an NIH identity, you can access your Short Term Access Keys (STAKs) at the same place you access the AWS console (https://iam.nih.gov, VPN or Campus only).

1. Click `Cloud Access`. 

<img src="/docs/images/1_cloud_access.png" width="550" height="250">

2. On the line with your account name, click **Short-term access keys**. 

<img src="/docs/images/2_click_stak.png" width="550" height="200">

3. Copy the three lines from Option 1. The only method that will work for authentication in Cloud Lab is to paste all three of these into your terminal, because you will need the two keys and the session token. You will need to redo this step whenever your connection is lost or your keys expire. If you are using a Sagemaker notebook, you won't need to authenticate, but for EC2 or Cloud Shell you will need to authenticate.

<img src="/docs/images/3_paste_creds.png" width="550" height="250">

