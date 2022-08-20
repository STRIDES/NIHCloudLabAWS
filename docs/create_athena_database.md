# Searching the SRA database using Amazon Athena

1) Navigate to the Amazon Athena homepage. Click **Data Sources**. Advanced users could also navigate directly to the AWS Glue page and skip to #4.

<img src="/docs/images/1_select_data_sources.png" width="550" height="400">

2) Click **Create data source**. Note that you probably won't yet have any data sources listed as we do in the following screenshot. 

<img src="/docs/images/2_click_create_dataset.png" width="550" height="400">

3) Select *S3 - AWS Glue Data Catalog*. Scroll down and click **Next**.

<img src="/docs/images/3_select_glue.png" width="550" height="125">

4) Select *AWS Glue Catalog in this account* and *Create a crawler in AWS Glue*. Click **Create in AWS Glue**.

<img src="/docs/images/4_glue_catalog.png" width="550" height="400">

5) Name your crawler and then click **Next**. Make sure you do not include `-` or any special characters other than `_` in the name, otherwise you can have issues further down.

<img src="/docs/images/5_name_crawler.png" width="550" height="400">

6) Now specify the crawler source type. For *Crawler source type* select **Data Stores**. For *Repeat crawls of S3 data stores*, select **Crawl all folders**. Click **Next**.

<img src="/docs/images/6_data_stores.png" width="550" height="400">

7) Now we add the data store. for *Choose a data store* select **S3**. Skip down to *Crawl data in* and select **Specified path in my account**. For *Include path* select one of the two paths from this [NCBI guide](https://www.ncbi.nlm.nih.gov/sra/docs/sra-athena/) which is either:
- Coronaviridae dataset in the AWS Public Dataset Program: s3://sra-pub-sars-cov2-metadata-us-east-1/v2/
- Entire SRA metadata: s3://sra-pub-metadata-us-east-1

Click **Next**

<img src="/docs/images/7_add_data_stores.png" width="550" height="400">

8) Click **No** unless you want to add another data store.

<img src="/docs/images/8_click_no_other.png" width="550" height="400">

9) Select **Create an IAM role**, give your role some kind of name like `sraCrawler`. This will add a role and grant it permissions to access the public S3 bucket with the SRA metadata. Feel free to go to `IAM` and search for the Role you just created.

<img src="/docs/images/9_create_role.png" width="550" height="400">

10) Now we create a schedule for our Glue Crawler. For the sake of the demo, select **Hourly**, and set the *Start Minute* to 3 minutes from the current time so that the crawler will generate the tables right away. We will edit the crawler below to run *On Demand*, but we were having trouble generating the tables with the On Demand option. Frequent table updates will ensure that the data you are searching matches the information of the SRA master database. The downside to too frequent of updates is you will get charged for the Glue crawl, ~$1 per SRA crawl, so if you plan to leave this, set a frequency you can afford.

<img src="/docs/images/10_set_frequency.png" width="550" height="400">

11) Now we assign the tables to a Database. Since this is the first time you are adding a Glue Crawler, select **Add database**.

<img src="/docs/images/11_add_database.png" width="550" height="400">

12) Name your Database. Make sure to not use special characters other than `_`. Click **Next**.

<img src="/docs/images/12_name_database.png" width="550" height="400">

13) Review your selections and click **Finish**. Now your crawler will show up on the `Crawlers` menu. 

<img src="/docs/images/13_crawlers_menu.png" width="550" height="400">

14) After your crawler runs and the tables are generated, click your crawer name, click **Edit**, then change the schedule to **Run on Demand**. 

<img src="/docs/images/14_set_on_Demand.png" width="550" height="400">

## Query the SRA metadata using Athena

You can query the SRA database directly in the Athena user interface or you can use the API to query via a Jupyter Notebook. We recommend the Jupyter notebook approach, and provide an example [here](/tutorials/notebooks/SRADownload), as well as [these examples](https://github.com/ncbi/ASHG-Workshop-2021) produced by the SRA team. If you want to use the Athena console directly, we recommend learning the SQL query structure from our notebook or the SRA team ones, then using this [AWS guide](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html) to how to search directly in Athena. Skip to #3 since we have already done #1-2 above. 




