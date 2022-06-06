### Using the Amazon Genomics CLI (agc) in Coud Lab

The following instructions follow the [AWS docs](https://aws.github.io/amazon-genomics-cli/docs/), but with some tips and tricks specific to Cloud Lab. Read more about the specifics of the agc tool in the [docs](https://aws.github.io/amazon-genomics-cli/docs/concepts/).

You can do all of the following from your local computer using the AWS SDK, but to ensure things go smoothly in the Cloud Lab environment, we recommend you spin up a VM and follow along from within your EC2 or Sagemaker instance. If using Sagemaker, it is easier to use the terminal than a notebook, but both ways should work. Do not use Cloud Shell, because Cloud Shell is ephemeral and will not save your environment between sessions.

Because agc uses AWS Batch for computation, you can get away with spinning up a small VM, like the t2 micro for this tutorial. Once you VM is ready, ssh into it. If you are using a notebook, open the Jupyter environment.

Make sure you set up your environment following the [Prerequisites](https://aws.github.io/amazon-genomics-cli/docs/getting-started/prerequisites/) page. Install the AWS CLI if running locally, and if on EC2 or Sagemaker, you just need to install nodejs. Make sure you run `aws configure` and input your Short-term Access keys. Intramural users can access keys following [these instructions](/docs/STAKs_intramural.md). 

Now run the [install instructions](https://aws.github.io/amazon-genomics-cli/docs/getting-started/installation/) and add agc to the path with `export PATH=$HOME/bin:$PATH`. If the install went well, go ahead and activate. You need to add a few flags to the base `activate` command. Create the bucket before running this command, and make sure that the bucket is empty. 
```
agc account activate --vpc <vcp-id> --subnets <subnet1> --subnets <subnet2> --bucket <bucket-name>
```

If for some reason the activation fails, you need to go to s3 and delete the bucket agc created and then try again. If you can't get the account to activate after a few attempts, start from scratch with this command `agc account deactivate --force`. 

If everything works, then it will take about 4 minutes to finish bootstrapping the infrastructure. Now configure you email (`agc configure email you@youremail.com`) and you are all set up! 

Now try running some examples. You can start with the [Hello World example](https://aws.github.io/amazon-genomics-cli/docs/getting-started/helloworld/) or skip ahead to the other [tutorials](https://aws.github.io/amazon-genomics-cli/docs/tutorials/). If a context deployment fails, go to `Cloud Formation` in the AWS console and delete the responsible stack, then try again. 

Once in a project, you can list the available contexts with `agc context list`, and you can list the available workflows with `agc workflow list`. If you want to check on any of the agc commands, just type `agc` or agc + subcommand like `agc workflow` and you will get a help menu. 

