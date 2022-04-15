# AWS Tutorial Resources

_We have pulled together a variety of tutorials here from disparate sources. Some use EC2, or aws genomics CLI, and other use notebooks. Tutorials are organized by research method, but we try to designate what AWS services are used as well to help you navigate._
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



## **Biomedical Workflows on AWS** <a name="VC"></a>

There are a lot of ways to run workflows on AWS. Here we list a few posibilities each of which may work for different research aims. As you walk through the various tutorials below, think about how you could possibly run that workflow more efficiently using a one of the other methods listed here.

- The most simple is probably to spin up an EC2 instance, and run your command interactively, or using `screen` or, as a [startup script](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html) attached as metadata. See the [GWAS tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud) below for more info on how to run a pipeline using EC2. 
- You could also run your pipeline via a Sagemaker notebook, either by splitting out each command as a different block, or by running a workflow manager (Nextflow etc.). See [here](https://aws.amazon.com/blogs/machine-learning/scheduling-jupyter-notebooks-on-sagemaker-ephemeral-instances/) about scheduling a notebook to let it run longer. You can find some example notebooks in the tutorials below, as well as on the [AWSJumpstart](AWSJumpstart/notebooks/).
- You can interact with `AWS Batch` using a workflow manager like [Nextflow](https://www.nextflow.io/docs/latest/awscloud.html) or [Cromwell](https://docs.opendata.aws/genomics-workflows/orchestration/cromwell/cromwell-overview.html).
- You can leverage the serverless functionality of AWS using the [AWS Genomics CLI](https://aws.amazon.com/genomics-cli/), which is kind of a wrapper to Nextflow and Cromwell with Batch. There are some peculiarities to using the CLI within Cloud Lab, so please read this [documentation](docs/agc) for Cloud Lab specific instructions.
- If you want to build a lasting pipeline that you plan to run many times, you could consider using [this solution](https://docs.aws.amazon.com/solutions/latest/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch/components.html) using `Step Functions` and `AWS Batch`. The github for that solution is found [here](https://github.com/awslabs/genomics-secondary-analysis-using-aws-step-functions-and-aws-batch).
- Finally, one benefit of the cloud is access to GPUs for workflow acceleration. While a lot of focus on GPU implementation will focus on AI/ML workflows, NVIDIA has software called Parabricks that will accelerate genomic workflows for pretty low costs. See the full list of command line options [here](https://docs.nvidia.com/clara/parabricks/v3.5/text/software_overview.html) to see if your specific workflow is accelerated. Specific details on how to use the Parabricks are detailed in the next section (Variant Calling).

## **Variant Calling** <a name="VC"></a>

- This [AWS blog](https://aws.amazon.com/blogs/industries/running-gatk-workflows-on-aws-a-user-friendly-solution/) describes running the GATK pipeline on 1k genomes samples using Nextflow and AWS Batch. View it as an example of what is possible, but to actually repeat thier analysis, use [Nextflow on AWS](https://www.nextflow.io/docs/latest/awscloud.html) with the GATK pipeline from [Sequera Labs](https://github.com/seqeralabs/gatk4-germline-snps-indels).
- Another [AWS blog](https://aws.amazon.com/blogs/industries/using-structural-variant-analysis-on-aws-with-amazon-fsx-for-lustre-in-novel-therapeutic-discovery/) focuses on structural variant calling, and the team that wrote it ran [GATK-SV](https://github.com/broadinstitute/gatk-sv) using [Cromwell on AWS](https://docs.opendata.aws/genomics-workflows/orchestration/cromwell/cromwell-overview.html).
- One tutorial specific to somatic variant calling comes from the Sheffield Bioinformatics Core [here](https://sbc.shef.ac.uk/somatic-variants/index.nb.html). It runs on Galaxy, but can be adapted to run in AWS. The datasets may prove useful to you.
- As mentioned above, NVIDIA Parabricks can be used to accelerate genomic workflows and especially variant calling. To give you an idea of the potential acceleration, you can expect that on a 32 CPU machine, a 30x human genome (HG002) will take about 36 hours to run GATK HaplotypeCaller. With Parabricks, you can run the same pipeline with 8 GPUs in ~40 minutes. To use Parabricks on AWS follow our instructions in the [docs](https://github.com/kyleoconnell/cloud-lab-training/tree/main/Tutorials/AWS_tutorials/docs/parabricks).

## **Genome Wide Association Studies** <a name="GWAS"></a>

- This [NIH CFDE written tutorial](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/GWAS-in-the-cloud
) walks you through running a simple GWAS using EC2. However, you could consider using one of the other approaches we listed above for something a bit more cloud native. 
- Terra has a [GWAS workspace](https://app.terra.bio/#workspaces/amp-t2d-op/2019_ASHG_Reproducible_GWAS-V2) that walks through a few tutorials and has links to public data for testing GWAS. Since it uses notebooks it should be easy enough to adapt to Sagemaker on AWS.

## **Medical Imaging** <a name="IM"></a>
- Most medical imaging analyses are done in notebooks, so we would recommend downloading the Jupyter Notebook from [here](https://github.com/kyleoconnell/cloud-lab-training/tree/main/Tutorials/AWS_tutorials/BrainTumorSegmentation) and then importing or cloning it into Sagemaker. The tutorial walks through brain image segmentation.
- AWS has a nice intro to Machine Learning in Sagemaker notebook that predicts breast cancer from features extracted from image data, which walks you through both image analysis and some of the ML functionality of Sagemaker, the notebook is found [here](https://github.com/aws/amazon-sagemaker-examples/blob/main/introduction_to_applying_machine_learning/breast_cancer_prediction/Breast%20Cancer%20Prediction.ipynb).
- You can also view this [AWS blog](https://aws.amazon.com/blogs/machine-learning/annotate-dicom-images-and-build-an-ml-model-using-the-monai-framework-on-amazon-sagemaker/) on how to annotate dicom images and build a custom AI model with the data.
- You can learn to deidentify medical images following this AWS [tutorial](https://aws.amazon.com/blogs/machine-learning/de-identify-medical-images-with-the-help-of-amazon-comprehend-medical-and-amazon-rekognition/).
- Download NVIDIA's example [Medical Imaging Notebook](https://developer.nvidia.com/run-jupyter-notebooks). Note that there are other interesting notebooks on that site, but be warned that most of the NVIDIA notebooks require a GPU, so plan accordingly.

## **RNAseq** <a name="RNA"></a>
- You can run this [Nextflow tutorial](https://nf-co.re/rnaseq/usage) for RNAseq a variety of ways on AWS. Following the instructions outlined above, you could use EC2, AWS Batch, Sagemaker, or using functions + [Batch](https://www.nextflow.io/docs/latest/awscloud.html#:~:text=Nextflow%20requires%20to%20access%20the%20AWS%20command%20line,Docker%20image%20%28s%29%20used%20during%20the%20pipeline%20execution). 
- For a notebook version of a complete RNAseq pipeline from Fastq to Salmon quantification from [the University of Maine INBRE](https://github.com/MaineINBRE/rnaseq-myco-tutorial) use this [Notebook](rnaseq-myco-tutorial-main). 
- There is also this NIH-written tutorial to use [kids first data on Cavatica](https://training.nih-cfde.org/en/latest/Bioinformatic-Analyses/RNAseq-on-Cavatica/rna_seq_1/). Note that you will need to pre-register for both kids first data and Cavatica access.

## **Single Cell RNAseq** <a name="sc"></a>
- This [AWS blog](https://aws.amazon.com/blogs/publicsector/driving-innovation-single-cell-analysis-aws/) lays out a potential method that integrates a lot of the AWS native tools for running an scRNAseq pipeline. It is less of a tutorial, and more of a demo of what is possible.
-  This [NVIDIA blog](https://developer.nvidia.com/blog/accelerating-single-cell-genomic-analysis-using-rapids/) details how to run an accelerated scRNAseq pipeline using RAPIDS. You can find a link to the github that has lots of example notebooks [here](https://github.com/clara-parabricks/rapids-single-cell-examples). For each example use case they show some nice benchmarking data with time and cost for each machine type. You will see that most runs cost less than $1.00 with GPU machines. 

## **Long Read Sequence Analysis** <a name="Long"></a>
Oxford Nanopore has a pretty complete offering of notebook tutorials for handling long read data to do a variety of things including variant calling, RNAseq, Sars-Cov-2 analysis and much more. Access the notebooks [here](https://labs.epi2me.io/nbindex/).

## **AI/ML Pipelines** <a name="AI"></a>
AWS is moving all AI/ML workflows to Sagemaker, the Juptyer notebook platform we have used a few times already. AWS has a very general tutorial [here](https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/) on how to build out an AI pipeline on Sagememaker. You can also look at the breast cancer tutorial in the imaging section above for a more applied example. 
You can also submit a training job to Sagemaker, and have your final model uplaoded to S3 using [PyTorch](https://sagemaker.readthedocs.io/en/stable/frameworks/pytorch/using_pytorch.html#train-a-model-with-pytorch), [Tensorflow](https://docs.aws.amazon.com/sagemaker/latest/dg/tf.html) or [Apache MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/mxnet.html).


STRIDES Training
Please visit the STRIDES Training page at cloud.nih.gov/training/ to view available cloud training opportunities

STRIDES Training
Please visit the STRIDES Training page at cloud.nih.gov/training/ to view available cloud training opportunitiesSTRIDES Initiative
Please visit the NIH STRIDES website at cloud.nih.gov or contact the NIH STRIDES team at STRIDES@nih.gov for more information


