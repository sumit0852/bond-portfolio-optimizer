
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

