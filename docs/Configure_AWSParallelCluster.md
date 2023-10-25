## Configuring AWS Parallel Cluster
Make sure that you have parallel cluster installed first [link](https://docs.aws.amazon.com/parallelcluster/latest/ug/install-v3-parallelcluster.html).

### 1. Setup your AWS credentials

To connect to your AWS console paste in your Short Term Access Keys following [these instructions](/docs/Intramural_STAKs.md). These should last 12 hours, and although normally you could just enter the key and secret key using aws configure, with short term keys you also need the session token, so make sure you include that. 

Next, use aws configure to set your default region: 
    
`aws configure`

          AWS Access Key ID [None]: ABCDEFGHIJKLEXAMPLE
          AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
          Default AWS Region name [us-east-1]: us-east-1
          Default output format [None]:

### 2. Configure your Parallel Cluster
    
Run the following command: 
`pcluster configure`

Once command is run the following configuration options will display:

    Pick a region:

           Allowed values for the AWS Region ID:
                1. af-south-1
                2. ap-east-1
                3. ap-northeast-1
                4. ap-northeast-2
                5. ap-south-1
                6. ap-southeast-1
                7. ap-southeast-2
                8. ca-central-1
                9. eu-central-1
                10. eu-north-1
                11. eu-south-1
                12. eu-west-1
                13. eu-west-2
                14. eu-west-3
                15. me-south-1
                16. sa-east-1
                17. us-east-1
                18. us-east-2
                19. us-west-1
                20. us-west-2
    
Choose the scheduler to use with your cluster:

        Allowed values for Scheduler:
                1. slurm
                2. awsbatch
                
Choose an operating system:

        Allowed values for Operating System:
                1. alinux2
                2. centos7
                3. ubuntu1804
                4. ubuntu2004

The minimum and maximum size of the cluster of compute nodes is entered. This is measured in number of instances:
                
                Minimum cluster size (instances) [0]:
                Maximum cluster size (instances) [10]: 

The head and compute nodes instance types are entered. For instance types, your account instance limits are large enough to meet your requirements, [instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits). You can select something really small for the head node (Master) since it is just handling scheduling, and then compute is up to you based on requirements.

                Master instance type [instance type]: 
                Compute instance type [instance type]: 

    
The key pair is selected from the key pairs registered with Amazon EC2 in the selected AWS Region. If you do not yet have a key pair, go to the EC2 console and [create one](/docs/connect_to_EC2.md): 

            Allowed values for EC2 Key Pair Name:
                1. example1-uswest1-key
                2. example2-uswest1-key

After the previous steps are completed, decide whether to use an existing VPC or let AWS ParallelCluster create a VPC for you. If you don't have a properly configured VPC, AWS ParallelCluster can create a new one. It either uses both the head and compute nodes in the same public subnet, or only the head node in a public subnet with all nodes in a private subnet. It's possible to reach your limit on number of VPCs in a AWS Region. The default limit is five VPCs for each AWS Region. 

**For Cloud Lab accounts we recommend you do not try to create a VPC, but rather use the existing VPCs associated with your account. When it asks for your VPC, just paste in one of the two options it gives you**.

If you don't create a new VPC, you must select an existing VPC:

    Automate VPC creation? (y/n) [n]: n
    Allowed values for VPC ID:
    #  id                     name                                 number_of_subnets
    ---  ---------------------  ---------------------------------  -------------------
    1  vpc-ID  ParallelClusterVPC-NUMBER                    2
    2  vpc-ID  ParallelClusterVPC-NUMBER                    5


After the VPC has been selected, you need to decide whether to use existing subnets or create new ones. Again for Cloud Lab accounts select **No**:

    Automate Subnet creation? (y/n) [n]: n
    
    Allowed values for head node Subnet ID:
    #  id                        name                                                                       size  availability_zone
    ---  ------------------------  -----------------------------------------------------------------------  ------  -------------------
    1  subnet-ID  Subnet1_name     32  us-east-1b
    2  subnet-ID  Subnet2_name      32  us-east-1a

**Paste in one of the subnet IDs**

### 3. Launch Cluster

Before launching the default configuration allows public IP addresses, which typically is not allowed in the NIH environment , to fix this:

      Modify the pcluster config file (Will be in a hidden file in directory you installed and configured the Parrallel Cluster), the default name of the Pcluster configuration file is "config"

        $ vi ~/.parallelcluster/config 
      
      add a line under the "[vpc_default]" block 

         use_public_ips = false

      once line is added make sure to save the file:

         wq!


 When all settings contain valid values, you can launch the cluster by running the create command:

    $ pcluster create <nameofcluster>

After the cluster reaches the "CREATE_COMPLETE" status, you can connect to it by using your normal SSH client settings.

## 4. Deactivate venv when finished working

To deactivate a pip environment, just type `deactivate`.
For conda environment type `conda deactivate`.
    
