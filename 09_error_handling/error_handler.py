file = open('youtube.txt','w')
# use it cautiously 
#  maybe overwriting situation , deletion by another process

# always use try catch

try:
    file.write('Chai aur code ')
finally:
    file.close()


# =============== better syntax by python ===============

with open('youtube.txt','w') as file :
    file.write('chai aur python')