variable "apikey" {
    description = "The api key for your IBM cloud account"
    type = string
}

variable "cos_location" {
    description = "The URL of the image in the COS bucket"
    type = string
}

variable "resource_group_id" {
    description = "The id of the resource group you want to use. Type \"default\" to use the default group."
    type = string
}

variable "name" {
    description = "The name of your custom OS"
    type = string
}

variable "approved_country" {
    description = "Are you located in one of the following countries?"
}

variable "region" {
    description = "What region are you using? \"us-south\", \"us-east\", \"eu-gb\", \"eu-de\", \"jp-tok\", \"jp-osa\", \"au-syd\". Type your region without the quotes."
}

variable "TF_VERSION" {
  default = "0.12"
  description = "Schematics Terraform version"
}