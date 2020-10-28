from dataclasses import dataclass
from typing import List
import requests

PRISMA_API_URL = 'https://api.gpcloudservice.com/getPrismaAccessIP/v2'

@dataclass()
class MobileIP:
    zone: str
    addresses: List[str]

def get_mobile_ips(api_key):
    data = {
        'serviceType': 'gp_gateway',
        'addrType': 'all',
        'location': 'all'
    }
    headers = {
        'header-api-key': api_key
    }
    result = requests.post(url=PRISMA_API_URL, headers=headers, json=data, verify=False).json()
    try:
        if result['status'] == 'success':
            mobile_ips = []
            for entry in result['result']:
                mobile_ips.append(MobileIP(zone=entry['zone'], addresses=entry['addresses']))
            return mobile_ips
    except KeyError:
        raise RuntimeError(result)