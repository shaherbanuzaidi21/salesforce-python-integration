from simple_salesforce import Salesforce

sf = Salesforce(
    username='your_email',
    password='your_password',
    security_token='your_token',
    domain='test'   # important for developer org
)

accounts = sf.query("SELECT Id, Name FROM Account LIMIT 5")

for record in accounts['records']:
    print(f"ID: {record['Id']}, Name: {record['Name']}")