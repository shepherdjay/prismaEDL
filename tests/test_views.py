from flask import url_for
from prismaEDL.utilities import PRISMA_API_URL
import os

def get_path(file):
    path = os.path.join(os.path.dirname(__file__), file)
    return path

def test_paloalto(requests_mock, client):
    # SETUP
    with open(get_path('testfiles/happy_response.json')) as infile:
        fake_data = infile.read()
    requests_mock.post(PRISMA_API_URL, text=fake_data)

    response = client.get(url_for('main.palo_edl'))
    assert b'101.1.2.4' in response.data
    assert requests_mock.called_once