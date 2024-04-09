class Friends():
    def __init__(self):
        self.friend = list()
    
    def insert(self, name):
        self.friend.insert(0, name)
    
    def append(self, name):
        self.friend.append(name)
        
    def getAllFriends(self):
        return self.friend
    

list_of_friends = Friends()
list_of_friends.insert("Tae")
list_of_friends.append("won")
list_of_friends.insert("Yoon")

print(list_of_friends.getAllFriends())
