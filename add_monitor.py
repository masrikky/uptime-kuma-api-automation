#pip install uptime-kuma-api

from uptime_kuma_api import UptimeKumaApi, MonitorType

uptime_kuma_url = "http://localhost:3001"
username = "USERNAME"
password = "PASSWORD"

# Define the monitor details
monitor_name = "TEST"
monitor_url = "https://google.com"
monitor_type = MonitorType.HTTP
interval = 60 

api = UptimeKumaApi(uptime_kuma_url)

api.login(username, password)

monitor_data = {
    "type": monitor_type,  
    "name": monitor_name,  
    "url": monitor_url,    
    "interval": interval   
}

# Add the monitor
response = api.add_monitor(**monitor_data)

if response.get("status") == "success":
    print(f"Monitor '{monitor_name}' added successfully!")
else:
    print(f"Failed to add monitor. Response: {response}")
