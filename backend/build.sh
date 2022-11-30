#!/bin/bash

echo "`(cat version.json) | jq '.version = .version + 1'`"  > version.json;
backendVersion=$(jq -r '.version' version.json);
echo "Build new backend version: $backendVersion";
docker build -t ${CATOBASE_API_REPOSITORY_NAME}:0.0.$backendVersion . ;
docker push ${CATOBASE_API_REPOSITORY_NAME}:0.0.$backendVersion;
yc sls container revisions deploy \
	--folder-id ${FOLDER_ID} \
	--container-id ${CATOBASE_API_CONTAINER_ID} \
	--memory 512M \
	--cores 1 \
	--execution-timeout 5s \
	--concurrency 8 \
	--environment AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID},AWS_SECRET_ACCESS_KEY=${AWS_ACCESS_KEY_ID},DOCUMENT_API_ENDPOINT=${DOCUMENT_API_ENDPOINT},APP_VERSION=$backendVersion \
	--service-account-id ${API_SA_ID} \
	--image "${CATOBASE_API_REPOSITORY_NAME}:0.0.$backendVersion";


