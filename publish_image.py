# To publish the image
from ibm_vpc import VpcV1
# To authentice with the api key
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# For exception handling
from ibm_cloud_sdk_core import ApiException
# To grab variables from command line
import sys

# Get variables from command line
apikey = sys.argv[1]
cos_location = sys.argv[2]
resource_group_id = sys.argv[3]
name = sys.argv[4]
approved_country = sys.argv[5]
region = sys.argv[6]


# Check approved country
if approved_country.lower() != "true":
    print("You are not in one of the countries authorized to use Tanium.")
    quit()



# Authenticate
authenticator = IAMAuthenticator(apikey)
service = VpcV1(authenticator=authenticator)

# Confirm region is valid
valid_regions = ["us-south", "us-east", "eu-gb", "eu-de", "jp-tok", "jp-osa", "au-syd"]
region = region.lower()
if region not in valid_regions:
    print("You did not select a valid region. Please try again and enter one of the following values: ")
    print(valid_regions)
    quit()
# Set service url
url = "https://" + region + ".iaas.cloud.ibm.com/v1"
service.set_service_url(url)



try:
    # Create image file prototype object
    image_file_prototype_model = {}

    # Get the URL of the image in the cos bucket
    image_file_prototype_model['href']= cos_location

    # Create the operating system identity model
    operating_system_identity_model = {}
    # Set the OS model to use CentOS 7
    operating_system_identity_model['name'] = 'centos-7-amd64'

    # Create image prototype model
    image_prototype_model = {}

    # Add the name to the image prototype model
    image_prototype_model['name'] = name

    # Create resource group identity model
    resource_group_identity_model = {}
    # Select the resource group for the image
    if resource_group_id != "default":
        resource_group_identity_model['id'] = resource_group_id
        # Add the resoruce group (resource_group_identity_model) to the image prototype model
        image_prototype_model['resource_group'] = resource_group_identity_model



    # Add file location (file prototype model) to the image prototype model
    image_prototype_model['file'] = image_file_prototype_model

    #Add operation system (operating system identity model) to the image prototype model
    image_prototype_model['operating_system'] = operating_system_identity_model

    image_prototype = image_prototype_model
    response = service.create_image(image_prototype)
    
    # If the request was successful
    if response.status_code == 201:
        print("Successfully Published! Status code: 201")



except ApiException as e:
    print("An error occured with status code " + str(e.code) + ": " + e.message)