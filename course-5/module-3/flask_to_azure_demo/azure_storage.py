# Azure Storage Example

from azure.storage.blob import BlobServiceClient

# Replace with your actual storage account name and access key
account_name = "your_storage_account_name"
account_key = "your_storage_account_key"

# Azure Blob Storage - Azure Blob Storage is a service for storing large amounts of unstructured data, 
# such as text or binary data. It is ideal for serving images or documents directly to a browser, 
# storing files for distributed access, streaming video and audio, writing to log files, 
# and storing data for backup and restore, disaster recovery, and archiving.
# Create a BlobServiceClient using the account name and access key
blob_service_client = BlobServiceClient(
    account_url=f"https://{account_name}.blob.core.windows.net", 
    credential=account_key
    )
# this client can be used to interact with your Azure Blob Storage account, 
# allowing you to upload, download, and manage blobs (files) in your storage containers.

# To create a new container in your Azure Blob Storage account, 
# you can use the following code:
container_name = "your_container_name" # as long as it is unique within your storage account
container_client = blob_service_client.create_container(container_name)

# To upload a file to the container, you can use the following code:
with open("path/to/your/file.txt", "rb") as data:
    blob_client = blob_service_client.get_blob_client(container=container_name, blob="file.txt")
    blob_client.upload_blob(data)

# Download a blob
with open("path/to/save/file.txt", "wb") as download_file:
    download_file.write(blob_client.download_blob().readall())
# this code downloads the blob named "file.txt" from the specified container and saves it to the local file system.

# To confirm your file was actually uploaded, you can list the blobs in the container:
blobs_list = container_client.list_blobs()
for blob in blobs_list:
    print(blob.name)

# or you can visit the Azure Portal, navigate to your storage account, and check the container to see if the file is there.