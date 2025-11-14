listt = [{'name':'chai','time':'2min'},{'name':'code','time':'3min'}]

# if ou want to add something in the list , then or update , then how 


# enumerate(list,start=1)

# list(enumerate(listt,start=1))

# for i in enumerate(listt,start=1):
#     print(i)


for i,video in enumerate(listt,start=1):
    print(i,video['name'],video['time'])

