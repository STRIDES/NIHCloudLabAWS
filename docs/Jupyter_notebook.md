
# Guide to spinning up a Sagemake Notebook instance and importing an example notebook

## Spin up the instance

1. Go to `Services > (A) Machine Learning > (B) Amazon SageMaker`, or just search for `Sagemaker` in the top search bar.

<img src="/docs/images/1_find_sagemaker.png" width="550" height="600">

2. On the left menu, click **Notebook > Notebook Instance**, then click **Create notebook instance**.

<img src="/docs/images/2_new_notebook_instance.png" width="550" height="250">

3. Fill out the required fields. If you need help selecting an instance go [here](https://aws.amazon.com/sagemaker/pricing/) to `On-Demand Pricing`. Click '**Additional configuration**, then increase your disk size to fit your needs. You can also create a Lifecycle configuration to enable auto-shutdown of idle VMs. See our [other guide](/docs/auto-shutdown-instance.md) on how to do this. If you want to benchmark the cost of an instance, add a tag such as key=`Project`, value=`cloudlab`, and then you can filter this later in your [billing dashboard](/docs/billing_and_cost_management.md). Finally, click **Create notebook instance** at the bottom. 

<img src="/docs/images/3_configure_sagemaker_instance.png" width="550" height="1000">

### Import our training notebook

4. Your instance will say `Pending` for a few minutes. Once the instance says `InService` (i.e. running) we can click `Open JupyterLab` on the far right of the screen. 

<img src="/docs/images/4_open_jupyter.png" width="550" height="250">

5. There are a lot of options here for opening different types of notebooks, as well as a terminal window. If you want to start a new notebook, you can select a kernel, if you aren't sure what to select, we recommend `conda_python3`. 

<img src="/docs/images/5_select_kernel.png" width="550" height="500">

6. Before importing this repository and opening the example notebook, begin by looking at the AWS example notebooks by clicking the bottom icon on the far left that looks like a brain. You will see that most of these are generic data science and ML topics, but there are a few biomedically-relevant examples, with several notebooks focused on cancer data. These notebooks are a great way to learn some basic functionality of AWS like ingesting data, training and running ML/AI models, and running R notebooks. You can also explore a variety of more advanced applications. Open a few notebooks and copy them to your workspace to see how that works. 

<img src="/docs/images/6_aws_example_notebooks.png" width="550" height="400">

7. Now you can copy in a custom notebook and some example data. From the base directory, (A) click the git icon on the middle left bar, it kind of looks like the letter 'T' with a tilt. (B) Click `Clone a Repository`, and then (C) paste the address to this repo (from the green box in the top right of the GitHub main directory) into the box. Or you can just open a terminal and type the following:

```
git clone https://github.com/STRIDES/NIHCloudLabAWS.git
```

<img src="/docs/images/7_clone_repo.png" width="550" height="400">


8. If you used the user interface you will have the NIHCloudLabAWS directory available in your file browser. If you used the terminal, it will clone into the $HOME directory, so you will need to copy the repo into the Sagemaker directory before it will show up in your file browser. Now (A) navigate to NIHCloudLabAWS > tutorials > notebooks > GWAS > GWAS_coat_color.ipynb. Explore this notebook and see how data moves in and out of the SageMaker environment. You can also manually add files, whether notebooks or data using the up arrow in the top left navigation menu, or by just dragging them in. (B) You can easily switch between different kernels in the top right, whether R or Python or Spark.

<img src="/docs/images/8_open_notebook.png" width="550" height="200">


9. Here's a few tips if you are new to notebooks. The navigation menu in the top left controls the control panel that is the equivalent to your directory structure. The panel above the notebook itself controls the notebook options. Most of these are obvious, but a few you will use often are:
+ the plus sign to add a cell
+ the scissors to cut a cell
+ stop to stop a running process
+ run a cell with the play button or use shift + enter/return. You can also use CMD + Enter, but it will only run the current cell and not move to the next cell. 

10. Above that menu you will see an option called (A) `Kernel` which is useful if you need to reset the kernel, you can click Kernel > Restart Kernel and Clear All Outputs. This will give you a clean restart. You can also use Kernel > Change Kernel if you need to switch between Kernel environments. Also worth noting that when you run a cell, sometimes it doesn't produce any output, but things are running in the background. (B) If the brackets next to a cell have an * then it is still running. (C) You can also look at the bottom where the kernel is listed (e.g. Python 3 | status) and it will show either Idle or Busy depending on if anything is running or not. 

<img src="/docs/images/9_run_notebook.png" width="550" height="600">

