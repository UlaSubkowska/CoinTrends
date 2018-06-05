import time
import requests

list_of_symbols=['BTCUSD', 'ETHUSD', 'LTCUSD']
start_dates={'BTCUSD':'2010-07-17', 'ETHUSD':'2016-03-08', 'LTCUSD':'2016-03-08'}

def date_future(date):
    now = time.gmtime()
    date_UTC = time.strptime(date, '%Y-%m-%d')
    return True if date_UTC > now else False

def data_to_old(date):
    start_date = '2016-03-08'
    start_date=time.strptime(start_date, '%Y-%m-%d')
    date_UTC = time.strptime(date, '%Y-%m-%d')
    return False if start_date<date_UTC else True

def check_date(date):
    if date_future(date):
        error_date_message = 'Sorry you can not type start date in future, please try type proper date.'
        return error_date_message
    elif data_to_old(date):
        error_date_message = 'Sorry but we do not have such a archival data, beginning data for ETHUSD and LTCUSD is ' \
                             '2016-03-08, please type date ones again.'
        return error_date_message
    return False


def get_prices(symbol: str, start_date: str, end_date: str) ->str:
    url = "https://apiv2.bitcoinaverage.com/indices/global/history/{}?period=alltime&?format=json".format(symbol)
    response_data=requests.get(url, stream= True)
    start_date = time.strptime(start_date, '%Y-%m-%d')
    end_date = time.strptime(end_date, '%Y-%m-%d')
    my_data = []
    for chunk in response_data.json():
        chunk_date=chunk['time'].replace(' 00:00:00', '')
        UTC_chunk_date=time.strptime(chunk_date, '%Y-%m-%d')
        if UTC_chunk_date==start_date:
            my_data.append({'date': chunk_date, 'price': chunk['average']})
            my_data.reverse()
            return my_data
        if UTC_chunk_date<=end_date:
            my_data.append({'date': chunk_date, 'price': chunk['average']})


def data_for_chart_labels(my_data: list)->list:
    labels=[]
    for element in my_data:
        date_label=element['date'].replace('20','',1)
        labels.append(date_label)
    return labels


def data_for_chart_prices(my_data: list)->list:
    values = []
    for element in my_data:
        values.append(float(element['price']))
    return values


def week_annotation(labels: list)->list:
    week=[]
    amount=[]
    step=7
    number_of_week=0
    inx_shift=1
    for i in range(len(labels)):
        if not i%step:
            week.append(labels[i-inx_shift])
            amount.append('{} week'.format(number_of_week))
            number_of_week+=1
    week.pop(0)
    amount.pop(0)
    return week, amount


def divide_data(values:list)->list:
    divided_data=[]
    week_data=[]
    for elem in values:
        if len(week_data)<7:
            week_data.append(elem)
        if len(week_data)==7:
            divided_data.append(week_data)
            week_data=[]
    if len(week_data)>0:
        divided_data.append(week_data)
    return divided_data


def trend_line(prices: list) -> list:
    sum_of_up = 0
    sum_of_down = 0
    result = []
    how_many_elements = len(prices)
    price_avr = sum(prices) / how_many_elements
    t_avr_parameter = sum(range(how_many_elements + 1)) / how_many_elements
    for (inx, price) in enumerate(prices):
        t_parameter = inx + 1
        sum_of_up += (t_parameter - t_avr_parameter) * (price - price_avr)
        sum_of_down += (t_parameter - t_avr_parameter) * (t_parameter - t_avr_parameter)

    a_parameter = sum_of_up / sum_of_down
    b_parameter = price_avr - a_parameter * t_avr_parameter
    for i in range(how_many_elements):
        t_parameter = i + 1
        result.append(a_parameter * t_parameter + b_parameter)

    return result

def trends_lines(divided_data:list)->list:
    results=[]
    for week in divided_data:
        result=trend_line(week)
        results.append(result)
    return results

def grow_drop(X_trends):
    grow=1
    drop=0
    the_same=2
    X_grow_drop=[]
    for weeks in X_trends:
        if weeks[0]>weeks[-1]:
            X_grow_drop.append(drop)
        elif weeks[0]<weeks[-1]:
            X_grow_drop.append(grow)
        else:
            X_grow_drop.append(the_same)
    return X_grow_drop


def BTCUSD_relations(B_grow_drop, E_grow_drop, L_grow_drop):
    trend_descript=[]
    E_message=''
    L_message=''
    B_grow_drop.pop()
    for (index, trend) in enumerate(B_grow_drop):
        if trend:
            if E_grow_drop[index+1]:
                E_message='ETHUSD started to grow,'
            if L_grow_drop[index+1]:
                L_message='LTCUSD started to grow'
            message='BTCUSD Growth\n{} {} just after BTCUSD'.format(E_message, L_message)
        else:
            if not E_grow_drop[index+1]:
                E_message='ETHUSD started to drop,'
            if not L_grow_drop[index+1]:
                L_message='LTCUSD started to drop'
            message = 'BTCUSD Drop\n{} {} just after BTCUSD'.format(E_message, L_message)
        trend_descript.append(message)
    return trend_descript
