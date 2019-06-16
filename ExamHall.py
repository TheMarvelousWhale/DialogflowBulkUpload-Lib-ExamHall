# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 10:53:46 2019

@author: hoang
"""


import re,json,shutil
import pandas as pd
from copy import deepcopy
from pprint import pprint

################################################################################
source = './Lyon_template/'
dest = './Lyon_template - Copy/'

shutil.copytree(source,dest) 
################################################################################
with open(r'linkBtnResponse.json') as f:
    template_question = json.loads(f.read())
    
with open(r'usersays_en.json') as f:
    template = json.loads(f.read())
    payload_template = deepcopy(template)[0]


#
#str0 ='The Wang Gungwu Library (Overseas Chinese Collections) is located at Level B5 of the South Spine. Here is the address: 50 Nanyang Ave, Block S3.2-B5, Singapore 639798. A detailed map with directions can be found here: http://maps.ntu.edu.sg/m?q=wang%20gungwu%20library&fs=m'
#str1 = 'The Art, Design & Media Library is located at Level 1 of the School of Art, Design and Media (ADM) building. Here is the address: ART-01-03, School of Art, Design and Media (ADM), 81 Nanyang Drive, Singapore 637458. A detailed map with directions can be found here: http://maps.ntu.edu.sg/m?q=art,%20design%20%26%20media%20library%20(adm)&fs=m'
#str2 = 'Exam Hall 10 is located at Hall of Residence 10 (Hall 10), 22 Nanyang Avenue, Singapore 639810. Nearest Bus Stop - Red Line Bus Stop, Hall 11. Blue Line Bus Stop, Opp Hall 10 & 11. Public Bus - 199, Hall 11. A detailed map of the examination venue can be found at http://maps.ntu.edu.sg/m?q=Examination%20Hall%2010&fs=m'
#
#
#libp = r'(.*). Here is the address: (.*). A detailed map with directions can be found here: (.*)'
examp = r'(.*). A detailed map of the examination venue can be found at (.*)'
#result = re.findall(examp,str2)



main = pd.read_excel("ExamHallLoc.xlsx")
qnVarTemp = pd.read_excel("QnVarTemplate.xlsx")

col0 = main.iloc[:,0]
col1 = main.iloc[:,1]

examp = r'(.*). A detailed map of the examination venue can be found at (.*)'

for i in range(len(main.index)):
    a = re.findall(r'[Ww]here is Exam Hall (.*)?',col0[i])[0]
    num = re.sub('\?','',a)
    intentName = f'Knowledge.Location.Where_is_Exam_Hall_{num}'
    e = f'Exam Hall {num}'
    res = re.findall(examp,col1[i])[0]
    q_copy=deepcopy(template_question)
    q_copy['name'] = intentName
    #print(renamedIntentName)
    print(intentName)
    
    q_copy['responses'][0]['messages'][0]['payload']['message'] = res[0]
    q_copy['responses'][0]['messages'][0]['payload']['metadata']['payload'][0]["url"] = res[1]
    q_copy['responses'][0]['messages'][0]['payload']['metadata']['payload'][0]["name"] = f'Click here to go to {e}'
    
    #pprint(q_copy)
    user_Says_load = []
    for qnVar in qnVarTemp.iloc[:,0]:
        temp = deepcopy(payload_template) #create a payload
        temp['data'][0]['text'] = re.sub('abcxyz',e,qnVar) #put in data
        #print(temp['data'][0]['text'])
        user_Says_load.append(temp) #attach to main load        
    u_copy = user_Says_load
    
    with open(f'{dest}intents/{e}.json','w') as f:
        f.write(json.dumps(q_copy))
    with open(f'{dest}intents/{e}_usersays_en.json','w') as f:
        f.write(json.dumps(u_copy))
        
        
        
shutil.make_archive("New Intents", 'zip', dest)
shutil.rmtree(dest)