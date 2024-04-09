# class Friends():
#     def __init__(self):
#         self.friend = list()
    
#     def insert(self, name):
#         self.friend.insert(0, name)
    
#     def append(self, name):
#         self.friend.append(name)
        
#     def getAllFriends(self):
#         return self.friend

# list_of_friends = Friends()
# list_of_friends.insert("Tae")
# list_of_friends.append("won")
# list_of_friends.insert("Yoon")

# print(list_of_friends.getAllFriends())

# class Numbers():
#     def __init__(self):
#         self.numbers = [1,2,3]
    
#     def changeSecond(self, num):
#         self.numbers[1] = num
        
#     def insertNumbers(self, *num):
#         self.numbers += num
    
#     def removeFrist(self):
#         del self.numbers[0]
    
#     def sort1(self):
#         self.numbers.sort()
        
#     def sort2(self):
#         self.numbers.sort(reverse=True)
        
#     def insertIndex(self, index, num):
#         if index > len(self.numbers):  # 리스트의 길이보다 큰 인덱스가 주어진 경우
#             self.numbers.append(num)  # 리스트에 요소를 추가합니다.
#         else:
#             self.numbers.insert(index, num)  # 주어진 인덱스에 요소를 삽입합니다.
        
#     def getAllNumbers(self):
#         return self.numbers

# num_list = Numbers()
# print(num_list.getAllNumbers())

# num_list.changeSecond(17)
# print(num_list.getAllNumbers())

# num_list.removeFrist()
# print(num_list.getAllNumbers())

# num_list.sort1()
# print(num_list.getAllNumbers())

# num_list.sort2()
# print(num_list.getAllNumbers())

# num_list.insertIndex(3, 25)
# print(num_list.getAllNumbers())

# from random import randint 

# class Game():
#     def __init__(self):
#         self.money = 50
    
#     def play(self, guese):
#         if guese == randint(1,2):
#             self.money += 9
#         else:
#             self.money -= 10
            
#         self.showMeTheMoney()
    
#     def showMeTheMoney(self):
#         print(self.money)

# player = Game()
# player.play(1)
# player.play(2)
# player.play(2)
# player.play(1)

# 작은수에서 큰수로부터 밑으로 1씩 감소하면서 나눠떨어지면 된다
# def gcd(a,b):
#     if a > b:
#         c = b
#         while(c > 0):
#             if a % c == 0 and b % c == 0:
#                 return print(c)
#             else:
#                 c -= 1
#     else:
#         c = a
#         while(c > 0):
#             if b % c == 0 and a % c == 0:
#                 return print(c)
#             else:
#                 c -= 1
# gcd(16,24)

# word = input("Your word: ")
# for i in word:
#     if i == 'a':
#         print(i, end="\n")
#     else:
#         print(i, end="")

# class MakeList():
#     def __init__(self):
#         self.numList = list()
        
#     def normalList(self):
#         self.numList.clear()
#         for i in range(0,50):
#             self.numList.append(i)
    
#     def squareList(self):
#         self.numList.clear()
#         for i in range(0,50):
#             self.numList.append(i * i)

    
#     def getList(self):
#         print(self.numList)
        
# numList = MakeList()
# numList.normalList()
# numList.getList()
# numList.squareList()
# numList.getList()

# class Months():
    
#     def __init__(self):
#         self.days = {'January':31, 'February':28, 'March':31, 'April':30,
#         'May':31, 'June':30, 'July':31, 'August':31,
#         'September':30, 'October':31, 'November':30,
#         'December':31}
    
#     def getMonth(self, month):
#         print(self.days[month])
        
#     def printAllMonths(self):
#         for month in sorted(self.days.keys()):
#             print(month)
            
#     def printMonths31Days(self):
#         for month, days in sorted(self.days.items()):  # 사전의 순서는 월의 순서를 따르므로 추가적인 정렬 없이 출력
#             if days == 31:
#                 print(month)
                
#     def getDaysByAbbreviation(self, abbreviation):
#         for month, days in self.days.items():
#             if month[:3].lower() == abbreviation.lower():
#                 print(f"{month}: {days} days")
#                 return
#         print("Invalid abbreviation")
    
            
        
    
    
    
# month = Months()
# month.getMonth('January')
# month.printMonths31Days()

# class Phone():
#     def __init__(self):
#         self.d = [{'name':'Todd', 'phone':'555-1414','email':'todd@mail.net'},
#                   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
#                   {'name':'Princess','phone':'555-3141', 'email':''},
#                   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
    
#     def get8PhoneNumber(self):
#         print("전화번호가 8로 끝나는 사용자 이름을 출력합니다:")
#         for entry in self.d:
#             if entry['phone'][-1] == '8':
#                 print(entry['name'])
                
#     def getEmaillessUsers(self):
#         print("\n이메일이 없는 사용자 이름을 출력합니다:")
#         for entry in self.d:
#             if not entry['email']:  # 이메일이 없는 경우
#                 print(entry['name'])
                
#     def getContactInfoByName(self, name):
#         print(f"\n사용자 이름이 '{name}'인 전화번호와 이메일을 출력합니다:")
#         for entry in self.d:
#             if entry['name'] == name:
#                 print(f"전화번호: {entry['phone']}")
#                 print(f"이메일: {entry['email']}")
#                 return
#         print("해당하는 이름이 없습니다.")

# # Phone 클래스의 인스턴스 생성
# phone_instance = Phone()

# # 전화번호가 8로 끝나는 사용자 이름 출력
# phone_instance.get8PhoneNumber()

# # 이메일이 없는 사용자 이름 출력
# phone_instance.getEmaillessUsers()

# # 사용자 이름으로 전화번호와 이메일 출력
# phone_instance.getContactInfoByName('Todd')
# phone_instance.getContactInfoByName('Princess')
# phone_instance.getContactInfoByName('Mickey')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def getName(self):
        print(self.name)
        
    def getAge(self):
        print(self.age)
    
class Employee(Person):
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.employeeID = id
        
    def getEmployeeID(self):
        print(self.employeeID)
    
    def getInfo(self):
        self.getName()
        self.getAge()
        self.getEmployeeID()
        
taewon = Employee("IoT", 25, 20191532)
taewon.getInfo()
    