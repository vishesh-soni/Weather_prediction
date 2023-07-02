import numpy as np
import pickle
import pandas as pd

def first_values(filename):
    filename = 'model_files'+'\\'+str(filename)+'.npy'
    temp = np.load(filename)
    return round(temp[0][0],2)
# # # temp = np.reshape(temp,(1000))
# # arr = []
# # for i in temp[0]:
# #     arr.append(i)
# # arr.append(10)
# # out = []
# # for i in range(7):
# #     arr1 = np.array(arr)
# #     k = arr1[i+1:]
# #     k = k.reshape(-1,1000)
# #     pickled_model = pickle.load(open(r'model_files\modela.pkl', 'rb'))
# #     pred = pickled_model.predict(k)
# #     arr.append(pred)
# #     out.append(pred[0])
# def predict_next(filename,model):
#     filename = 'model_files'+'\\'+str(filename)+'.npy'
#     temp = np.load(filename)
#     # print(temp.shape)
#     # temp = np.reshape(temp,(1000))
#     arr = []
#     for i in temp[0]:
#         arr.append(i)
#     arr.append(10)
#     out = []
#     for i in range(7):
#         # print(i)
#         arr1 = np.array(arr)
#         k = arr1[i+1:]
#         k = k.reshape(-1,1000)
#         pickled_model = pickle.load(open('model_files'+'\\'+str(model)+'.pkl', 'rb'))
#         pred = pickled_model.predict(k)
#         arr.append(pred)
#         out.append(round(pred[0],2))

#     return out

# out = predict_next('temperature','modela')
# print(out)
# temp = predict_next('temperature',temperature,'modela')



# temperature = '9.8'
# df = pd.DataFrame(9.8)

# from datetime import datetime

# now = datetime.now()
# current_time = now.strftime("%H:%M")
# print("Current Time =", current_time)
# tct = current_time.split(':')
# print(tct)
# import datetime

# # Get the current time
# current_time = datetime.datetime.now()
# times =[]
# # Generate 7 timestamps, each one hour apart
# for i in range(1,7):
#     timestamp = current_time + datetime.timedelta(hours=i)
#     formatted_timestamp = timestamp.strftime("%I:00 %p")
#     times.append(formatted_timestamp)
# print(times)

