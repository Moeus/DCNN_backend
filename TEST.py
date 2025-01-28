import requests
import pandas as pd
import random
import time
url = 'https://dcnn-backend.onrender.com/predict'
data=pd.read_csv('model_file/data.csv')
num=random.randint(0,7000)
data=data[['是否老年人', '是否有配偶', '是否经济独立', '用户入网时间', '是否开通互联网服务', '是否开通网络安全服务',
       '是否开通在线备份服务', '是否开通设备保护服务', '是否开通技术支持业务', '是否开通网络电视', '是否开通网络电影',
       '合同签订方式', '是否开通电子账单', '付款方式', '月度费用', '总费用']]
send_data=data.iloc[num:num+1].reset_index(drop=True)
print(f"选取data.csv中第{num+1}行数据传入服务端")
# print(send_data)
start=time.time()
response = requests.post(url, json=send_data.to_dict())
print("服务端正常响应" if response else "服务器未响应")
# print(response.json())
end=time.time()
print(f"本次请求耗时{end-start:.2f}S")