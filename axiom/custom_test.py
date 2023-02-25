# from jinjasql import JinjaSql
from jinja2 import Template
import sqlite3


template_string = '''
UPDATE axiom_project
SET container = {{ container }},
    order_id = {{ order }}
WHERE
    id = {{ id }}; 
'''


params = {
    'id': 9,
    'container': 'Test_anand',
    'order': 'KKAAJJUU12'
}

output = Template(template_string).render(params)
print(output)

connection = sqlite3.connect('mydatabase')
cursor = connection.execute(output)
connection.commit()
cursor.close()
print("success")