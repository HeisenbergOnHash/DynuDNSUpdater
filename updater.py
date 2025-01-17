import requests,logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

  
def get_public_ip():
  try:
    # Use an external service to get the public IP
    response = requests.get('https://api.ipify.org?format=json')
    response.raise_for_status()
    ip_info = response.json()
    logging.info(ip_info)
    return ip_info['ip']
  except requests.RequestException as e:
    logging.error(f"Error fetching public IP: {e}")
    return None

def update_dynu_dns(api_key, hostname, ip_address=None):
  """
  Update DynuDNS with the provided hostname and IP address.

  :param api_key: API key for DynuDNS
  :param hostname: The hostname you want to update
  :param ip_address: The IP address to set (optional). If not provided, the public IP is used.
  """
  url = "https://api.dynu.com/v2/dns"
  headers = {
    "accept": "application/json",
    "API-Key": api_key,
    "Content-Type": "application/json"
  }

  if not ip_address:
    ip_address = get_public_ip()
    if not ip_address:
      logging.error("Could not fetch the public IP. Aborting update.")
      return

  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Find the record for the given hostname
    dns_records = response.json().get("domains", [])
    for record in dns_records:
      if record.get("name") == hostname:
        domain_id = record.get("id")
        # Update the record
        update_url = f"{url}/{domain_id}"
        payload = {
          "name": hostname,
          "ipv4Address": ip_address
        }
        update_response = requests.post(update_url, json=payload, headers=headers)
        update_response.raise_for_status()
        logging.info(f"Successfully updated IP for {hostname} to {ip_address}")
        return

    logging.warning(f"Hostname {hostname} not found in DNS records.")
  except requests.RequestException as e:
    logging.error(f"Error updating DynuDNS: {e}")

