from datetime import datetime, timedelta

'''Datetime(year, month, day, hour, minutes, seconds)'''
data = datetime(2022, 4, 27)
print(f'data: {data}')

'''Para formatar a data usar o metodo strftime, pois ao criar
ao criar um datetime, você instanciou um objeto.'''

print(f'data formatada: {data.strftime("%d/%m/%Y")}')

'''Receber data por string, com o metodo de classe strptime'''

data1 = datetime.strptime('20/04/2022', '%d/%m/%Y')
print(f'data1: {data1}')

'''Timestamp, segundos acumulados desde uma determinada data'''
print(data.timestamp())

'''Converter Timestap para data'''
data3 = data.fromtimestamp(1651028400.0)
print(f'Data3 formatada: {data3.strftime("%d/%m/%Y")}')

'''TimeDelta serve para manusear datas em relação a periodos de tempo'''
data = datetime.strptime('19/01/2000', '%d/%m/%Y')
data = data + timedelta(days=5)
print(data.strftime('%d/%m/%Y'))

'''Operações como date'''
d1 = datetime.strptime('19/01/2000', '%d/%m/%Y')
d2 = datetime.strptime('13/05/2000', '%d/%m/%Y')
dif = d2 - d1
print(f'Diferença: {dif}')