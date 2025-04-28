# Creating and Searching a database using Amazon Athena

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

7) Now we add the data source.

<img src="./images/athena/7_add_data_source.png">

8) Select **Create an IAM role**, give your role some kind of name like `sraCrawler`. Click on `Update choosen IAM Role`. This will add a role and grant it permissions to access the public S3 bucket. Click **Next**.

<img src="./images/athena/8_create_role.png">

9) For **Target database**, Click **Add database**. 

<img src="./images/athena/9_output_scheduling.png">

10) Name your database. Click **Create database**.

<img src="./images/athena/10_create_database.png">

11) Click **Run crawler**.

<img src="./images/athena/11_run_crawler.png">

## Query the database via Athena user interface

1) Navigate to the `Amazon Athena > Query editor`. Before you run you need to set up query result location in Amazon S3. Click `Edit setting`.

<img src="./images/athena/result_location.png">

2) Click `Browse S3`.

<img src="./images/athena/browse_s3.png">

3) Choose a S3 bucket.

<img src="./images/athena/choose_s3_bucket.png">

4) After saving the setting you can run your query.

<img src="./images/athena/run_query.png">



## Query a databse via Jupyter Notebook

You can query a database via a Jupyter Notebook. We provide an example [here](https://github.com/STRIDES/NIHCloudLabAWS/blob/main/notebooks/SRADownload/SRA-Download.ipynb), as well as [these examples](https://github.com/ncbi/ASHG-Workshop-2021). 