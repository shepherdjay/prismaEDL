from dataclasses import dataclass
from typing import List
import requests

PRISMA_API_URL = 'https://api.prod.datapath.prismaaccess.com/getPrismaAccessIP/v2'

@dataclass
class MobileIP:
    zone: str
    address: str
    status: str
    type: str

def get_mobile_ips(api_key):
    data = {
        'serviceType': 'gp_gateway',
        'addrType': 'all',
        'location': 'all'
    }
    headers = {
        'header-api-key': api_key
    }
    result = requests.post(url=PRISMA_API_URL, headers=headers, json=data).json()
    try:
        if result['status'] == 'success':
            mobile_ips = []
            for entry in result['result']:
                zone = entry['zone']
                for details in entry['address_details']:
                    address = details['address']
                    status = details['addressType']
                    type = details['serviceType']
                    mobile_ips.append(MobileIP(zone=zone, address=address, status=status, type=type))
            return mobile_ips
    except KeyError:
        raise RuntimeError(result)
