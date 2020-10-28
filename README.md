### prismaEDL

#### What is it?
A flask app for grabbing your PaloAlto Prisma Mobile External IPs and displaying them in various formats. Primarily so that you
can share them with external vendors who may need to whitelist.

Out of the gate it supports Palo's EDL (External Dynamic List) and we hope to support future formats as well. Since Palo's
format is also fairly human readable it is also the default.

#### How to Use

PreReqs
- Create a Prisma Access API Key following Palo's Instructions in Step 1: https://docs.paloaltonetworks.com/prisma/prisma-access/prisma-access-panorama-admin/prisma-access-overview/retrieve-ip-addresses-for-prisma-access

To run locally:
- Clone the repository and install the requirements `pip install -r requirements.txt`
- Create an environment variable PRISMA_API_KEY and populate it with your Prisma Access API Key
- Use flask to Run the app `flask run prismaEDL/app.py`

To run on a web server:

That's a complicated topic I won't address here. If you've ran flask apps in production before or any wsgi app it should
work pretty straight forward. Maybe in the future I'll be able to provide specific instructions or feel free to contribute
as well.

#### Contributing
Contributions are welcome - I ask simply that you aim to create tests for any of the code you write. Necessary development
packages are found in requirements_dev.txt
 