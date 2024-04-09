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
def gcd(a,b):
    if a > b:
        c = b
        while(c > 0):
            if a % c == 0 and b % c == 0:
                return print(c)
            else:
                c -= 1
    else:
        c = a
        while(c > 0):
            if b % c == 0 and a % c == 0:
                return print(c)
            else:
                c -= 1
            
    
gcd(16,24)