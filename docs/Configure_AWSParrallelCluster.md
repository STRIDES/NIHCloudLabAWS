**1. Setup your AWS crednetials**

    To connect to your AWS console enter AWS Access Keys:
        *$ aws configure*

          AWS Access Key ID [None]: ABCDEFGHIJKLEXAMPLE
          AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
          Default AWS Region name [us-east-1]: us-east-1
          Default output format [None]:

**2. Configure your Parrallel Cluster**
    
    run the following command:
        -pcluster configure

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

 The head and compute nodes instance types are entered. For instance types, your account instance limits are large enough to meet your requirements, [instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html#ec2-on-demand-instances-limits):

                Master instance type [instance type]: 
                Compute instance type [instance type]: 

    
The key pair is selected from the key pairs registered with Amazon EC2 in the selected AWS Region:

            Allowed values for EC2 Key Pair Name:
                1. example1-uswest1-key
                2. example2-uswest1-key

After the previous steps are completed, decide whether to use an existing VPC or let AWS ParallelCluster create a VPC for you. If you don't have a properly configured VPC, AWS ParallelCluster can create a new one. It either uses both the head and compute nodes in the same public subnet, or only the head node in a public subnet with all nodes in a private subnet. It's possible to reach your limit on number of VPCs in a AWS Region. The default limit is five VPCs for each AWS Region

    Automate VPC creation? (y/n) [n]: y
    Allowed values for Network Configuration:
        1. Master in a public subnet and compute fleet in a private subnet
        2. Master and compute fleet in the same public subnet

If you don't create a new VPC, you must select an existing VPC:

    Automate VPC creation? (y/n) [n]: n
    Allowed values for VPC ID:
    #  id                     name                                 number_of_subnets
    ---  ---------------------  ---------------------------------  -------------------
    1  vpc-0b4ad9c4678d3c7ad  ParallelClusterVPC-20200118031893                    2
    2  vpc-0e87c753286f37eef  ParallelClusterVPC-20191118233938                    5


After the VPC has been selected, you need to decide whether to use existing subnets or create new ones:

    Automate Subnet creation? (y/n) [y]: y

Wait for configuration file to be created:

    Creating CloudFormation stack...
    Do not leave the terminal until the process has finished


When you have completed the preceding steps, a simple cluster launches into a VPC. The VPC uses an existing subnet that supports public IP addresses, if public IP addresses are not supported then check here (placeholder for network config link?)


**3. Launch Cluster**

     When all settings contain valid values, you can launch the cluster by running the create command:

    $ pcluster create nameofcluster

After the cluster reaches the "CREATE_COMPLETE" status, you can connect to it by using your normal SSH client settings.
    
