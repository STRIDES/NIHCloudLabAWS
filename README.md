# NIH Cloud Lab for AWS
---------------------------------

There are a lot of resources available to learn about AWS, which can be overwhelming. NIH Cloud Lab’s goal is to make cloud very easy and accessible for you, so that you can stop wasting time on administrative tasks and focus on your research.

Use this repository to learn about how to use AWS by exploring the linked resources and walking through the tutorials. If you are a beginner, we suggest you begin with this 101 section. If you already have foundational knowledge of AWS and cloud, feel free to skip ahead to the [tutorials](/tutorials/) section for in-depth examples of how to run specific workflows such as genomic variant calling and medical image analysis.

## Overview of Page Contents

+ [Getting Started](#GS)
+ [Overview](#OV)
+ [Command Line Tools](#CLI)
+ [Amazon Marketplace](#MARK)
+ [Ingest and Store Data](#STO)
+ [Virtual Machines in EC2](#VM)
+ [Disk Images](#IM)
+ [SageMaker Notebooks](#SAG)
+ [Creating a Conda Environment](#CO)
+ [Clusters](#CLU)
+ [Billing and Benchmarking](#BB)
+ [Cost Optimization](#COST)
+ [Getting Support](#SUP)
+ [Additional Training](#TR)

## **Getting Started** <a name="GS"></a>
You can learn a lot of what is possible on AWS in the AWS Getting Started [Tutorials Page](https://aws.amazon.com/getting-started/hands-on/?getting-started-all.sort-by=item.additionalFields.sortOrder&getting-started-all.sort-order=asc&awsf.getting-started-category=*all&awsf.getting-started-level=*all&awsf.getting-started-content-type=*all&awsm.page-getting-started-all=2) and we recommend you go there and explore some of the tutorials on offer. Nonetheless, it can be hard to know where to start if you are new to the cloud. To help you, we thought through some of the most common tasks you will encounter doing cloud-enabled research, and gathered tutorials and guides specific to those topics. We hope the following materials are helpful as you explore migrating your research to the cloud.

## **Overview** <a name="OV"></a>
There are three primary ways you can run analyses using AWS: using virtual machines, Jupyter Notebook instances, and Serverless services. We give a breif overview of each of these here and go into more detail in the sections below. [Virtual machines](https://aws.amazon.com/getting-started/launch-a-virtual-machine-B-0/) are like your desktop computers, but you access them through the cloud console and you get to decide what resources are on that computer such as CPU and memory. In AWS, these virtual machines are called Elastic Compute Cloud or EC2. Jupyter Notebook instances are virtual machines with Juptyer Lab pre loaded onto them. On AWS these are run through [SageMaker](https://aws.amazon.com/pm/sagemaker/?trk=8987dd52-6f33-407a-b89b-a7ba025c913c&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Machine%20Learning|Sagemaker|US|EN|Text&s_kwcid=AL!4422!3!532502995192!e!!g!!aws%20sagemaker&ef_id=CjwKCAjw7IeUBhBbEiwADhiEMfXNyIY5DZB4FG17gZcXYycBpN1lNPRNfXdxWP9NhTY_t_IrAmEiIhoCIqwQAvD_BwE:G:s&s_kwcid=AL!4422!3!532502995192!e!!g!!aws%20sagemaker). You decide what kind of virtual machine you want to 'spin up' and then you can run Juptyer notebooks on that virtual machine. Finally, serverless services are services allow you to run things, an analysis, an app, a website, and not have to deal with your own servers (VMs). There are still servers running somewhere, you just don't have to manage them. All you have to do is call a command that runs your analysis in the background, and copies the output files to a storage bucket. 

## **Command Line Tools** <a name="CLI"></a>
Most things in AWS can be done without the command line, but the command line tools will generally make your life easier in the long run. Command line interface (CLI) tools are those that you use directly in a terminal/shell as opposed to clicking within a graphical user interface (UI). The primary tool you will need is the AWS CLI, which will allow you to interact with instances or S3 buckets (see below) from your local terminal. Instructions for the CLI can be found [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html). If you are unable to install locally, you can use all the CLI commands from within EC2 and SageMaker instances. 

To configure the CLI, you will need to authenticate using [access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html), which are unique strings that tell AWS that you are allowed to interact with the account. Within Cloud Lab, you will need to use Short Term Access Keys. If you are an intramural user, the instructions for accessing these are found [here](/docs/Intramural_STAKs.md). Short Term Access keys differ from Long Term Access keys in that they only work for a short period of time. Once your time limit expires, you have to request new keys and then authenticate again.

If you are running bioinformatic workflows, you can leverage the serverless functionality of AWS using the [AWS Genomics CLI](https://aws.amazon.com/genomics-cli/), which is a wrapper for genomics workflow managers and AWS Batch (serverless computing cluster). See our [docs](/docs/agc.md) on how to set up the AGC CLI for Cloud Lab. You can also use this older [genomics solution](https://docs.opendata.aws/genomics-workflows/index.html) if you have trouble with the newer CLI. See our [docs](/docs/Genomics_Workflows.md) for tips and tricks specific to the Cloud Lab environment.

## **Amazon Marketplace** <a name="STO"></a>
The [AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/what-is-marketplace.html) is a platform similar to Amazon.com where you can search for and launch pre-configured solutions such as Machine Images. Examples of images you may launch would those with enhanced security (see EC2 section) or ones opimized for various tasks like machine learning or accelerated genomics. 

## **Ingest and Store Data using Amazon S3** <a name="STO"></a>
Data can be stored in two places on the cloud: either in a cloud storage bucket, which on AWS is called Amazon Simple Storage Service (S3), or on an instance, which usually has Elastic Block Storage. Block storage is storage with a finite size (e. g. 200GB) that is located on your virtual machine. S3 is object storage, meaning that you can put any type of object in S3, and it is scalable, so there is no upper limit on storage size. 

In general, you want to keep your compute and storage separate, so you should aim to store data in S3 for access, then only copy the data you need to a particular instance to run an analysis, then copy the results back to S3. In addition, the data on an instance is only available when the instance is running, whereas the data in S3 is always available, and serves as a longer term storage solution. [Here](https://aws.amazon.com/getting-started/hands-on/backup-files-to-amazon-s3/) is a great tutorial on how to use S3 and is worth going through to learn how it all works.

We also wanted to give you a few other tips that may be helpful when it comes to moving and storing data. If your end goal is to move data to an S3 bucket, you can do that using the UI and clicking the `Upload` button, or you can use the CLI by typing `aws s3 cp <FILE> <s3://BUCKET>`. If you want to move a whole folder, then use the --recursive flag: `aws s3 cp <DIR> <s3://BUCKET> --recursive`. The same applies whether moving data from your local directory or from an EC2 instance. Likewise, you can move data from S3 back to your local machine or your EC2 instance with `aws s3 cp <s3://BUCKET/FILE> <DESTINATION/PATH>`. Finally, you can move data to an instance using scp, just make sure the instance is running. You can use a command like `scp -i 'key.pem' <FILE> ec2-user@ec2-NAME.REGION.compute.amazonaws.com:~/PATH `. SCP is an SSH tool for copying local data to a remote server. Once the data is on the VM, it is a good idea to use `aws s3 cp` to move data to S3. If you are trying to move data from the Short Read Archive (SRA) to an instance, or to S3, you can use [fasterq_dump](https://github.com/glarue/fasterq_dump) from the SRA toolkit. The best way is probably to install on an EC2 instance, then copy the data to the VM, then optionally copy it to S3 for backup or use elsewhere. 

There is some strategy to managing storage costs as well. When you have spun up a VM, you have already paid for the storage on the VM since you are paying for the size of the disk, whereas S3 storage is charged based on how much data you put in your buckets. This is something to think about when copying results files back to S3 for example. If they are not files you will need later, then leave them on the VM's EBS and save your money on more important data to put in S3. If the data is important though, either create a disk image as a backup, or copy it to s3, or both! 

## **Spin up a Virtual Machine and run a workflow** <a name="VM"></a>
Virtual machines (VMs) on AWS are called Amazon Elastic Compute Cloud (EC2) and are like virtual computers that you access via SSH and which start as (nearly) completly blank slates. You have complete control over the VM configuration beginning with the [operating system](https://docs.aws.amazon.com/systems-manager/latest/userguide/prereqs-operating-systems.html#prereqs-os-linux). You can choose a variety of Linux flavors, as well as macOS and Windows. Virtual Machines are organized into [machine families](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjw7IeUBhBbEiwADhiEMedsuBikka4KyMJjZdw2Qi63FwjhvKhPlmHr9EYefV3GIE14lRz-ixoCqWIQAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types) with different functions, such as General Purpose, Compute Optimized, Accelerated Computing etc. You can also select machines with graphics processing units (GPUs), which run very quickly for some use cases, but also cost a lot more than most of the CPU machines. Billing occurs on a per second basis, and larger and faster machine types cost more per second. This is why it is important to stop or delete machines when not in use to minimize costs. 

Many great resources exist on how to spin up, connect to, and work on a VM on AWS. The first place to direct you is the tutorial created by [NIH Common Data Fund](https://training.nih-cfde.org/en/latest/Cloud-Platforms/Introduction_to_Amazon_Web_Services/introtoaws3/). This tutorial expects that you will launch an instance and work with it interactively.
[Here](https://aws.amazon.com/getting-started/hands-on/launch-a-virtual-machine/) is an example developed by AWS that gives a good step by step on how to launch and access an instance using Amazon Lightsail. Lightsail is a simplified version of the full AWS console, and may provide an interface you like better for using EC2. Note that resources you spin up in Lightsail will not be available in EC2. A lot of the [tutorials](/tutorials/) in this repo will have instructions on spinning up EC2 instances as well. 

If you need help on launching a Windows VM, check out this [tutorial](https://aws.amazon.com/getting-started/hands-on/launch-windows-vm/).

From a security perspective, we recommend that you use Center for Internet Security (CIS) Hardened VMs. These have security controls that meet the CIS benchmark for enhanced cloud security. To use these VMs, go to the AWS Marketplace > Discover Products. Then search for `CIS Hardened` and chose the OS that meets your needs. Click, `Continue to Subscribe` in the top right, and then `Continue to Configuration` and set your configuration parameters. Finally, click `Continue to Launch`. Here you decide how to launch the Marketplace solution; we recommend `Launch from EC2`, although you are welcome to experiment with the other options. Now click `Launch` and walk through the usual EC2 launch parameters. Click `Launch` and then you can view the status of your VM in the EC2 Instances page.

If you need to scale your VM up or down (see Cost Optimization below), you can always change the machine type by clicking on the instance ID, then go to `Actions > Instance Settings > Change instance type`. The VM has to be stopped to change the instance type.  

Finally, when you SSH into your instance, note that the username is typically `ec2-user` but on Ubuntu machines, the username is `ubuntu`. 

## **Disk Images** <a name="IM"></a>
Part of the power of virual machines is that they offer a blank slate for you to configure as desired. However, sometimes you want to recycle data or installed programs for your next VM instead of having to recreate the wheel. One solution to this issue is using disk (or machine) images, where you copy your existing virtual disk to an [Amazon Machine Image](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) which can serve as a backup, or can be used to launch a new instance with the programs and data from a previous instance.

## **Launch a SageMaker Notebook** <a name="SAG"></a>
Let's begin with running a SageMaker notebook. Notebooks are ideal for certain problems, particularly when doing a tutorial because you can mix code with instructions. They are also great for exploring your data or workflow one portion at a time, since the code gets broken up into little chunks that you can run one by one, which lends itself very well to most ML/AI problems. The notebook we are going to run is inside this repo, but we are going to launch a SageMaker instance and then copy the notebook into AWS programatically.

To begin, go to `Services > Machine Learning > Amazon SageMaker`. Once on the landing page, you should see a menu bar on the left side of the page. Click `Notebook` and then `Notebook instances`. Now click the orange colored `Create notebook instance`. Give your instance a globally unique name. Under `Notebook instance type` choose a machine type. You can find the full list of instance types [here](https://aws.amazon.com/ec2/instance-types/). Fortunately not all machines are available with SageMaker, so we only have to choose from a few. You can figure out how much your notebook will cost to run using the pricing calculator [here](https://aws.amazon.com/ec2/pricing/on-demand/) based on your machine type. As long as the notebook is running (and not stopped) you will be charged per second of use. Leave all other values as default for now. Click `Create notebook instance`. It should take about 10 minutes to spin up, so go brew some coffee and come back. Once the status changes from `Pending` to `InService` then you can connect.

### Import our training notebook
Now that our instance is `InService` (read running) we can click `Open JupyterLab` on the far right of the screen. Notice that we have a lot of options for creating new notebooks, and we can also open a terminal window. Let's begin by looking at the AWS example notebooks by clicking the bottom icon on the far left that looks like a brain. You will see that most of these are generic data science and ML topics, but there are a few biomedically relevant examples, with several notebooks focused on cancer data. These notebooks are a great way to learn some basic functionality of AWS like ingesting data, training and running ML/AI models, and running R notebooks. You can also explore a variety of more advanced applications. Open a few notebooks and copy them to your workspace to see how that works. After this, you can copy in a custom notebook and some example data. From the base directory, click the git icon on the middle left bar, it kind of looks like the letter 'T' with a tilt. Click `Clone a Repository`, and then paste the address to this repo (from the green box in the top right) into the box.

```
git clone https://github.com/STRIDES/NIHCloudLabAWS.git
```

Now you have the NIHCloudLabAWS directory available. Navigate to NIHCloudLabAWS > tutorials > notebooks > GWAS > GWAS_coat_color.ipynb.
Explore this notebook and see how data moves in and out of the SageMaker environment. You can also manually add files, whether notebooks or data using the up arrow in the top left navigation menu. We can easily switch between different kernels in the top right, whether R or Python or Spark. 

Here's a few tips if you are new to notebooks. The navigation menu in the top left controls the control panel that is the equivalent to your directory structure. The panel above the notebook itself controls the notebook options. Most of these are obvious, but a few you will use often are:
+ the plus sign to add a cell
+ the scissors to cut a cell
+ stop to stop a running process
+ run a cell with the play button or use shift + enter/return. You can also use CMD + Enter, but it will only run the current cell and not move to the next cell. 

Above that menu you will see an option called `Kernel` which is useful if you need to reset the kernel, you can click Kernel > Restart Kernel and Clear All Outputs. This will give you a clean restart. You can also use Kernel > Change Kernel if you need to switch between Kernel environments. Also worth noting that when you run a cell, sometimes it doesn't produce any output, but things are running in the background. If the brackets next to a cell have an * then it is still running. You can also look at the bottom where the kernel is listed (e.g. Python 3 | status) and it will show either Idle or Busy depending on if anything is running or not. 

## **Creating a Conda Environment** <a name="CO"></a>
Virtual environments allow you to manage package versions without having package conflicts. For example, if you needed Python 3 for one analysis, but Python 2.7 for another, you could create separate environments to use the two versions of Python. One of the most popular package managers used for creating virtual environments is the [conda package manager](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#:~:text=A%20conda%20environment%20is%20a,NumPy%201.6%20for%20legacy%20testing). 

Mamba is a reimplementation of conda written in C++ and runs much faster than legacy conda. Conda environments are created using configuration files in yaml format (yaml is a type of configuration file), where you specify the name of the environment, the conda channels to search, and then the programs to install. You can optionally specify a version for each program, or just list the name and have the default version installed. For example, `- bwa` or `- bwa ==0.7.17` with both install version `0.7.17`, but you could list a different version as needed. Further, some programs you may need do not play well with conda, or are simply not available. If you run into lots of errors while trying to install something, consider installing via pip (python package manager) or downloading a binary (pre compiled version of software). Make sure if you install anything in addition to the conda environment, you do it after activating the environment. 

To create the conda environment, first install mamba:
```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge
```
Now add mamba to your path.
```
export PATH="/home/ec2-user/mambaforge/bin:$PATH"
```
List your current conda environments.
```
conda info --envs 
```
Now create the conda environment with all of your desired packages. Note that the file name doesn't matter if you have the name designation at the top of the yaml file. If you don't name the environment in the yaml, then it will be named whatever your file is named. Or you can add a -n flag to name the environment (`mamba env create -f environment.yaml -n your_name_of_choice`).
```
mamba env create -f envs/environment.yaml
```
Now list your environments again to find the path of your new environment.
```
conda info --envs 
```
Now activate your environment using the path printed from the previous command. 
```
conda activate /home/ec2-user/mambaforge/envs/$ENVNAME
```
Now test your environment by running one of the programs you just installed. For example, type `bwa` (if you installed bwa!).

If you want to create an environment in a SageMaker Notebook, follow [these instructions](https://github.com/aws/studio-lab-examples/blob/main/custom-environments/custom_environment.ipynb). 

## **Clusters** <a name="CLU"></a>
One great thing about the cloud is its ability to scale with demand. When you submit a job to a traditional cluster, you specify up front how many CPUs and memory you want to give to your job, and you may over or under utilize these resources. With cloud resources like serverless and clusters  you can leverage a feature called autoscaling, where the compute resources will scale up or down with the demand. This is more efficient and keeps costs down when demand is low, but prevents latency when demand is high (think Black Friday shopping on a website). For most users of Cloud Lab, the best way to leverage scaling is to use AWS Batch, but in some cases, maybe for a whole lab group or large project, it may make sense to spin up a [Kubernetes cluster](https://aws.amazon.com/kubernetes/). Note that if you spin up resources in Batch, that you need to deactivate the compute environment (in Batch) and delete the autoscaling groups (in EC2) to avoid further charges.

## **Billing and Benchmarking** <a name="BB"></a>
Many Cloud Lab users are interested in understanding how to estimate the price of a large scale project using a reduced sample size. Generally, you should be able to benchmark with a few representative samples to get an idea of time and cost required for a larger scale project. In terms of cost, the best way to estimate costs is to use the AWS pricing calculator [here](https://aws.amazon.com/ec2/pricing/on-demand/) for an initial figure, which is a pricing tool that forcasts costs based on products and useage. Then, you can run some benchmarks and double check that everything is acting as you expect. For example, if you know that your analysis on your on-premesis cluster takes 4 hours to run for a single sample with 12 CPUs, and that each sample needs about 30 GB of storage to run a workflow, then you can extrapolate out how much everything may cost using the calculator (e.g. EC2 + S3). To check on costs, go to `Services > Billing`. From there, the `AWS Billing Dashboard` will prove useful, as well as the `Bills` tab. You can drill into each expense and see what each notebook is costing you for example. `AWS Cost Explorer` will probably also prove helpful.

## **Cost Optimization** <a name="COST"></a>
As you go through all the tutorials, you can keep costs down by stopping and/or deleting resources (e.g. EC2 or S3) you no longer need. Enabling S3 Intelligent Tiering will also help with S3 data, although this is more appropriate to longer-term projects than Cloud Lab. Some workflows like Cromwell on AWS will spin up infrastructure under `Cloud Formation`. Make sure you delete all those stacks when you are finished with them. You also need to go to Batch and deactivate your compute environment, and go to EC2 and delete your autoscaling groups. Another strategy is to ensure that you are using all the compute resources you have provisioned. If you spin up a VM with 16 CPUs, you can see if they are all being utilized using [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SingleMetricPerInstance.html). If you are only really using 8 CPUs for example, then just change your machine size to fit the analysis. Finally, you can play with [Spot](https://aws.amazon.com/ec2/spot/?cards.sort-by=item.additionalFields.startDateTime&cards.sort-order=asc&trk=8e336330-37e5-41e0-8438-bc1c75320d09&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2%20Spot|US|EN|Text&s_kwcid=AL!4422!3!517520538473!e!!g!!ec2%20spot%20instances&ef_id=Cj0KCQjwgYSTBhDKARIsAB8KuksD7LV6FQEACly0PY4VJnEIONcvLuFG_Tq5RWp1p3OQkFbhBDRSjQcaAlMHEALw_wcB:G:s&s_kwcid=AL!4422!3!517520538473!e!!g!!ec2%20spot%20instances) or [Reserved](https://aws.amazon.com/ec2/pricing/reserved-instances/) instances for running workflows and end up saving a lot of money. 

## **Getting Support** <a name="SUP"></a>
As part of your participation in Cloud Lab you will be added to the Cloud Lab Teams channel where you can chat with other Cloud Lab users, and gain support from the Cloud Lab team. For NIH Intramural users, you can submit a support ticket to Service Now. For all other users, you can reach out to the Cloud Lab email with questions at `CloudLab@nih.gov`. Please be sure for tickets and email to have a clear Subject line, such as AWS help with Nextflow and BATCH. For issues our team is unable to resolve, you can reach out to AWS support directly by clicking the question mark in the top right part of the console. 

If you have a question about Quota Limits, visit our [documentation](/docs/service_quotas.md) on how to request a limit increase. 

## **Additional Training** <a name="TR"></a>
This repo only scratches the surface of what can be done in the cloud. If you are interested in additional cloud training opportunities please visit the [STRIDES Training page](https://cloud.nih.gov/training/). For more information on the STRIDES Initiative at the NIH, visit [our website](https://cloud.nih.gov) or contact the NIH STRIDES team at STRIDES@nih.gov for more information.

