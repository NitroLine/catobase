locals {
  api_gateway_name = "catobase-api-gateway"
}

resource "yandex_api_gateway" "catobase_api_gateway" {
  name      = local.api_gateway_name
  folder_id = local.folder_id
  spec      = file("../backend/openapi.yaml")
}

output "catobase_api_gateway_domain" {
  value = "https://${yandex_api_gateway.catobase_api_gateway.domain}"
}