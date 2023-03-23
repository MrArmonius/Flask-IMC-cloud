# Ansible INFO

For the first part of the project you need to use the public ipv4 address because we don't have DNS private zone to resolve the name.
For this you need to put this command when you run a playbook:
`ansible -i 20.228.186.197, -u azureuser --private-key Terraform/uqac_azures.pem all -b -m ping`.
 
This command has the aim to ping the machines from the inventory, e.a. from the `-i` option.

Run ansible playbook command:
`ansible-playbook -i 74.235.208.67, -u azureuser --private-key uqac_azures.pem ../ansible/playbook_sample.yaml`