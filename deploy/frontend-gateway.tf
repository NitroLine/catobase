locals {
  website_gateway_name = "catobase-frontend-gateway"
}

resource "yandex_api_gateway" "catobase_frontend_gateway" {
  name      = local.website_gateway_name
  folder_id = local.folder_id
  spec      = file("frontend_openapi.yaml")
}

output "catobase_frontend_gateway_domain" {
  value = "https://${yandex_api_gateway.catobase_frontend_gateway.domain}"
}