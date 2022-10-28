import requests  
import json
#from bs4 import BeautifulSoup 
from pyecharts import options as opts
from pyecharts.charts import Pie
import os

docx_name = '风险区'

def Adddata(a,list_a,b,list_b):
    if int(a) !=0:
        list_a.append(a)
        list_b.append(b)
    
    else:
        print('\t' + b + '无' + docx_name)
    
os.chdir("E:\文件\学习\编程学习\python学习项目\Pyecharts\饼图Pie\各省属地现有风险区数目")
headers = {
    'cookie': 'BIDUPSID=C24DAF0DDCFC4EADA6190FE4BCCB314F; PSTM=1624862488; __yjs_duid=1_40e1e41adb9a9915aec59edc63778a361624953837159; MAWEBCUID=web_VIFQtgNYpsbzASxVetLZJwaITdYQcunGcAQDATwwpjVzLstctm; BAIDUID=64029D337199BFBD494EAC0EA95E71D3:FG=1; BDUSS=NORjlweDhkd2ZWekRZSUt1N2d3cTN5Nzg3VzlGYno4QmkyVUN-Zm5KNHpwbGRqRVFBQUFBJCQAAAAAAAAAAAEAAABJ9AKhw9TWrtTOuvW69QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADMZMGMzGTBjYj; BDUSS_BFESS=NORjlweDhkd2ZWekRZSUt1N2d3cTN5Nzg3VzlGYno4QmkyVUN-Zm5KNHpwbGRqRVFBQUFBJCQAAAAAAAAAAAEAAABJ9AKhw9TWrtTOuvW69QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADMZMGMzGTBjYj; newlogin=1; MCITY=-233%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=64029D337199BFBD494EAC0EA95E71D3:FG=1; RT="z=1&dm=baidu.com&si=6elo11jnjb6&ss=l9qhhonc&sl=3&tt=1yu&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=5db&ul=ee8&hd=eew"; ZD_ENTRY=bing; ab_sr=1.0.1_MjJjYzYzZmU1NDBhOTI1MGJhMmZlZDQwZDNhMWQxZjAyMmYwZjUzNzc2MzMzMTM4ZmQ2NDg5MTg4NTQ0MTY0M2M4NWY5YTZmMjk3ZDg1NjMxYmE4MjAwNWJhYjA3NDM5NTY1OGNiZjNkM2NhNGU0YjYwNzYxNzllNDllZjRmZDdlNTgxMmM0MzBlNTQ0ZTM5Zjk3YWNkNmUxNmZiOWVmODJkN2VjMGU1NzZlMGZhNjZkYjQ1MTEwODIwYTAyZmFj',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
    }

url = 'https://voice.baidu.com/api/newpneumonia?from=page&callback=jsonp_1666841702946_12436'
response = requests.get(url, headers=headers)  
r = response.text
#q = re.findall(r'[(](.*?)[)]', r)
s = json.loads(r[26:-2])['data']['caseList']



for provinces in s:
    city_name = []
    confirmedRelative_list = []
    ImgName = ''
    TitleName = ''
    
    area = provinces['area']    #省名
    TitleName = area+'各属地现有风险区数目'

    for citys in provinces['subList']:
        city = citys['city']    #城市名
        confirmedRelative = citys['confirmedRelative']    #新增确诊
        curConfirm = citys['curConfirm']    #现有确诊
        confirmed = citys['confirmed']    #累计确诊
        asymptomaticRelative = citys['asymptomaticRelative']    #新增无症状感染者
        totalNum = citys['dangerousAreas']['totalNum']    #风险区
        
        Adddata(totalNum,confirmedRelative_list,city,city_name)
        
        #city_name.append(city)
        #confirmedRelative_list.append(curConfirm)
        #confirmedRelative_list.append(totalNum)
    
    #print(confirmedRelative_list)    
    ImgName =str(area) +'.html'   
    try:
        c = (
        Pie()
            .add(
                "",
                [list(z) for z in zip(city_name, confirmedRelative_list)],
                center=["25%", "40%"],
                radius=[60, 90],
            )
            .set_global_opts(
                legend_opts=opts.LegendOpts(
                    is_show = False
                    ),
                title_opts=opts.TitleOpts(title=TitleName)
            )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .render(ImgName)
        )
    except:
        print(area+'无' + docx_name)






