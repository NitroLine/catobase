terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
}

provider "yandex" {
  token  =  "y0_AgAAAAAILUguAATuwQAAAADRzRk2lre4CdkdSNu7y3UHAb34-VFFjkg"
  cloud_id  = local.cloud_id
  folder_id = local.folder_id
  zone      = local.zone
}


locals {
  cloud_id  = "b1g86b2eq4feof97tpst"
  folder_id = "b1g3e1noaib6fpsbd24m"
  zone      = "ru-central1-a"
}