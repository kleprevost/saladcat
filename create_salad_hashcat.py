import requests

# EDIT THESE VARIABLES
salad_org_name = "myorg"
salad_project_name = "myproject"
salad_api_key = "mykey"
container_group_name = "saladcat"
hashtopolis_api_server_url = "http://myip:myport/api/server.php"
hashtopolis_voucher = "myvoucher"

url = "https://api.salad.com/api/public/organizations/"+salad_org_name+"/projects/"+salad_project_name+"/containers"

# This payload will create a new container group on Salad.
# The default settings are 4 CPU cores, 30gb RAM (max), and a 4090. 
payload = {
    "name": container_group_name,
    "container": {
        "image": "kleprevost/hashtopolis-hashcat-salad:latest",
        "resources": {
            "cpu": 4,
            "memory": 30720,
            "gpu_classes":["ed563892-aacd-40f5-80b7-90c9be6c759b"],
            "storage_amount":53687091200
        },
        "command": []
    },
    "environment_variables": {
    	"API_SERVER_URL":hashtopolis_api_server_url,
    	"VOUCHER":hashtopolis_voucher},
    "autostart_policy": False,
    "restart_policy": "always",
    "replicas": 1
}
headers = {
    "Salad-Api-Key": salad_api_key,
    "Content-Type": "application/json"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)