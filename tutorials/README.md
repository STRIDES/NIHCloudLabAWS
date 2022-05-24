# AWS Tutorial Resources

---------------------------------
## Overview of Page Contents

+ [Biomedical Workflows on AWS](#Bio)
+ [GWAS](#GWAS)
+ [Medical Imaging](#IM)
+ [RNAseq](#RNA)
+ [scRNAseq](#sc)
+ [Long Read Sequencing Analysis](#Long)
+ [AI/ML Pipeline](#AI)
+ [Open Data](#OPEN)

## **Biomedical Workflows on AWS** <a name="Bio"></a>

There are a lot of ways to run workflows on AWS. Here we list a few possibilities each of which may work for different research aims. As you walk through the various tutorials below, think about how you could possibly run that workflow more efficiently using a one of the other methods listed here. If you are unfamiliar with any of the terms or concepts here, please review the [AWS 101](https://github.com/STRIDES/NIHCloudLabAWS) page. 

- The most simple is probably to spin up an EC2 instance, and run your command interactively, or using `screen` or, as a [startup script](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) attached as metadata. See the [GWAS tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud) below for more info on how to run a pipeline using EC2. 
- You could also run your pipeline via a SageMaker notebook, either by splitting out each command as a different block, or by running a workflow manager (Nextflow etc.). See [here](https://aws.amazon.com/blogs/machine-learning/scheduling-jupyter-notebooks-on-sagemaker-ephemeral-instances/) about scheduling a notebook to let it run longer. You can find some example notebooks in the [tutorials below](/tutorials/notebooks/).
- You will be able (soon) to leverage the serverless functionality of AWS using the [AWS Genomics CLI](https://aws.amazon.com/genomics-cli/), which automates genomic workflows similar to the above links, but with a simplified command line interface. We are waiting on a new version of the CLI that will be compatible with the Cloud Lab environment, so check our [documentation](/docs/agc.md) for periodic updates on access. We are actively working on integrating this tool into Cloud Lab. In the mean time, work with the alternative solution [here](https://docs.opendata.aws/genomics-workflows/index.html) and see our [docs](/docs/Genomics_Workflows.md) for tips and tricks to get these templates to work in Cloud Lab.
- Finally, one benefit of the cloud is access to GPUs for workflow acceleration. While a lot of focus on GPU implementation will focus on AI/ML workflows, NVIDIA has software called Parabricks that will accelerate genomic workflows for pretty low costs. See the full list of command line options [here](https://docs.nvidia.com/clara/parabricks/v3.5/text/software_overview.html) to see if your specific workflow is accelerated. Specific details on how to use the Parabricks within Cloud Lab are detailed in the next section (Variant Calling).
 
 **Please note, GPU machines cost more than most CPU machines, so be sure to shut these machines down after use. You may also encounter service quotas to protect you from the accidental use of expensive machine types. If that happens, and you still want to use a certain instance type, follow these [instructions](/docs/service_quotas.md).**

## **Genome Wide Association Studies** <a name="GWAS"></a>

Genome wide association studies, or GWAS, are statistical analyses that look for associations between genomic variants and phenotypic traits.
- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using EC2. Note that the CFDE page has a few other bioinformatics related tutorials like BLAST and Illumina read simulation. We also converted this tutorial to a simplified [notebook version](/tutorials/notebooks/GWAS) if you prefer that format. See the SageMaker Notebook instructions on the AWS 101 page for help getting that running.

## **Medical Imaging Analysis** <a name="IM"></a>
Medical imaging analysis requires the analysis of large image files and often requires elastic storage and accelerated computing.
- Most medical imaging analyses are done in notebooks, so we would recommend accessing this [Jupyter Notebook](/tutorials/notebooks/SpleenLiverSegmentation) and importing or cloning it into SageMaker. The tutorial walks through image segmentation.
- AWS has a nice intro to Machine Learning in a SageMaker notebook that predicts breast cancer from features extracted from image data, which walks you through both image analysis and some of the ML functionality of SageMaker, the notebook is found [here](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_applying_machine_learning/breast_cancer_prediction/Breast%20Cancer%20Prediction.ipynb).
- You can also view this [AWS blog](https://aws.amazon.com/blogs/machine-learning/annotate-dicom-images-and-build-an-ml-model-using-the-monai-framework-on-amazon-sagemaker/) on how to annotate DICOM images and build a custom AI model with the data.
- You can learn to deidentify medical images following this AWS [tutorial](https://aws.amazon.com/blogs/machine-learning/de-identify-medical-images-with-the-help-of-amazon-comprehend-medical-and-amazon-rekognition/).

## **RNAseq** <a name="RNA"></a>
RNAseq is a technique for quantifying gene levels of gene expression across the genome. 
- You can run this [Nextflow tutorial](https://nf-co.re/rnaseq/3.7) for RNAseq a variety of ways on AWS. Following the instructions outlined above, you could use EC2, SageMaker, or AWS Batch(/docs/Genomics_Workflows.md).
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification from [the University of Maine INBRE](https://github.com/MaineINBRE/rnaseq-myco-tutorial) use this [Notebook](rnaseq-myco-tutorial-main). 

## **Single Cell RNAseq** <a name="sc"></a>
Single Cell RNAseq (scRNAseq) analyses allow for gene expression profiling at the single cell level.
- This [AWS blog](https://aws.amazon.com/blogs/publicsector/driving-innovation-single-cell-analysis-aws/) lays out a potential method that integrates a lot of the AWS native tools for running an scRNAseq pipeline. It is less of a tutorial, and more of a demo of what is possible.
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the GitHub that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. If you want a CPU version that users Scanpy you can use this [notebook](https://github.com/clara-parabricks/rapids-single-cell-examples/blob/master/notebooks/hlca_lung_cpu_analysis.ipynb). Pay careful attention to the environment setup as there are a lot of dependencies for these notebooks. Create a conda environment in the terminal, then run the notebook. Consider using [mamba](https://github.com/mamba-org/mamba) to speed up environment creation. 

## **Long Read Sequence Analysis** <a name="Long"></a>
Long read DNA sequence analysis involves analyzing sequencing reads typically longer than 10 thousand base pairs (bp) in length, compared with short read sequencing where reads are about 150 bp in length.
Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. Access the notebooks [here](https://labs.epi2me.io/nbindex/). Note that these notebooks expect you are running locally and accessing the epi2me notebook server. To run them in Cloud Lab, skip the first cell that connects to the server and then the rest of the notebook should run correctly, with a few tweaks. If you are just looking to try out notebooks, don't start with these. If you are interested in long read sequence analysis, then some troubleshooting may be needed to adapt these to the Cloud Lab environment. You may even need to rewrite them in a fresh notebook by adapting the commands.

## **AI/ML Pipelines** <a name="AI"></a>
Artificial intelligence and machine learning algorithms are being applied to a variety of biomedical research questions, ranging from image classification to genomic variant calling. AWS is moving all AI/ML workflows to SageMaker, the Juptyer notebook platform we have used a few times already. AWS has a very general tutorial [here](https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/) on how to build out an AI pipeline on Sagememaker. You can also look at the breast cancer tutorial in the imaging section above for a more applied example. 
You can also submit a training job to SageMaker, and have your final model uploaded to S3 using [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#train-a-model-with-pytorch), [Tensorflow](https://docs.aws.amazon.com/sagemaker/latest/dg/tf.html) or [Apache MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/mxnet.html).

## **Open Data** <a name="OPEN"></a>
AWS has a lot of public data that you can integrate into your testing or use in your own research. You can access these datasets at the [Registry of Open Data on AWS](https://registry.opendata.aws/). There you can click on any of the datasets to view the S3 path to the data, as well as publications that have used those data and tutorials if available. To demonstrate, we can click the [gnomad dataset](https://registry.opendata.aws/broad-gnomad/), then get the S3 path and view the files at the command line by pasting `https://registry.opendata.aws/broad-gnomad/`. 
