




provider "azurerm" {
  features {}
  subscription_id="ur id"
}

# Resource Group
resource "azurerm_resource_group" "datatricks" {
  name     = "datatricks"
  location = "eastus2"
}

# Storage Account (Data Lake Gen2 enabled)
resource "azurerm_storage_account" "datalake" {
  name                     = "datatricksstorage"  # must be globally unique and all lowercase
  resource_group_name      = azurerm_resource_group.datatricks.name
  location                 = azurerm_resource_group.datatricks.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  is_hns_enabled           = true  # Enables Data Lake Gen2

  tags = {
    environment = "dev"
  }
}

# Storage Container
resource "azurerm_storage_container" "container" {
  name                  = "synapsecontainer"
  storage_account_name  = azurerm_storage_account.datalake.name
  container_access_type = "private"
}



resource "azurerm_synapse_workspace" "synapse" {
  name                = "datatrickssynapse"
  location            = azurerm_resource_group.datatricks.location
  resource_group_name = azurerm_resource_group.datatricks.name

  storage_data_lake_gen2_filesystem_id = "https://${azurerm_storage_account.datalake.name}.dfs.core.windows.net/${azurerm_storage_container.container.name}"

  sql_administrator_login          = "ur user name"
  sql_administrator_login_password = "ur password"

  identity {
    type = "SystemAssigned"
  }

  tags = {
    environment = "dev"
  }
}

# Synapse Firewall Rule (allow your IP)
resource "azurerm_synapse_firewall_rule" "allow_my_ip" {
  name                 = "AllowMyIP"
  synapse_workspace_id = azurerm_synapse_workspace.synapse.id
  start_ip_address     = "YOUR.PUBLIC.IP.ADDRESS"
  end_ip_address       = "YOUR.PUBLIC.IP.ADDRESS"
}