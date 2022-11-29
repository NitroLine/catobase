# Deploy serivce to yandex cloud

- Выставить переменную окружения `export FOLDER_ID=<id из облака>`
- Установите нужные переменные в файле `provider.tf`
- `terraform init`
- `terraform apply`
- В выводе команды будут переменный необходимо проставить их в env
 ```
export API_SA_ID=<ваш токен из catobase_api_sa_id>
export ACCESS_ID=<id токен из aws_access_key_id>
export DATABASE_ENDPOINT=<endpoint из cats-database_document_api_endpoint>
```
- Выдать права сервисному аккаунту `service_apply.sh`
- Получить приватный ключ доступа `terraform output -raw aws_private_key`
- Выставить его в переменную окружения `export ACCESS_KEY=<ваш токен>`
- `yc container registry configure-docker`