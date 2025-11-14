# JSON is itself a file format , it can be start with this {}, [] and sometimes '[{},{}]'
# JSON dikhta string jaise, but syntax alag hota hai 

import json 
def load_data():
    try:
        with open('youtube.txt','r') as file:
           test =  json.load(file) # this loads the file , coverts it inot the JSON if data is present 
        #    print(type(test)) # list dikhayga leking behind the scene ye json ka list hai 
           return test
    except FileNotFoundError:
        return []
    # finally:
    #     pass

def save_data_helper(videos):
    # Try catch nahi lagaya becase mujhe empty array return nahi karna , no need
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)


def add_video(videos):
    name=input("Enter a video name: ")
    time=input("Enter video time: ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be updated"))
    if 1<=index<=len(videos):
         name = input("Enter the new video name")
         time = input("Enter the new video time")
         videos[index-1]={'name':name, 'time': time}
         save_data_helper(videos)
    else:
        print("Invalid index selected")
    


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")

"""
Here is how del works:
In-place Modification: When you use del list[index] or del list[start:end], the elements are removed directly from the existing list object in memory. The list object's identity (checked with id()) remains the same.
No Return Value: The del statement is a keyword that performs an action; it is not a function that returns a value. If you try to assign the result of a del operation to a variable, you will find it has a value of None. 

"""

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | Choose an option ")
        print("\n 1. List all youtube videos ")
        print("\n 2. Add a youtube video")
        print("\n 3. Update a youtube video details")
        print("\n 4. Delete a youtube video")
        print("\n 5. Exit the app")
        choice = input("Enter your choice: ")
        # print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

#  new keyword dunder 
if __name__=="__main__":  
    main()

