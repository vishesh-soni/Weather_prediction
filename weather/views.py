from django.shortcuts import render
import numpy as np
import pickle
import pandas as pd
import os
import datetime

# filename = r"model_files\model2.sav"
    # pickle.dump(xgbcl, open(filename,'wb'))

# loaded_model = pickle.load(open(filename, 'rb'))
# pickled_model = pickle.load(open('./model_files/model2.pkl', 'rb'))
# if os.path.exists(filepath):
#     file = open('./model_files/model2.pkl', 'rb')
#     codedata = pickle.load(file)
#     file.close()

def predict_next(filename,variable,model):
    filename = 'model_files'+'\\'+str(filename)+'.npy'
    temp = np.load(filename)
    # print(temp.shape)
    # temp = np.reshape(temp,(1000))
    arr = []
    for i in temp[0]:
        arr.append(i)
    arr.append(variable)
    out = []
    for i in range(7):
        # print(i)
        arr1 = np.array(arr)
        k = arr1[i+1:]
        k = k.reshape(-1,1000)
        pickled_model = pickle.load(open('model_files'+'\\'+str(model)+'.pkl', 'rb'))
        pred = pickled_model.predict(k)
        arr.append(pred)
        out.append(round(pred[0],2))

    return out

def first_values(filename):
    filename = 'model_files'+'\\'+str(filename)+'.npy'
    temp = np.load(filename)
    return round(temp[0][0],2)


def home(request):
    # temp = np.load(r'model_files\temperature.npy')
    
    model1 = pickle.load(open(r'model_files\model1.pkl', 'rb'))
    
    temperature = first_values('temperature')
    Apparent_temp = first_values('Apparent Temperature')
    Humidity = first_values('Humidity')
    Wind_bearing = first_values('Wind Bearing')
    Visibility = first_values('Visibility')
    Wind_speed = first_values('Wind Speed')
    Pressure = first_values('Pressure')
    # print(temperature.type)
    
    temp = predict_next('temperature',temperature,'modela')
    app_temp = predict_next('Apparent Temperature',Apparent_temp,'modelb')
    humid = predict_next('Humidity',Humidity,'modelc')
    wind_bear = predict_next('Wind Bearing',Wind_bearing,'modeld')
    visible = predict_next('Visibility',Visibility,'modele')
    wind = predict_next('Wind Speed',Wind_speed,'modelf')
    press = predict_next('Pressure',Pressure,'modelg')

    temp = np.array(temp)
    app_temp = np.array(app_temp)
    humid = np.array(humid)
    wind_bear = np.array(wind_bear)
    visible = np.array(visible)
    wind = np.array(wind)
    press = np.array(press)

    tp = ['Breezy', 'Breezy and Dry', 'Breezy and Foggy',
    'Breezy and Mostly Cloudy', 'Breezy and Overcast',
    'Breezy and Partly Cloudy', 'Clear',
    'Dangerously Windy and Partly Cloudy', 'Drizzle', 'Dry',
    'Dry and Mostly Cloudy', 'Dry and Partly Cloudy', 'Foggy',
    'Humid and Mostly Cloudy', 'Humid and Overcast',
    'Humid and Partly Cloudy', 'Light Rain', 'Mostly Cloudy',
    'Overcast', 'Partly Cloudy', 'Rain', 'Windy', 'Windy and Dry',
    'Windy and Foggy', 'Windy and Mostly Cloudy', 'Windy and Overcast',
    'Windy and Partly Cloudy']

    out = [temperature,Apparent_temp,Humidity,Wind_speed,Wind_bearing,Visibility,Pressure]
    out = np.array(out)
    out = out.reshape(1,-1)
    # print(out.shape)
    pred = tp[model1.predict(out)[0]]
    # print(pred)
    model_1_pred = []

    for i in range(7):
        test = [temp[i],app_temp[i],humid[i],wind_bear[i],visible[i],wind[i],press[i]]
        
        # test.append(temp[i])
        # app_temp.append(app_temp[i])
        # humid.append(humid[i])
        # wind_bear.append(wind_bear[i])
        # visible.append(visible[i])
        # wind.append(wind[i])
        # press.append(press[i])
        test = np.array(test)
        test = test.reshape(1,-1)
        # p = model1.predict(test)
        # print(p)
        model_1_pred.append(tp[model1.predict(test)[0]])

        print(model_1_pred)
        # lent = [0,1,2,3,4,5,6]

        current_time = datetime.datetime.now()
        time = current_time.strftime("%I:%M:%S %p")
        times =[]
        # Generate 7 timestamps, each one hour apart
        for i in range(1,8):
            timestamp = current_time + datetime.timedelta(hours=i)
            formatted_timestamp = timestamp.strftime("%I:00 %p")
            times.append(formatted_timestamp)
        
        param = {'temperature':temperature , 'Apparent_temp':Apparent_temp,
                 'Humidity':Humidity,'Wind_speed':Wind_speed,
                 'Wind_bearing':Wind_bearing,'Visibility':Visibility,
                 'Pressure':Pressure,'pred':pred,
                 'temp':temp,'app_temp':app_temp,
                 'humid':humid,'wind':wind,
                 'wind_bear':wind_bear,'visible':visible,
                 'press':press,'time':time,'times':times,'model':model_1_pred}
        
        return render(request,'output.html',param)

