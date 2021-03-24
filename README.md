The Tanium Cloud Appliance for IBM Cloud tile in the IBM Cloud Catalog is used to publish the Tanium Cloud Appliance as a custom image. In order to use this deployment method, you must first perform the following tasks:
1.	Download the Tanium Cloud Appliance from Tanium
2.	Create a secure IBM Cloud object storage bucket 
3.	Upload the Tanium Cloud Appliance to the IBM Cloud object storage bucket

## Create a IBM Cloud Object Storage (COS) bucket
The IBM Cloud Object Storage bucket is used to store the Tanium Cloud Appliance. It is important that the COS bucket is secured based on IBM best practices to prevent unauthorized access to the Tanium Cloud Appliance.

1.	Create an IBM Cloud Object Storage bucket
https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-getting-started-cloud-object-storage


2.	Secure the Cloud Object Storage access via Service Credentials
https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-service-credentials
 

3.	Grant Access to using the Service Credentials
https://cloud.ibm.com/docs/cloud-object-storage/iam?topic=cloud-object-storage-iam-bucket-permissions


4.	It is highly recommended you disable public access to this COS bucket.
https://cloud.ibm.com/docs/cloud-object-storage?topic=cloud-object-storage-iam-public-access#public-access-console-disable



## Upload the Tanium Cloud Appliance to your IBM COS bucket
Once you created and secured your IBM COS bucket, you are now ready to upload the Tanium Cloud Appliance to your IBM COS bucket. The IBM COS bucket acts as a secure repository for the Tanium Cloud Appliance to be published.

1.	Login to your IBM Cloud account
2.	From your main Dashboard view, in your Resource summary, select the Storage link.
3.	From the Resource List view, scroll down to locate the cloud object storage resource created in the previous task, click the COS resource.
4.	In the Buckets view,  select the COS bucket you will use to upload the Tanium Cloud Appliance.
5.	On the Objects page, expand on the Upload drop down menu and select Folders.
6.	Navigate to the folder containing the Tanium Cloud Appliance on your local file system and select it and click open to perform the upload.
7.	Once the Tanium Cloud Appliance is successfully uploaded, make note of the full file path in the COS bucket. This will be required input during the deployment process.



# Create instance from catalog

## Configure your workspace
1. Give the workspace an appropriate name
2. Select the appropriate `Resource group`
3. Apply tags if needed

## Set the deployment values

* apikey
    * The API key of your IBM Cloud account to publish the image
    * To create a new API key:
        * On the top right corner of IBM Cloud's website, click `Manage`
        * Click `Access (IAM)` in the drop down menu
        * Clik `API keys` in the left column
        * Click `Create an IBM Cloud API key`
        * Give the API key a name and description
        * Click `Create`
        * Copy the API key or download it
          * NOTE: You won’t be able to see this API key again, so you can’t retrieve it later.
* approved_country
  * Indicates whether you are deploying the Tanium Cloud Appliance in a Tanium approved country
    * Type "true" or "false" (without quotes)
* cos-location
    * The public endpoint of the COS bucket
    * To find:
        * Navigate to the bucket that has the Tanium Cloud Appliance
        * Click the `More options` button for the dat file
        * Click `Object Details`
        * Find the `Object SQL URL`
        * Copy everything from the bucket's name to the end of the dat file's name
* name
    * The name to give the published image.
* region
  * The region where the image will be published. Use one of the following
    * us-south
    * us-east
    * eu-gb
    * eu-de
    * jp-tok
    * jp-osa
    * au-syd
* resource_group_id
    * The id of the resource group you want to give to the published image
