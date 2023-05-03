import os
from prismaEDL.utilities import get_mobile_ips, MobileIP, PRISMA_API_URL

def get_path(file):
    path = os.path.join(os.path.dirname(__file__), file)
    return path


def test_data_get_valid(requests_mock):
    """ When we call Palo's API Correctly we should get the happy_response.json and provide the expected MobileIP objects """
    # Setup
    with open(get_path('testfiles/happy_response.json'), 'r') as infile:
        json_data = infile.read()
    requests_mock.post(PRISMA_API_URL, text=json_data)
    expected = [
        MobileIP(zone='Colombia', address='101.1.2.4', status='active', type='gp_gateway'),
        MobileIP(zone='Colombia', address='101.2.3.4', status='reserved', type='gp_gateway'),
        MobileIP(zone='Argentina', address='101.1.2.5', status='active', type='gp_gateway'),
        MobileIP(zone='Brazil Central', address='101.1.2.3', status='active', type='gp_gateway')
    ]

    result = get_mobile_ips(api_key="TestingKey")
    assert expected == result
    assert requests_mock.called_once
