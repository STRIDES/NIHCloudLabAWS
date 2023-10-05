# Installing the AWS ParallelCluster User interface (UI)

 ## To install an instance of the AWS ParallelCluster UI choose an AWS Cloud Formation quick-create link for the AWS region you want the cluster in.
  
  The AWS ParallelCluster UI is a web-based user interface that mirrors the AWS ParallelCluster pcluster CLI, while providing a console-like experience. You install and access the AWS ParallelCluster UI in your AWS account. When you run it, the AWS ParallelCluster UI accesses an instance of the AWS ParallelCluster API hosted on Amazon API Gateway in your AWS account.
  
  Follow the instructions [here](https://docs.aws.amazon.com/parallelcluster/latest/ug/install-pcui-v3.html), once UI is deployed the link should direct you to the UI and should look like :

   ![parallel cluster UI image](/docs/images/ParallelclusterUI.PNG)

 ### Create and Configure ParallelCluster using the UI without pre-made templates
 
   1. In the AWS ParallelCluster UI Clusters view, choose Create cluster, Step by step.

   2. In Cluster, Name, enter a name for your cluster.

   3. Choose a VPC and a subnet for your cluster, and choose Next.

   4. In Head node, choose Add SSM session, and choose Next.

   5. In Queues, Compute resources, choose 1 for Static nodes.

   6. Choose and instance type, and choose Next.

   7. In Storage, select desired shared storage type or stay with default options and choose Next.

   8. In Cluster configuration, review the cluster configuration YAML and choose Dry run to validate it.

   9. Choose Create to create your cluster, based on the validated configuration.

   10. After a few seconds, the AWS ParallelCluster UI automatically navigates you back to Clusters, where you can monitor the cluster create status and Stack events.

   11. Choose Details to see cluster details, such as the version and status.

   12. Choose Instances to see the list of EC2 instances and status.

   13. Choose Stack events to view cluster stack events, and a AWS Management Console link to the CloudFormation stack that creates the cluster.

   14. In Details, after cluster creation completes, choose View YAML to view or download the cluster configuration YAML file.

   15. After cluster creation completes, choose Shell to access the cluster head node.
 
# Installing the AWS ParallelCluster CLI:

    - Using a virtual environment (recommended)
    - Using a conda virtual environment 
 
 We recommend conducting all steps within AWS Cloud Shell, but you could also use a small Ec2 instance or your local machine's terminal.     

 ## 1.0 Install within pip virtual environment
 
 ## 1.1 Install pip virtual environment
 
  If virtualenv is not installed, install virtualenv using pip3

        -Linux, macOS, or Unix
      
            $ python3 -m pip install --upgrade pip
            $ python3 -m pip install --user --upgrade virtualenv
     

        -Windows
    
            $ pip3 install --user --upgrade virtualenv

 
 ### 1.2 Create a pip virtual environment and name it

         -Linux, macOS, or Unix
          
            $ python3 -m virtualenv ~/name
        

        -Windows
        
            C:\>virtualenv %USERPROFILE%\name

 ### 1.3 Activate your new virtual environment
 
        -Linux, macOS, or Unix
          
            $ source ~/name/bin/activate
        
        -Windows
        
            C:\>%USERPROFILE%\name\Scripts\activate

 ### 1.4 Install AWS ParallelCluster into your virtual environment.

        -Linux, macOS, or Unix
          
            (name)~$ python3 -m pip install --upgrade "aws-parallelcluster<3.0"
        
        -Windows
        
            (apc-ve) C:\>pip3 install --upgrade "aws-parallelcluster<3.0"

 ## 2.0 Install within conda virtual environment
 
 ### 2.1 (Optional) Install mamba
 ```
curl -L -O https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-$(uname)-$(uname -m).sh
bash Mambaforge-$(uname)-$(uname -m).sh -b -p $HOME/mambaforge
# Add to your PATH
export PATH="$HOME/mambaforge/bin:$PATH"
```
 ### 2.2 Create environment and install parallel cluster
 ```
 mamba create -n pcluster -c conda-forge aws-parallelcluster -y
 ```
 
 ### 2.3 Activate environment
 ```
 source activate pcluster
 ```
 Or, using mamba activate
 ```
 mamba init
 mamba activate pcluster
 ```

 ## 4. Verify that AWS ParallelCluster is installed correctly
               
        -Linux, macOS, or Unix
          
            $ pcluster version
        
        -Windows
        
            (apc-ve) C:\>pcluster version

    Output should display version number.

 ## 5. Move on to configuring and connecting to your cluster
 Follow the [next instructions]([https://github.com/STRIDES/NIHCloudLabAWS/blob/main/docs/Configure_AWSParallelCluster.md) on how to configure your cluster.



