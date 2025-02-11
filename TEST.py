import requests
import pandas as pd
import random
import time
from concurrent.futures import ThreadPoolExecutor

#请求的地址和端口，路由为/predict
url = 'https://moving-dashing-sawfly.ngrok-free.app/predict'


def run():
    try:
        data = pd.read_csv('data.csv')
        num = random.randint(0, 7000)
        data = data[['是否老年人', '是否有配偶', '是否经济独立', '用户入网时间', '是否开通多条电话业务', '是否开通互联网服务',
       '是否开通网络安全服务', '是否开通在线备份服务', '是否开通设备保护服务', '是否开通技术支持业务', '是否开通网络电视', 
       '是否开通网络电影', '合同签订方式', '是否开通电子账单', '付款方式', '月度费用', '总费用', '是否流失']]
        send_data = data.iloc[num:num + 1].reset_index(drop=True)
        print(f"选取data.csv中第{num + 1}行数据传入服务端")
        print(send_data)
        start = time.time()
        response = requests.post(url, json=send_data.to_dict())
        print("服务端正常响应" if response else "服务器未响应")
        print(response.json())
        end = time.time()
        print(f"本次请求耗时{end - start:.2f}S")
        return end - start
    except Exception as e:
        print(f"请求过程中出现错误: {e}")
        return -1

if __name__ == "__main__":
    s = time.time()
    durations = []  # 用于存储每个线程运行后返回的不为 -1 的时长
    # 创建一个线程池，最大线程数可以根据你的需求调整
    with ThreadPoolExecutor(max_workers=100) as executor:
        # 提交 1000 个任务到线程池
        futures = [executor.submit(run) for _ in range(50)]
        # 等待所有任务完成
        for future in futures:
            result = future.result()
            if result != -1:
                durations.append(result)

    e = time.time()
    print()
    print(f"测试用时{e - s:.2f}S")
    print(f"单个线程内的平均用时为: {sum(durations)/len(durations):.2f}")