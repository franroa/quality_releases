resource "azurerm_network_interface" "my-vm-interface" {
  name                = "my-vm-interface"
  location            = var.location
  resource_group_name = var.resrouce_group_name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = var.subnet_id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip_id
  }
}

//# Create (and display) an SSH key
//resource "tls_private_key" "example_ssh" {
//  algorithm = "RSA"
//  rsa_bits = 4096
//}
//output "tls_private_key" {
//    value = tls_private_key.example_ssh.private_key_pem
//    sensitive = true
//}


resource "azurerm_linux_virtual_machine" "my-vm" {
  name                = "my-vm"
  location            = var.location
  resource_group_name = var.resrouce_group_name
  size                = "Standard_B1s"
  network_interface_ids = [azurerm_network_interface.my-vm-interface.id]

  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "16.04-LTS"
    version   = "latest"
  }

  admin_username = "azureuser"

  admin_ssh_key {
    username       = "azureuser"
    ### A better way could be to upload your laptops key into the pipeline library and set it with the install ssh step of the pipeline
    public_key     = file("~/.ssh/gitlab_course.pub")
//    public_key = tls_private_key.example_ssh.public_key_openssh
  }
}