# def home(request):
#     model1 = pickle.load(open(r'model_files\model1.pkl', 'rb'))

#     tp = ['Breezy', 'Breezy and Dry', 'Breezy and Foggy',
#        'Breezy and Mostly Cloudy', 'Breezy and Overcast',
#        'Breezy and Partly Cloudy', 'Clear',
#        'Dangerously Windy and Partly Cloudy', 'Drizzle', 'Dry',
#        'Dry and Mostly Cloudy', 'Dry and Partly Cloudy', 'Foggy',
#        'Humid and Mostly Cloudy', 'Humid and Overcast',
#        'Humid and Partly Cloudy', 'Light Rain', 'Mostly Cloudy',
#        'Overcast', 'Partly Cloudy', 'Rain', 'Windy', 'Windy and Dry',
#        'Windy and Foggy', 'Windy and Mostly Cloudy', 'Windy and Overcast',
#        'Windy and Partly Cloudy']

#     temp_f = first_values('temperature')
#     app_temp_f = first_values('Apparent Temperature')
#     humid_f = first_values('Humidity')
#     wind_bear_f = first_values('Wind Bearing')
#     visible_f = first_values('Visibility')
#     wind_f = first_values('Wind Speed')
#     press_f = first_values('Pressure')

#     out = [temp_f,app_temp_f,humid_f,wind_bear_f,visible_f,wind_f,press_f]
#     out = np.array(out)
#     out = out.reshape(1,-1)
#     # print(out.shape)
#     pred = tp[model1.predict(out)[0]]

#     current_time = datetime.datetime.now()
#     time = current_time.strftime("%I:%M:%S %p")

#     param = {'temperature':temp_f , 'Apparent_temp':app_temp_f,
#                  'Humidity':humid_f,'Wind_speed':wind_f,
#                  'Wind_bearing':wind_bear_f,'Visibility':visible_f,
#                  'Pressure':press_f,'pred':pred,'time':time}

#     return render(request,'home.html',param)

def predict(request):
    return render(request,'predict.html')

