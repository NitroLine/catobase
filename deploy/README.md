# Deploy serivce to yandex cloud

## Настройка на основе Serverless containers + API Gateway

- Выставить переменную окружения `export FOLDER_ID=<id из облака>`
- Установите нужные переменные в файле `provider.tf`
- `terraform init`
```
terraform apply -target=yandex_ydb_database_serverless.cats_database
terraform apply -target=yandex_iam_service_account.catobase_api_sa
terraform apply -target=yandex_container_registry.default
terraform apply -target=yandex_container_repository.catobase_api_repository
```
- В выводе команды будут переменный необходимо проставить их в env
 ```
export API_SA_ID=<ваш токен из catobase_api_sa_id>
export AWS_ACCESS_KEY_ID=<id токен из aws_access_key_id>
export DOCUMENT_API_ENDPOINT=<endpoint из cats-database_document_api_endpoint>
export CATOBASE_API_REPOSITORY_NAME=<id из catobase-api_repository_name>
```
- Выдать права сервисному аккаунту `service_apply.sh`
- Получить приватный ключ доступа `terraform output -raw aws_private_key`
- Выставить его в переменную окружения `export AWS_ACCESS_KEY_ID=<ваш токен>`
- Устонвоить зависимости для python в папке `backend`: `pip install -r requirements.txt`
- Содать таблицы в базе данных `python migrate.py`
- `yc container registry configure-docker`
- `yc sls container create --name catobase-api-container --folder-id ${FOLDER_ID}`
- Из вывода команды скопировать поле `id` и проставить в переменную окружения `export CATOBASE_API_CONTAINER_ID=<ваш id>`
- ### Перейти в папку `backend` чтобы собрать и залить новую версию API в облако скриптом `./build.sh`
- В файле `backend\openapi.yaml` подменить `${API_SA_ID}` на соответсвующее значение переменной
- В файле `backend\openapi.yaml` подменить все `${CATOBASE_API_CONTAINER_ID}` на соответсвующее значение переменной
- `terraform apply -target=yandex_ydb_database_serverless.catobase_api_gateway`
- Адрес из вывода команды поставить переменную `CATOBASE_API_GATEWAY` в файле `frontend/src/params.js`
- `terraform apply -target=yandex_storage_bucket.catobase_frontend_bucket`
- Из вывода команды имя бакета установить переменную окружения `export CATOBASE_WEBSITE_BUCKET=<имя из переменной catobase_frontend_website_bucket>`
- В файле `frontend_openapi.yaml` подменить `${API_SA_ID}` на соответсвующее значение переменной
- В файле `frontend_openapi.yaml` подменить `${CATOBASE_WEBSITE_BUCKET}` на соответсвующее значение переменной
- `terraform apply -target=yandex_api_gateway.catobase_frontend_gateway`
- В выводе файла конечная ссылка для фронтэнда `catobase_frontend_gateway_domain`
- Сконфигурируйте `s3cmd --configure` 
- ### Перейти в папку `frontend` чтобы собрать и залить новую версию фронтэнда в облако скриптом `./build.sh`
