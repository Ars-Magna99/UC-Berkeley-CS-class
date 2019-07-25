# Python Crash Course 
# After class practice 


# 3 - 4 name of guests
guests = ["Keanu Reeves","Michael Jackson","Haonan Feng","Song Cao","Yunpeng Fu","Rongfa Lu","Ziyi Wang"]
print (guests)

#someone I inveted was unable to attend 
no_appear = ["Michael Jackson"]
print (no_appear[0] +" "+ "is unable to attend my party.")

# I have to invite someone else.
new_guest = "Optimus Prime"
guests[1] = new_guest
print(guests)
print("I have found a bigger table. We can invite more guests")

guests.insert(0,"Ultraman Taro")
guests.insert(2,"Ultraman Taiga")
print (guests)
print("There are "+ str(len(guests))+" guests.")

while len(guests) > 2:
	  kicked = guests.pop()
	  print("Sorry, "+kicked+", you cannot come")

print(guests)

del guests[0:2]
print(guests)
assert len(guests) == 0 #check whether the list is empty

print("------------------------Question 3-4 ends here-----------------------")

#3 - 8 look at the world 
# think about 5 places you want to travel to. 
future_travel = ["Beijing","Taibei","Ryukyu","Vietnam","Korea","Chengdu","Urumqi"]

for place in future_travel:
	print(place)

print(sorted(future_travel))
print(sorted(future_travel,reverse = True))
print(future_travel)

future_travel.reverse()
print(future_travel)
future_travel.reverse()
print(future_travel)
future_travel.sort()
print(future_travel)
future_travel.sort(reverse = True)
print(future_travel)

