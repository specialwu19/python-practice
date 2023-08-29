import requests as req
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

url="https://odws.hccg.gov.tw/001/Upload/25/opendataback/9059/59/5776ed30-fa3c-48f4-9876-d8fb28df0501.json" #Ubike站點資訊
r=req.get(url,headers=headers) #發請求
print(r.json()) #資料分析成json格式

rootJson=r.json()
for data in rootJson:
        print(f"bike stop=站點名稱:{data['站點名稱']}、站點位置:{data['站點位置']}") #print出需要的資料
        

url="https://data.moenv.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=JSON" #空氣品質資訊
r=req.get(url,headers=headers) #發請求
print(r.json()) #資料分析成json格式

rootJson=r.json()
for data in rootJson["records"]:
    print(f"air quality=偵測位置:{data['site']}、城市:{data['county']}、PM2.5:{data['pm25']}") #在records中，print出需要的資料