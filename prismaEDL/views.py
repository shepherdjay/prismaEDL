from flask import current_app, Blueprint, Response
from prismaEDL.utilities import get_mobile_ips
import io

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/paloalto')
@main.route('/')
def palo_edl():
    api_key = current_app.config['PRISMA_API_KEY']
    ip_data = get_mobile_ips(api_key)
    palo_format = []
    for mobile_ip in ip_data:
        for address in mobile_ip.addresses:
            palo_format.append(f'{address} #{mobile_ip.zone}')

    return Response('\r\n'.join(palo_format), mimetype='text/plaintext')