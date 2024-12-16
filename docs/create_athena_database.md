# Searching the SRA database using Amazon Athena

1) Navigate to the Amazon Athena homepage. Click **Data sources and catalogs**.

<img src="./images/athena/1_select_data_sources.png">

2) Click **Create data source**. Note that you probably won't yet have any data sources listed as we do in the following screenshot. 

<img src="./images/athena/2_click_create_dataset.png">

3) Select *S3 - AWS Glue Data Catalog*. Scroll down and click **Next**.

<img src="./images/athena/3_select_glue.png">

4) Select *AWS Glue Catalog in this account* and *Create a crawler in AWS Glue*. Click **Create in AWS Glue**.

<img src="./images/athena/4_glue_catalog.png">

5) Name your crawler and then click **Next**. Make sure you do not include `-` or any special characters other than `_` in the name, otherwise you can have issues further down.

<img src="./images/athena/5_name_crawler.png">

6) Click **Add a data source**.

<img src="./images/athena/6_click_add_data_source.png">

7) Now we add the data source. For *Data source* select **S3**. For *Location of S3 data* and select **In a diffirent account**. For *S3 path* select one of the two paths from this [NCBI guide](https://www.ncbi.nlm.nih.gov/sra/docs/sra-athena/) which is either:
- Entire SRA metadata: s3://sra-pub-metadata-us-east-1
- Coronaviridae dataset in the AWS Public Dataset Program: s3://sra-pub-sars-cov2-metadata-us-east-1/v2/


Click **Add an S3 data source**. 

<img src="./images/athena/7_add_data_source.png">

8) Select **Create an IAM role**, give your role some kind of name like `sraCrawler`. This will add a role and grant it permissions to access the public S3 bucket with the SRA metadata. Feel free to go to `IAM` and search for the Role you just created. Click **Next**.

<img src="./images/athena/8_create_role.png">

9) For **Set output and scheduling**, leave the default options and click **Next**. 

<img src="./images/athena/9_output_scheduling.png">

10) Name your Database. Click **Create database**.

<img src="./images/athena/10_create_database.png">

11) Click **Run crawler**.

<img src="./images/athena/11_run_crawler.png">

## Query the SRA metadata using Athena

You can query the SRA database directly in the Athena user interface or you can use the API to query via a Jupyter Notebook. We recommend the Jupyter notebook approach, and provide an example [here](https://github.com/STRIDES/NIHCloudLabAWS/blob/main/notebooks/SRADownload/SRA-Download.ipynb), as well as [these examples](https://github.com/ncbi/ASHG-Workshop-2021) produced by the SRA team. In that GitHub repo, you can view notebook 2 and adapt it from BigQuery to Athena, and then notebook 3 is a great example or different kinds of Athena queries you can run. If you want to use the Athena console directly, we recommend learning the SQL query structure from our notebook or the SRA team ones, then using this [AWS guide](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) to how to search directly in Athena. Skip to #3 since we have already done #1-2 above. 