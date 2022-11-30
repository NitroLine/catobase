locals {
  website_bucket_name_prefix = "catobase-website"
}

resource "yandex_storage_bucket" "catobase_frontend_bucket" {
  bucket     = "${local.website_bucket_name_prefix}-${local.folder_id}"
  access_key = yandex_iam_service_account_static_access_key.catobase_api_sa_static_key.access_key
  secret_key = yandex_iam_service_account_static_access_key.catobase_api_sa_static_key.secret_key
}

output "catobase_frontend_website_bucket" {
  value = yandex_storage_bucket.catobase_frontend_bucket.bucket
}