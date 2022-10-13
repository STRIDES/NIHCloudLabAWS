# How to build a Docker container and push to the Elastic Container Registry

This doc outlines how to create a Docker container and how to push that container to the Amazon Elastic Container Registry. Find more info [here](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html)

## Create an Elastic Container Registry

1. Navigate to the Elastic Container Registry Page. It's easiest to just search at the top. 

<img src="/docs/images/1_find_ecr.png" width="550" height="225">

2. Click **CREATE REPOSITORY**

<img src="/docs/images/2_create_registry.png" width="550" height="200">

3. Fill in the details and click **Create repository**. For this example, name your repository `bamtools-example`.

<img src="/docs/images/3_general_settings.png" width="550" height="700">

## Build and Stage your Container

We are going to use an example [Dockerfile](https://github.com/BioContainers/containers/blob/master/bamtools/2.4.0/Dockerfile) for BAMtools from [BioContainers](https://github.com/BioContainers/containers) to build a quick container just to practice pushing to Artifact Registry. Copy that file locally and save as `Dockerfile`.

From within a compute environment (Sagemaker, EC2, or Cloud Shell), run the following: 

`docker build -t bamtools:latest . --no-cache`

Test your container by running it and make sure Bamtools is available. 

`docker run bamtools:latest bamtools -h`

Authenticate to the registry. 

`aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com`

List your local images, and find the Image ID.

`docker images`

<img src="/docs/images/4_list_docker_images.png" width="550" height="75">

Tag the container to the registry.

`docker tag <IMAGE_ID> aws_account_id.dkr.ecr.region.amazonaws.com/my-repository:tag`

Now push to the Registry.

`docker push aws_account_id.dkr.ecr.region.amazonaws.com/my-repository:tag`

Pull the container and make sure it all works as expected. 

`docker pull aws_account_id.dkr.ecr.region.amazonaws.com/my-repository:tag`

