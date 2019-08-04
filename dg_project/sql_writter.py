import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dg_project.settings')
import django
django.setup()

from homepage.models import Resort
import json

with open("dg_project\homepage\static\sql_info.json","r",encoding='utf-8') as info:
    jsf = json.loads(info.read())
    print(type(jsf))
    
for key in jsf.keys():
    rs = Resort(
        resort = jsf[key]['name'],
        brief = jsf[key]['slogan'],
        url = jsf[key]['url'],
        parameters = jsf[key]['parameters'],
        benefit= jsf[key]['benefit'],
        descption = jsf[key]['description'],
        logo_dir = f"{key}.jpg"
        )
    rs.save()