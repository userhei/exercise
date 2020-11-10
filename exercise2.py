#!/usr/bin/python3.6
#coding = utf-8

'''
创建一个名为 Restaurant 的类,其方法 __init__() 设置两个属性: restaurant_name 和 cuisine_type 。
1.创建一个名为 describe_restaurant() 的方法和一个名为 open_restaurant() 的方法,其中前者打印前述两项信息,而后者打印一条消息,指出餐馆正在营业。
2.统计就餐人数：添加一个名为 number_served 的属性,并将其默认值设置为 0 。添加一个名为 set_number_served() 的方法,它让你能够设置就餐人数。调用这个方法并向它传递一个值,然后再次打印这个值。添加一个名为increment_number_served() 的方法,它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值:你认为这家餐馆这个时候新增的就餐人数。根据这个类创建一个名为 restaurant 的实例,调用前面添加的方法。
3.冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类,让它继承 Restaurant 类。添加一个名为 flavors 的属性,用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个 IceCreamStand 实例,并调用这个方法。
'''

class Restaurant:

  def __init__(self,restaurant_name,cuisine_type,number_served = 0):
    self.__restaurant_name = restaurant_name
    self.__cuisine_type = cuisine_type
    self.__number_served = number_served

  def get_restaurant_name(self):
    return self.__restaurant_name
 
  def set_restaurant_name(self,restaurant_name):
    self.__restaurant_name = restaurant_name

  def get_cuisine_type(self):
    return self.__cuisine_type

  def set_cuisine_type(self,cuisine_type):
    self.__cuisine_type = cuisine_type
 
  def get_number_served(self):
    return self.__number_served
 
  def set_number_served(self,number_served):
    self.__number_served = number_served

  def describe_restaurant(self):
    print('Restaurant Name:{self.get_restaurant_name()}')
    print(f'Cuisine Type: {self.get_cuisine_type()}\n')

  def open_restaurant(self):
    print(f'{self.get_restaurant_name().title()} is opening.')

  def increment_number_served(self,number_served):
    self.__number_served += number_served
    return self.__number_served

  def print_number_served(self):
    print(f'Today,the number of people served in restaurant is {self.__number_served}')

class IceCreamStand(Restaurant):
 
  def __init__(self,restaurant_name,cuisine_type,flavors = ['Chocolate','Vanilla','Strawberry']):
    super().__init__(restaurant_name,cuisine_type)
    self.__flavors = flavors

  def get_flavors(self):
    return self.__flavors
  
  def set_flavors(self,flavors):
    self.__flavors = flavors   

  def print_flavors(self):
    flavors_str = ""
    for value in self.__flavors:
      flavors_str += value + ','
    flavors_str = flavors_str.strip(',')    
    print(f'The flavors of ice cream are {flavors_str}')


def main():
  restaurant = Restaurant('Wilk','French cuisine')
  
  print('*the answer of the first question:'.title())
  restaurant.describe_restaurant()
  restaurant.open_restaurant()

  print('\n*the answer of the second question:'.title())
  restaurant.set_number_served(10)
  restaurant.print_number_served()
  print('\nAt this time, six people came in the restaurant')
  restaurant.increment_number_served(6)
  restaurant.print_number_served()

  print('\n*the answer of the third question:'.title())
  ice_cream_stand = IceCreamStand('IceCream\'s Car','Ice cream')
  ice_cream_stand.print_flavors()

if __name__=='__main__':
  main()

