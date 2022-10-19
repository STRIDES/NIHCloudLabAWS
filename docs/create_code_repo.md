# Guide to using AWS CodeCommit

Most NIH Cloud Lab users are probably used to using GitHub to manage and access code. The cloud providers also offer their own managed git repositories, which allows you to keep all your code within AWS without any external integrations.
Follow this guide to learn how to set up and use AWS CodeCommit.

### Create a CodeCommit Repository

1. Navigate to the CodeCommit page.

<img src="/docs/images/find_codecommit.png" width="550" height="150">

2. Click **Create repository**

<img src="/docs/images/create_repository.png" width="550" height="150">

3. Enter the necessary information for your repository. Feel free to add tags to track costs. Click **Create**.

<img src="/docs/images/3_add_repo_info.png" width="550" height="150">

### Authenticate and Set Up Environment

All the instructions for setting up your environment are outlined in this [AWS documentation](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-https-unixes.html). Because we are using Short Term Access Keys, we need to use the AWS CLI credential helper. 

1. Open a compute environment of choice, either [EC2](https://github.com/STRIDES/NIHCloudLabAWS/blob/main/docs/connect_ec2.md), a [Sagemaker Notebook](https://github.com/STRIDES/NIHCloudLabAWS/blob/main/docs/Jupyter_notebook.md), or [Cloud Shell](https://aws.amazon.com/cloudshell/).

2. Authenticate the AWS CLI using your [Short Term Access Keys](https://github.com/STRIDES/NIHCloudLabAWS/blob/main/docs/Intramural_STAKs.md). Make sure you redo this whenever you disconnect as these keys reset periodically.

3. If using an EC2 instance, [install Git](https://git-scm.com/download/linux). AWS Linux machines will install with `sudo yum install git -y`. Cloud Shell and Sagemaker Instances already have Git installed.

4. Set up the credential helper. Run the following code to update the git config. 

```
git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true
```

### Clone the Repository and Push Local Code
