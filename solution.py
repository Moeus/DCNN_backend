import pandas as pd
import joblib
import keras
import os
#环境变量
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# 读取pkl模型
ordina_lencoder = joblib.load('model_file/ordina_lencoder.pkl')
min_max_scaler = joblib.load('model_file/min_max_scaler.pkl')
model = keras.models.load_model('model_file/ANN_model.keras')

col=['是否老年人', '是否有配偶', '是否经济独立', '用户入网时间', '是否开通互联网服务', '是否开通网络安全服务',
       '是否开通在线备份服务', '是否开通设备保护服务', '是否开通技术支持业务', '是否开通网络电视', '是否开通网络电影',
       '合同签订方式', '是否开通电子账单', '付款方式', '月度费用', '总费用']
num_cols = ["用户入网时间", "月度费用", "总费用"]

def solve(data):
    X=pd.DataFrame(data)
    try:
        X=X[col]
    except:
        return "输入数据格式错误"
    else:
        #编码前预处理
        X[X.columns.difference(num_cols)] = X[X.columns.difference(num_cols)].astype(object)
        X[["是否老年人", "用户入网时间"]] = X[["是否老年人", "用户入网时间"]].astype('int64')
        X["是否流失"]="Yes"
        print("正在处理post请求")
        #数据编码
        X[ordina_lencoder.feature_names_in_]=ordina_lencoder.transform(X[ordina_lencoder.feature_names_in_])
        X[num_cols] = min_max_scaler.transform(X[num_cols])

        # 预测
        y_pred = model.predict(X.drop("是否流失",axis=1))
        return f"模型认为该客户可能流失,流失概率为{y_pred[0][0]*100:.2f}%" if y_pred[0][0]>=0.4 else "模型认为该客户不会流失"