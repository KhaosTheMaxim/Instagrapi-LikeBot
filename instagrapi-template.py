from instagrapi import Client
import time

print("  _____       _    __  __          _        ")
print(" |_   _|__ __| |_ |  \/  |__ ___ _(_)_ __   ")
print("   | |/ -_) _| ' \| |\/| / _` \ \ / | '  \  ")
print("   |_|\___\__|_||_|_|  |_\__,_/_\_\_|_|_|_| ")

time.sleep(3)

print("Thank You for using my code")
print("Subscribe at https://youtube.com/@TechMaximTM")

time.sleep(3)

print('Instagram Bot Starting Up')
time.sleep(2)
print('Logging In')
with open("credentials.txt", "r") as f:          # enter your credentials in the credentials.txt file
    username, password = f.read().splitlines()

#verificationcode = input("enter 2fa code: ") #remove the hashtag to uncomment this if you have 2fa on your account

client = Client()
#client.load_settings("session.json") #uncomment after running the first time
client.login(username, password)#, verification_code=verificationcode) 
client.dump_settings("session.json") # comment after running the first time with #

time.sleep(3)
print('Logged in')

hashtag = input("Enter the hashtag category you want to like: ")

def maximloop():
    medias = client.hashtag_medias_recent(hashtag, 1)
    print('loaded hashtag defined post')
    try:
        for i, media in enumerate(medias):
            client.media_like(media.id)
            print(f"Liked post number {i+1} of hashtag {hashtag}")
    except Exception as e:
        print('some kind of error occured')
        print(type(e))
    print('waiting to prevent instagram verification and like disabling')
    time.sleep(20)
    print('restarting function')
    maximloop()

maximloop()

