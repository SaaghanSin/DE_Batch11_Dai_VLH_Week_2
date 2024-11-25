# Week 2 : exercise

Ex1. Research on online exatraction and offline extraction
Ex2. Research on ELT and ETL, when and why to use?
Ex3: Docker exercise!
Deploy 1 hoặc nhiều docker container có thể phục vụ chạy airflow, ETL (sử dụng python, pandas...), có khả năng kết nối với datasource, cloud. Guideline:
i) Install Docker.
ii) Install python, airflow (prefect, or dagster), selenium, requests, beautifulsoup, AWS or Azure CLI (if it is too easy for you, install pyspark) on a single container, or on different containers (it depends on how you orchestrate and use these services).
Ex4: Why docker-compose?
Ex5: How to reduce the size of Docker images, containers?
Keyword: multistaging build.

[Ex1:]
# Ex1:

1. **Online Exatraction and Offline Extraction:**
    1. **Definition:**
    - **Online Extraction:**
    
    The data is extracted directly from the source system itself. The extraction process can connect directly to the source system to access the source tables themselves or to an intermediate system that stores the data in a preconfigured manner (for example, snapshot logs or change tables). Note that the intermediate system is not necessarily physically different from the source system.
    
    With online extractions, you need to consider whether the distributed transactions are using original source objects or prepared source objects.
    
    - **Offline Extraction**

The data is not extracted directly from the source system but is staged explicitly outside the original source system. The data already has an existing structure (for example, redo logs, archive logs or transportable tablespaces) or was created by an extraction routine.

b. **Similarities**:

- **Data Sources:** Both methods can extract data from similar sources, such as databases, APIs, files, and web scraping.
- **Techniques:** Techniques like ETL and ELT, data cleaning, can be applied in both scenarios.
- **Goals:** The primary goal of both methods is to gather, process, and prepare data for analysis and use in applications or decision-making.
    
    c. **Differences**:
    

| Feature | **Online Extraction** | **Offline Extraction** |
| --- | --- | --- |
| **Data Timeliness** | Real-time, up-to-date | May have delays depending on batch frequency |
| **Performance Impact** | Can strain source systems if not handled properly | Minimizes impact on source systems |
| **Processing Model** | Continuous, real-time processing | Batch processing at scheduled times |
| **Complexity** | Complex to manage and monitor for real-time data | Easier to manage, more predictable scheduling |
| **Storage Requirements** | Typically less storage as data is processed immediately | May require more storage to hold data before processing |
| **Cost** | Can be expensive due to infrastructure needs for real-time processing | Generally more cost-effective for large data extraction |

d. **Use cases:**

- **Online Extraction:**

| **Use Case** | **Description** | **Real-Life Example** |
| --- | --- | --- |
| **Real-time Analytics** | Gathering data continuously in real-time for immediate analysis and decision-making. | **Amazon** or **eBay** track customer behaviors and adjust recommendations instantly based on user actions. **Netflix** and **Spotify** recommend content based on user activity. |
| **Financial Trading** | Collecting live data for instantaneous decision-making in trading or investment strategies. | **Stock exchanges** like **NYSE** and **NASDAQ** analyze live stock prices and make automated trades based on real-time data. |
| **IoT Applications** | Monitoring and managing connected devices in real-time, such as sensors or smart devices. | **Smart grids** manage power distribution in real-time, while **health monitoring systems** track patient vitals continuously for instant alerts. |
| **Fraud Detection** | Detecting fraudulent activities as they happen for immediate intervention. | **Visa** and **MasterCard** monitor credit card transactions in real-time and flag suspicious activities, like unusual purchases or location changes. |
- **Offline Extraction:**

| **Use Case** | **Description** | **Real-Life Example** |
| --- | --- | --- |
| **Business Intelligence** | Aggregating and analyzing historical data for reporting and decision-making. | **Walmart** collects sales data overnight to analyze product performance and customer trends, helping to make strategic decisions the next day. |
| **Data Warehousing** | Periodic extraction of large datasets for storage and offline analysis. | **Google** and **Microsoft** extract massive datasets for storage in data warehouses, where they are analyzed for trends and insights.(S3) |
| **Backup and Archiving** | Performing scheduled backups or long-term data archiving. | **Banks** like **Chase** or **HSBC** regularly extract and archive data for backup and compliance with legal retention policies. |
| **Batch Processing** | Processing data in batches at regular intervals without real-time updates. | **IBM** or **Accenture** process payroll data in batches monthly for employee salary distribution, without the need for continuous updates. |

[Ex2]
# Ex2

**2 . ETL or ELT?**

1. **Definition:**
- ETL: ETL is a data processing method where data is **extracted** from source systems, **transformed** (cleaned, structured, or formatted) to fit the requirements of the destination system, and then **loaded** into a data warehouse or database.
- **ELT:** ELT is a data processing method where data is **extracted** from source systems, **loaded** into the destination system (such as a data lake or data warehouse), and then **transformed** after being loaded into the system.


b. Similarities:

