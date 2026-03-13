from oops_proj import chatbook

#user1=chatbook()

lst=[1,2,3]

a1=len(lst)
#print(a1)

user1=chatbook()
#user1.msg_friend()
#print(user1._chatbook__name)

#print(user1.name)

#print(user1.get_name())
#user1.set_name('sam kumar')
#print(user1.get_name())

#static method
print(user1.id)
#static method


chatbook.set_id(100)
user2=chatbook()
print(user2.id)

