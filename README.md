# Bootcamp data engineer IGTI


**1st** **Data Lake with AWS S3:** Creation of a bucket in **S3** for raw data and data treated from a **Data Lake;**

**2nd Big Data Processing with AWS EMR:** Data processing with **Spark in EMR** using **EC2** instances to create automatic jobs (Here we configure the machines that will be used);

**3rd** **Big Data Processing with AWS Glue:** Creation of Jobs for automatic data processing in **Glue** (We do not see the machines configuration here);

**4th Data Availability with AWS Athena:** Data Availability in **Athena** for querying with SQL queries.

**Comments:**

- Connecting to a BI tool is not in the course, but it is possible with QuickSight.
- It is possible to create several databases in the AWS cloud as AWS RDS.

## Initiating the project

### Installations 

*AWSCLI* [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

*boto3* [https://pypi.org/project/boto3/](https://pypi.org/project/boto3/)

### In the terminal 

- Type "aws configure" the terminal:

***AWS Access Key ID [None]: IAM  key***
***AWS Secret Access Key [None]: secret IAM key (You can see it when you create another key)***
***Default region name [None]: us-east-2***
***Default output format [None]: json***

### Create Data Lake with AWS S3

- Create a bucket at AWS S3;
- Create a python file called interact_s3 at VSCode (See the file interact_s3.py);
- Execute the file with the following command in the terminal: "interact_s3.py" or "python interact_s3.py";
- This command will download or upload the file from the bucket S3 AWS;

### Processing Big Data with AWS EMR

#### Configure the cluster EMR

- At Amazon EMR, create a cluster;
- StepGo to advanced Software Configuration and 
- Step 1: (Software and Steps) Select the last release and select: Hadoop, JupyterHub, Hive, JupyterEnterpriseGateway, Hue and Pig;
- Select Concurrency >> Run multiple steps at the same... 10 maximum steps;
- After the last step completes select "Clusters enters waiting stage";
- Step 2: (Hardware) At cluster Composition select "Uniform instance groups"
- Networking is the default;
- Clusters nodes and Instances:

![image](https://user-images.githubusercontent.com/59781746/158043283-ea07c9b6-3083-4a9f-ace3-568355116f91.png)

- EBS Root Volume: Root device... 10Gb
- Step 3: General Cluster Settings;
- Cluster name, Tags (optional) and unselect "Termination protection";
- Step 4: Default
- After the status of "Cluster ready" you can use it.

#### Configure the notebooks to do tests with spark

- Create a notebook at "notebooks";
- Give the name and description;
- Choose the cluster that you already created;
- After "ready" select and choose jupyterLab;
- Open it and select the kernel "PySpark";
- Import pyspark.

#### Execution of jobs Spark by spark-submit

- Create a file .py to execute a script to emr (See the file job_spark.py);
- Create a folder at the bucket with the name "Pyspark" and do the upload of the ENEM file;

![image](https://user-images.githubusercontent.com/59781746/158043733-ad3b71b8-7617-4e1e-b581-bfbccfaea3d2.png)

- Select the cluster and "steps" to transform the data at parquet;
- Add a step to execute a spark job.

![image](https://user-images.githubusercontent.com/59781746/158043824-33e2a227-7d6c-4794-853f-490b6f5b4b24.png)

- See the data .parquet partitions at this path:

![image](https://user-images.githubusercontent.com/59781746/158043861-84b08523-b9e1-41b1-a996-abdd08f0d320.png)

- At the notebook type Spark.stop() to end the notebook session and terminate the cluster.

### Processing Big Data with AWS Glue

- At AWS Glue environment select ETL - Jobs;
- At Job properties:

![image](https://user-images.githubusercontent.com/59781746/158083490-a6319566-0f12-410b-b6f3-8b84ff947b7b.png)
![image](https://user-images.githubusercontent.com/59781746/158083555-d47c95e2-eea4-4356-a84e-672f325812c0.png)

- At "S3 path where the script is stored" select the file's path;
- At connections you don't need do something;
- Click at next to edit and save your python script;
- Include the script at file "glue_spark_job.py";
- Save and at "action" click at "run job";
- Don't forget to give full access at the IAM to S3 at its policies(Roles);

![image](https://user-images.githubusercontent.com/59781746/158084262-0c41a7e4-f12f-4599-9d94-30a3e7853543.png)

### Data Availability with AWS Athena

** Configuration**

- At AWS Glue (Datalake engine) select "crawlers" and add one with a name at Crawler info;
- At crawler source type;

![image](https://user-images.githubusercontent.com/59781746/158084590-838d5511-0731-4266-a534-0789f6106366.png)

- Data Store is S3 and at "include path" give the path of the crawler where is the data .parquet (folder);
- At IAM Role Create one with a name;
- At schedule "run on demand" or schedule it;
- At Output add a database with name and review it to finish.

** Query **

- At AWS Athena and select "get started";

![image](https://user-images.githubusercontent.com/59781746/158085157-1513aed0-6296-4c7b-a36e-5ede010e469c.png)

- Select the table and enjoy your queries using SQL and connect it at one BI from the datalake.

![image](https://user-images.githubusercontent.com/59781746/158085829-ed3fb483-8c10-4b3e-ae05-3e25a95a6a3d.png)



# Infrastructure As Code (IaC)
