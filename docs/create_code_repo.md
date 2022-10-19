# Guide to using AWS CodeCommit

Most NIH Cloud Lab users are probably used to using GitHub to manage and access code. The cloud providers also offer their own managed git repositories, which allows you to keep all your code within AWS without any external integrations.
Follow this guide to learn how to set up and use AWS CodeCommit.

### Create a CodeCommit Repository

1. Navigate to the CodeCommit page.

<img src="/docs/images/1_find_code_commit.png" width="550" height="200">

2. Click **Create repository**

<img src="/docs/images/2_create_respository.png" width="550" height="200">

3. Enter the necessary information for your repository. Feel free to add tags to track costs. Click **Create**.

<img src="/docs/images/3_add_repo_info.png" width="550" height="550">

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

### Clone the Repository and Push Code

1. You should not be authenticated and ready to clone the repository locally. To copy the url path, you can (A) click on the HTTPS link on the CodeCommit page. 

<img src="/docs/images/1_clone_respository1.png" width="550" height="150">

Or, (B) you can go into the details for your repository, and click **Clone URL** in the top right. 

<img src="/docs/images/1_clone_respository2.png" width="550" height="600">

If you get an error, re-authenticate with your Short Term Access Keys.

2. Now you can use regular git commands to add, commit, push etc. If you have to reinitialize your keys, then you may need to run `git init` to reinitialize the repo.

A simple workflow would look like this. 

```
# Clone the repo
git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/cloud-lab-test-repo
# CD into the repo
cd cloud-lab-test-repo
# Copy in the files you want to commit to the CodeCommit repository
cp ../example_file.txt .
# Create a new branch, Code Commit does not create a default branch, so you need to create a branch to push to.
git checkout -b cloud-lab-branch
# Stage your files
git add example_file.txt 
# Commit
git commit -m 'cloud lab test commit'
# Push to CodeCommit Repo
git push origin cloud-lab
# Test pulling files back down
git pull git pull origin cloud-lab
```
You should now see your file(s) in the CodeCommit Repository.





 