def output(request):
    # filename = r"model_files\model2.sav"
    temp = np.load(r'model_files\temperature.npy')
    
    model1 = pickle.load(open(r'model_files\model1.pkl', 'rb'))
    # print(1)
    # pred = pickled_model.predict(temp)
    # print(pred)
    # print(request.POST.get('Temperature'))
    if(request.POST.get('Temperature')):
        temperature = float(request.POST.get('Temperature'))
        Apparent_temp = float(request.POST.get('Apparent Temperature'))
        Humidity = float(request.POST.get('Humidity'))
        Wind_speed = float(request.POST.get('Wind Speed'))
        Wind_bearing = float(request.POST.get('Wind Bearing'))
        Visibility = float(request.POST.get('Visibility'))
        # Loud_cover = float(request.POST.get('Loud Cover'))
        Pressure = float(request.POST.get('Pressure'))
        # print(temperature.type)
        
        temp = predict_next('temperature',temperature,'modela')
        app_temp = predict_next('Apparent Temperature',Apparent_temp,'modelb')
        humid = predict_next('Humidity',Humidity,'modelc')
        wind_bear = predict_next('Wind Bearing',Wind_bearing,'modeld')
        visible = predict_next('Visibility',Visibility,'modele')
        wind = predict_next('Wind Speed',Wind_speed,'modelf')
        press = predict_next('Pressure',Pressure,'modelg')

        temp = np.array(temp)
        app_temp = np.array(app_temp)
        humid = np.array(humid)
        wind_bear = np.array(wind_bear)
        visible = np.array(visible)
        wind = np.array(wind)
        press = np.array(press)

        tp = ['Breezy', 'Breezy and Dry', 'Breezy and Foggy',
       'Breezy and Mostly Cloudy', 'Breezy and Overcast',
       'Breezy and Partly Cloudy', 'Clear',
       'Dangerously Windy and Partly Cloudy', 'Drizzle', 'Dry',
       'Dry and Mostly Cloudy', 'Dry and Partly Cloudy', 'Foggy',
       'Humid and Mostly Cloudy', 'Humid and Overcast',
       'Humid and Partly Cloudy', 'Light Rain', 'Mostly Cloudy',
       'Overcast', 'Partly Cloudy', 'Rain', 'Windy', 'Windy and Dry',
       'Windy and Foggy', 'Windy and Mostly Cloudy', 'Windy and Overcast',
       'Windy and Partly Cloudy']

        out = [temperature,Apparent_temp,Humidity,Wind_speed,Wind_bearing,Visibility,Pressure]
        out = np.array(out)
        out = out.reshape(1,-1)
        # print(out.shape)
        pred = tp[model1.predict(out)[0]]
        # print(pred)
        model_1_pred = []

        for i in range(7):
            test = [temp[i],app_temp[i],humid[i],wind_bear[i],visible[i],wind[i],press[i]]
            
            # test.append(temp[i])
            # app_temp.append(app_temp[i])
            # humid.append(humid[i])
            # wind_bear.append(wind_bear[i])
            # visible.append(visible[i])
            # wind.append(wind[i])
            # press.append(press[i])
            test = np.array(test)
            test = test.reshape(1,-1)
            # p = model1.predict(test)
            # print(p)
            model_1_pred.append(tp[model1.predict(test)[0]])

        print(model_1_pred)
        # lent = [0,1,2,3,4,5,6]

        current_time = datetime.datetime.now()
        time = current_time.strftime("%I:%M:%S %p")
        times =[]
        # Generate 7 timestamps, each one hour apart
        for i in range(1,8):
            timestamp = current_time + datetime.timedelta(hours=i)
            formatted_timestamp = timestamp.strftime("%I:00 %p")
            times.append(formatted_timestamp)
        
        param = {'temperature':temperature , 'Apparent_temp':Apparent_temp,
                 'Humidity':Humidity,'Wind_speed':Wind_speed,
                 'Wind_bearing':Wind_bearing,'Visibility':Visibility,
                 'Pressure':Pressure,'pred':pred,
                 'temp':temp,'app_temp':app_temp,
                 'humid':humid,'wind':wind,
                 'wind_bear':wind_bear,'visible':visible,
                 'press':press,'time':time,'times':times,'model':model_1_pred}
        
        return render(request,'output.html',param)
    
    