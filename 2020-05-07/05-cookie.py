# _*_coding:utf-8 _*_

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
           "cookie":"BAIDUID=F766C91D832D36BB465CA30F8D6AD38D:FG=1; BIDUPSID=F766C91D832D36BB465CA30F8D6AD38D; PSTM=1579887551; BD_UPN=123353; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BD_HOME=1; H_PS_PSSID=1433_31125_21105_31428_31342_31463_31322_30824_26350_31163_31476; delPer=0; BD_CK_SAM=1; PSINO=6; H_PS_645EC=808aTolu5yeFo0cpLYwNhufcV1x43QwfXiJCfGnEAcOX3rSyvZsBPXDVfFg; BDSVRTM=132; COOKIE_SESSION=604425_2_9_9_6_10_0_0_9_4_1_0_2243_0_0_21_1588210984_1588213231_1588817635%7C9%233794282_3_1588213210%7C2"
          }

url = 'https://www.baidu.com/s?wd=python'

response = requests.get(url, headers=headers)
with open('python.html','w') as F:
    F.write(response.content.decode())

print(response.status_code)
