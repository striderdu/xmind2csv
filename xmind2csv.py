from xmindparser import xmind_to_dict
import uuid
import csv

# dfs function
def s(a, parent):
    for i in a:
        for key in i:
            if isinstance(i[key], str):
                data = [i[key], uuid.uuid3(uuid.NAMESPACE_DNS, i[key]), uuid.uuid3(uuid.NAMESPACE_DNS, parent), CLASSIFYING_SYSTEM, \
                    ISVALID, ISEDIT, REVISER, TECH_FIELD, '']
                writer.writerow(data)
            else:
                s(i[key], i['title'])

# xmind to dict
xmind_dict = xmind_to_dict('集成电路技术.xmind')
main_dict = xmind_dict[0]['topic']

# config
HEADERS = ['name','number','parent_number','classifying_system','isValid','isEdit','reviser','tech_field','synonym']
CLASSIFYING_SYSTEM = '自定义分类技术体系'
ISVALID = 1
ISEDIT = 0
REVISER = 'root'
TECH_FIELD = main_dict['title']

with open('集成电路技术.csv', 'w', newline='') as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(HEADERS)
    data = [main_dict['title'], uuid.uuid3(uuid.NAMESPACE_DNS, main_dict['title']), '', CLASSIFYING_SYSTEM, ISVALID, ISEDIT, REVISER, TECH_FIELD, '']
    writer.writerow(data)
    s(main_dict['topics'], main_dict['title'])

