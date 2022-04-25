# AWS Tutorial Resources

_We have pulled together a variety of tutorials here from disparate sources. Some use EC2, or the aws genomics CLI, and other use notebooks. Tutorials are organized by research method, but we try to designate what AWS services are used as well to help you navigate._
---------------------------------
## Overview of Page Contents

+ [Biomedical Workflows on AWS](#Bio)
+ [Variant Calling](#VC)
+ [GWAS](#GWAS)
+ [Medical Imaging](#IM)
+ [RNAseq](#RNA)
+ [scRNAseq](#sc)
+ [Long Read Sequencing Analysis](#Long)
+ [AI/ML Pipeline](#AI)

## **Biomedical Workflows on AWS** <a name="Bio"></a>

There are a lot of ways to run workflows on AWS. Here we list a few posibilities each of which may work for different research aims. As you walk through the various tutorials below, think about how you could possibly run that workflow more efficiently using a one of the other methods listed here.

- The most simple is probably to spin up an EC2 instance, and run your command interactively, or using `screen` or, as a [startup script](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) attached as metadata. See the [GWAS tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud) below for more info on how to run a pipeline using EC2. 
- You could also run your pipeline via a Sagemaker notebook, either by splitting out each command as a different block, or by running a workflow manager (Nextflow etc.). See [here](https://aws.amazon.com/blogs/machine-learning/scheduling-jupyter-notebooks-on-sagemaker-ephemeral-instances/) about scheduling a notebook to let it run longer. You can find some example notebooks in the [tutorials below](/tutorials/notebooks/).
- You can interact with `AWS Batch` using a workflow manager like [Nextflow](https://www.nextflow.io/docs/latest/awscloud.html) or [Cromwell](https://docs.opendata.aws/genomics-workflows/orchestration/cromwell/cromwell-overview.html), which both leverage the [AWS Genomics Workflows Pipeline](https://docs.opendata.aws/genomics-workflows/index.html), so visit that link to automate the creation of genomics resources.
- If you want to build a lasting pipeline that you plan to run many times, you could consider using [this solution](https://docs.aws.amazon.com/solutions/latest/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch/components.html) using `Step Functions` and `AWS Batch`. The github for that solution is found [here](https://github.com/awslabs/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch). This is really for advanced users so make sure you are very experienced in AWS before trying, and in most cases this is probably not needed. An automated version from the genomics workflows page is found [here](https://docs.opendata.aws/genomics-workflows/orchestration/step-functions/step-functions-overview.html).
- You will be able (soon) to leverage the serverless functionality of AWS using the [AWS Genomics CLI](https://aws.amazon.com/genomics-cli/), which automates genomic workflows similar to the above links, but with a simplified command line interface. This feature does not yet work within Cloud Lab due to some peculiarities of the environment, so check our [documentation](/docs/agc.md) for periodic updates on access. We are actively working on integrating this tool into Cloud Lab. In the mean time, stick with the solution [here](https://docs.opendata.aws/genomics-workflows/index.html).
- Finally, one benefit of the cloud is access to GPUs for workflow acceleration. While a lot of focus on GPU implementation will focus on AI/ML workflows, NVIDIA has software called Parabricks that will accelerate genomic workflows for pretty low costs. See the full list of command line options [here](https://docs.nvidia.com/clara/parabricks/v3.5/text/software_overview.html) to see if your specific workflow is accelerated. Specific details on how to use the Parabricks within Cloud Lab are detailed in the next section (Variant Calling).
 
 **Be warned, GPU machines will burn through your budget very quickly if left running, so be sure to shut these machines down after use. You may also encounter service quotas to protect you from burning through your budget too quickly. If that happens, and you still want to use a certain instance type, follow these [instructions](/docs/service_quotas.md).**

## **Variant Calling** <a name="VC"></a>

- This [AWS blog](https://aws.amazon.com/blogs/industries/running-gatk-workflows-on-aws-a-user-friendly-solution/) describes running the GATK pipeline on 1k genomes samples using Nextflow and AWS Batch. View it as an example of what is possible, but to actually repeat their analysis, use [Nextflow on AWS](https://docs.opendata.aws/genomics-workflows/orchestration/nextflow/nextflow-overview.html) with the GATK pipeline from [Sequera Labs](https://github.com/seqeralabs/gatk4-germline-snps-indels).
- Another [AWS blog](https://aws.amazon.com/blogs/industries/using-structural-variant-analysis-on-aws-with-amazon-fsx-for-lustre-in-novel-therapeutic-discovery/) focuses on structural variant calling, and the team that wrote it ran [GATK-SV](https://github.com/broadinstitute/gatk-sv) using [Cromwell on AWS](https://docs.opendata.aws/genomics-workflows/orchestration/cromwell/cromwell-overview.html).
- As mentioned above, NVIDIA Parabricks can be used to accelerate genomic workflows and especially variant calling. To give you an idea of the potential acceleration, you can expect that on a 32 CPU machine, a 30x human genome (HG002) will take about 30 hours to run GATK HaplotypeCaller. With Parabricks, you can run the same pipeline with 8 GPUs in ~40 minutes. To use Parabricks on AWS follow our instructions in the [docs](/docs/parabricks.md). If you run into a service quota on the GPU instance, follow our [documentation](/docs/service_quotas.md) to resolve it.

## **Genome Wide Association Studies** <a name="GWAS"></a>

- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using EC2. Note that the CFDE page has a few other bioinformatics related tutorials like BLAST and Illumina read simulation. We also converted this tutorial to a simplified [notebook version](/tutorials/notebooks/GWAS) if you prefer that format. See the Sagemaker Notebook instructions on the AWSJumpstart page for help getting that running.
- Terra has a [GWAS workspace](https://app.terra.bio/#workspaces/amp-t2d-op/2019_ASHG_Reproducible_GWAS-V2) that walks through a few tutorials and has links to public data for testing GWAS. If you have access to Terra or Biodata Catalyst you can port the notebooks into Sagemaker, if not, then skip this one.

## **Medical Imaging** <a name="IM"></a>
- Most medical imaging analyses are done in notebooks, so we would recommend accessing this [Jupyter Notebook](BrainTumorSegmentation) and importing or cloning it into Sagemaker. The tutorial walks through brain image segmentation.
- AWS has a nice intro to Machine Learning in a Sagemaker notebook that predicts breast cancer from features extracted from image data, which walks you through both image analysis and some of the ML functionality of Sagemaker, the notebook is found [here](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_applying_machine_learning/breast_cancer_prediction/Breast%20Cancer%20Prediction.ipynb).
- You can also view this [AWS blog](https://aws.amazon.com/blogs/machine-learning/annotate-dicom-images-and-build-an-ml-model-using-the-monai-framework-on-amazon-sagemaker/) on how to annotate dicom images and build a custom AI model with the data.
- You can learn to deidentify medical images following this AWS [tutorial](https://aws.amazon.com/blogs/machine-learning/de-identify-medical-images-with-the-help-of-amazon-comprehend-medical-and-amazon-rekognition/).
- Download NVIDIA's example [Medical Imaging Notebook](https://developer.nvidia.com/run-jupyter-notebooks). Note that there are other interesting notebooks on that site, but be warned that most of the NVIDIA notebooks require a GPU, so be careful about spinning up expensive resources and not shutting them down! Again, you may need to request the lifting of a [service quota](/docs/service_quotas.md) on the GPU machine.

## **RNAseq** <a name="RNA"></a>
- You can run this [Nextflow tutorial](https://nf-co.re/rnaseq/usage) for RNAseq a variety of ways on AWS. Following the instructions outlined above, you could use EC2, the Amazon Genomics CLI (in the near future), AWS Batch, Sagemaker, or using functions + [Batch](https://www.nextflow.io/docs/latest/awscloud.html#:~:text=Nextflow%20requires%20to%20access%20the%20AWS%20command%20line,Docker%20image%20%28s%29%20used%20during%20the%20pipeline%20execution).
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification from [the University of Maine INBRE](https://github.com/MaineINBRE/rnaseq-myco-tutorial) use this [Notebook](rnaseq-myco-tutorial-main). 
- There is also this NIH-written tutorial to use [Kids First data on Cavatica](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/RNAseq-on-Cavatica/rna_seq_1/). Note that you will need to pre-register for both kids first data and Cavatica access.

## **Single Cell RNAseq** <a name="sc"></a>
- This [AWS blog](https://aws.amazon.com/blogs/publicsector/driving-innovation-single-cell-analysis-aws/) lays out a potential method that integrates a lot of the AWS native tools for running an scRNAseq pipeline. It is less of a tutorial, and more of a demo of what is possible.
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the github that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. If you want a CPU version that users Scanpy you can use this [notebook](https://github.com/clara-parabricks/rapids-single-cell-examples/blob/master/notebooks/hlca_lung_cpu_analysis.ipynb). Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks. Create a conda environment in the terminal, then run the notebook. Consider using [mamba](https://github.com/mamba-org/mamba) to speed up environment creation. 

## **Long Read Sequence Analysis** <a name="Long"></a>
Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. Access the notebooks [here](https://labs.epi2me.io/nbindex/). Note that these notebooks expect you are running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks. If you are just looking to try out notebooks, don't start with these. If you are interested in long read sequence analysis, then some troubleshooting may be needed to adapt these to the Cloud Lab environment. You may even need to rewrite them in a fresh notebook by adapting the commands.

## **AI/ML Pipelines** <a name="AI"></a>
AWS is moving all AI/ML workflows to Sagemaker, the Juptyer notebook platform we have used a few times already. AWS has a very general tutorial [here](https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/) on how to build out an AI pipeline on Sagememaker. You can also look at the breast cancer tutorial in the imaging section above for a more applied example. 
You can also submit a training job to Sagemaker, and have your final model uplaoded to S3 using [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#train-a-model-with-pytorch), [Tensorflow](https://docs.aws.amazon.com/sagemaker/latest/dg/tf.html) or [Apache MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/mxnet.html).
