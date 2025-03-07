import xmltodict

xml_data = open("payments.xml").read()
data_dict = xmltodict.parse(xml_data)

root = data_dict['employees']
employees = root['employee']

for i in employees:
    if "python" in i["job_title"].lower():
        print(i)
