locals {
  database_name = "cats-database"
}

resource "yandex_ydb_database_serverless" "cats-database" {
  name      = local.database_name
  folder_id = local.folder_id
}

output "cats-database_document_api_endpoint" {
  value = yandex_ydb_database_serverless.cats-database.document_api_endpoint
}

output "cats-database_path" {
  value = yandex_ydb_database_serverless.cats-database.database_path
}