- **Data Extraction:** Both ETL and ELT begin with extracting data from source systems.
- **Data Movement:** Both involve moving data from source systems to a data storage system (like a database or data warehouse).
- **Goals:** The primary goal of both methods is to gather, process, and prepare data for analysis and use in applications or decision-making.

c. Differences:

| Feature | **ETL** | **ELT** |
| --- | --- | --- |
| Stands for  |  Extract, transform, and load  |  Extract, load, and transform  |
|  Process  |  Takes raw data, transforms it into a predetermined format, then loads it into the target data warehouse.  |  Takes raw data, loads it into the target data warehouse, then transforms it just before analytics.  |
|  Transformation and load locations  |  Transformation occurs in a secondary processing server.  |  Transformation takes place in the target data warehouse.  |
|  Data compatibility  |  Best with structured data.  |  Can handle structured, unstructured, and semi-structured data.   |
|  Speed  |  ETL is slower than ELT.  |  ELT is faster than ETL as it can use the internal resources of the data warehouse.  |
|  Costs  |  Can be time-consuming and costly to set up depending on ETL tools used.  |  More cost-efficient depending on the ELT infrastructure used.  |
|  Security  |  May require building custom applications to meet data protection requirements.  |  You can use built-in features of the target database to manage data protection. |

d. Use cases:

### **ETL Use Cases**

1. **Legacy Systems Integration**
    
    ETL is ideal for organizations using older systems where structured data needs to be cleaned and reformatted before integration into a modern data warehouse.
    
    - Example: Migrating data from relational databases (e.g., Oracle, MySQL) to a centralized data warehouse (e.g., Teradata).
2. **Highly Regulated Industries**
    
    Industries like healthcare or finance, which require strict control and transformation of data before storing it, benefit from ETL.
    
    - Example: Transforming patient data to comply with HIPAA standards before loading it into the system.
3. **Data Quality and Governance Requirements**
    
    When data must be transformed and validated before storage to ensure accuracy and reliability.
    
    - Example: Normalizing customer data (e.g., addresses, contact details) to ensure consistency across systems.
4. **Limited Target System Resources**
    
    When the target system (data warehouse) cannot handle heavy transformations or resource-intensive operations.
    
    - Example: An on-premise data warehouse with limited compute capabilities relies on a dedicated ETL server for processing.

---

### **ELT Use Cases**

1. **Big Data Environments**
    
    ELT is optimal for processing vast amounts of structured, semi-structured, or unstructured data in modern data lakes or cloud-based systems.
    
    - Example: Loading raw log data from IoT devices into a Snowflake data warehouse and transforming it for analytics.
2. **Real-Time or Near Real-Time Analytics**
    
    ELT's faster processing makes it suitable for scenarios requiring timely insights.
    
    - Example: Loading raw clickstream data into Google BigQuery and transforming it to analyze user behavior in near real-time.
3. **Cloud-Native Architectures**
    
    ELT works well with scalable cloud platforms that leverage built-in transformation tools and compute power.
    
    - Example: Using AWS Redshift or Azure Synapse to process and analyze data from multiple sources.
4. **Flexible Data Processing Needs**
    
    Organizations requiring iterative or ad-hoc transformations prefer ELT since the raw data is already stored and accessible.
    
    - Example: Loading customer interaction data into a data lake and applying different transformations for personalized marketing campaigns.
5. **Cost Optimization for Storage**
    
    ELT reduces costs by loading data directly into a scalable storage system, transforming it only as needed.
    
    - Example: Storing raw data in an Azure Data Lake and performing transformations using Spark only for specific analytical queries.

[Ex3:]

[Ex4:]
# Ex4:

# Why docker-compose?

- Simplified control: Docker Compose allows you to define and manage multi-container applications in a single YAML file. This simplifies the complex task of orchestrating and coordinating various services, making it easier to manage and replicate your application environment.
- Efficient collaboration: Docker Compose configuration files are easy to share, facilitating collaboration among developers, operations teams, and other stakeholders. This collaborative approach leads to smoother workflows, faster issue resolution, and increased overall efficiency.
- Rapid application development: Compose caches the configuration used to create a container. When you restart a service that has not changed, Compose re-uses the existing containers. Re-using containers means that you can make changes to your environment very quickly.
- Portability across environments: Compose supports variables in the Compose file. You can use these variables to customize your composition for different environments, or different users.
- Extensive community and support: Docker Compose benefits from a vibrant and active community, which means abundant resources, tutorials, and support. This community-driven ecosystem contributes to the continuous improvement of Docker Compose and helps users troubleshoot issues effectively.

[Ex5:]
# Ex5:

- Utilize Multi-Stage Builds: eliminate unwanted layers in the image
    - We use intermediate images (build stages) to compile code, install dependencies, and package files in this approach.
    - Then only necessary app files required run the app are copied over to another image with only the required libraries, i.e., lighter to run the application.
- Using minimal base image (alpine, busybox,..)
- Understanding Caching:
    - Using COPY to define dependencies and packages before run install.
    - Adding coding file that are likely to change after in the Dockerfile.
- Minimize number of layers :combine related commands into a single RUN, COPY ,.. statement to reduce the number of layers.