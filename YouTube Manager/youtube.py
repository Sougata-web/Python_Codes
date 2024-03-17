import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            test=json.load(file)
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*" * 30)
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 30)
    

def add_video(videos):
    name = input("Enter the name of your youtube  video: ")
    time=input("Enter the timing of your youtube video: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index= int(input("Enter the video number to updaate: "))
    if 1<=index<=len(videos):
        name = input("Enter the name of your youtube  video: ")
        time=input("Enter the timing of your youtube video: ")
        videos[index-1]={'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")
        

def delete_video(videos):
    list_all_videos(videos)
    index=int(input("Enter the video number to be deleted: "))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")


def main():
    videos=load_data()

    while True:
        print("\n Youtube Manager | Choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube videos")
        print("3. Update a youtube videos")
        print("4. Delete a youtube videos")
        print("5. Exit ")

        choice = input("Enter your choice: ")

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
                print("Invalid Input")
            

if __name__=="__main__":
    main()