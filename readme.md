
To run the API, use the command:
docker build -t bond-optimizer .
docker run -p 8000:8000 bond-optimizer

Below is the Json Request: 
{
  "expected_returns": [0.03, 0.025, 0.04, 0.035, 0.028],
  "covariance_matrix": [
    [0.001, 0.0002, 0.0001, 0.0003, 0.0002],
    [0.0002, 0.0012, 0.0003, 0.0002, 0.0001],
    [0.0001, 0.0003, 0.0011, 0.0004, 0.0003],
    [0.0003, 0.0002, 0.0004, 0.0013, 0.0004],
    [0.0002, 0.0001, 0.0003, 0.0004, 0.0012]
  ],
  "durations": [2.1, 3.5, 4.0, 5.2, 2.8],
  "max_duration": 4.0
}

Push Your Image from Your Local Machine:
    az login --use-device-code
    az acr login --name <your-acr-name>
    az acr login --name fastapilearningsumitacr123.azurecr.io
    docker tag <your-local-image> <your-acr-name>.azurecr.io/<your-image-name>:v1
    docker tag bond-optimizer fastapilearningsumitacr123.azurecr.io/bond-optimizer:v1
    docker push <your-acr-name>.azurecr.io/<your-image-name>:v1
    docker push fastapilearningsumitacr123.azurecr.io/bond-optimizer:v1

Stage 2: Deploy Your App to Azure Container Apps
Now, you will create a serverless environment and deploy your FastAPI image into it.

Go to the Azure Portal: Return to https://portal.azure.com/.

Create a Container Apps Resource:

In the search bar, type Container Apps and select it.

Click the + Create button.

For Subscription and Resource group, select your Pay-as-you-go subscription and FastAPI-Learning-RG.

For Container app name, enter a globally unique name (e.g., myfastapiapp123).

Under "Container Apps Environment," click Create new.

For Environment name, enter fastapi-env.

For Region, choose the same region.

Click Create.

Back on the main screen, under "Container image," check the box Use quickstart image and then uncheck it. This reveals the image configuration options.

For Image source, select Azure Container Registry.

For Registry, select the ACR you created.

For Image, select your pushed image.

For Image tag, select v1 (or whatever tag you used).

Configure Ingress (for the API Endpoint):

Click on the Ingress tab at the top of the creation screen.

Check the box Enable for "Ingress."

For Ingress traffic, select Accepting traffic from anywhere.

For Target port, enter the port your FastAPI app is running on (typically 8000).

Review and Deploy:

Click the Review + create button.

After validation passes, click Create.

Your container app will now be deployed. This may take a few minutes.