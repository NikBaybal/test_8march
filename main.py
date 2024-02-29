import numpy as np
from random import choices,seed

# функция расчета расстояния от точки А до B
# входные векторы образованы путем соединения начало координат и точек А и В
def distance(vector_A:np.array,vector_B:np.array):
  vector=vector_A-vector_B
  return (np.dot(vector,vector)**0.5).round(2)


#функция создания случайных входных данных (координаты точек А заказов, координаты местонахождения курьеров)
def create_data(n):
  seed(20)  # фиксируем случайные числа
  orders=[]
  couriers=[]
  for i in range(n):
    orders.append([f'Заказ №{i+1}']+choices(range(-10, 10), k=2))
    couriers.append([f'Курьер №{i+1}']+choices(range(-10, 10), k=2))
  print('Входные данные в формате [Заказ №, координата по x, координата по y]:')
  print(orders)
  print(couriers)
  print()
  return orders,couriers


#функция распределения заказов по курьерам наиболее близких к заказу
def distribution(orders,couriers):
  result = {}
  for order in orders:
    vector_order = np.array([order[1],order[2]])
    result[order[0]] = ''
    minimum=100
    for i in range(len(couriers)):
      vector_courier = np.array([couriers[i][1], couriers[i][2]])
      if distance(vector_courier,vector_order)<minimum and couriers[i][0] not in result.values():
        minimum = distance(vector_courier,vector_order)
        result[order[0]] = couriers[i][0]
  return result


#создаем входные данные и распределяем заказы
orders,couriers=create_data(5)
res=distribution(orders,couriers)
print('Распределение заказов по курьерам:')
for i in res:
  print(i,'->',res[i])