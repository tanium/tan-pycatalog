resource "null_resource" "run_script" {
  provisioner "local-exec" {
    command = "python3 -m venv venv; source venv/bin/activate; python3 -m pip install pip install --upgrade \"ibm-vpc>=0.2.0\"; python3 publish_image.py ${var.apikey} ${var.cos_location} ${var.resource_group_id} ${var.name} ${var.approved_country} ${var.region}"
    interpreter = []
  }
}