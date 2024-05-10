# import random
# 
# # print(random.random())
# # print(random.randint(1,100))
# # print(random.randrange(1,100,2))
# 
# # musics = ['music-1', 'music-2', 'music-3', 'music-4', 'music-5']
# # 
# # random.shuffle(musics)
# # print(musics)
# 
# 
# # print(dir(random))
# 
# import math
# 
# # print(dir(math))
# # print(math.factorial(5))
# # print(math.sqrt(25))
# 
# import datetime
# 
# # print(datetime.datetime.now())
# # print(datetime.datetime.now().date())
# # print(datetime.datetime.now().time())
# 
# current_datetime = datetime.datetime.now()
# # print(current_datetime.strftime('%d/%m/%Y, %I:%M:%S'))
# print(current_datetime.strftime('%d-%m-%Y %I:%M %p'))

# https://docs.python.org/3/library/datetime.html


# from datetime import datetime, timedelta
# print(datetime.astimezone())
# 
# current_datetime = datetime.now()
# f_time = current_datetime - timedelta(days=1, hours=1)
# print(f_time)


# import datetime
# import pytz
# 
# # Get the current time in UTC
# utc_now = datetime.datetime.utcnow()
# 
# # Localize the UTC time to get the current time zone
# current_timezone = pytz.utc.localize(utc_now).astimezone()
# 
# # Get the name of the current time zone
# timezone_name = current_timezone.tzname()
# 
# print("Current time zone:", timezone_name)


# import base64
# 
# # String to encode
# text = "Hello, world!"
# 
# # Encode the string to Base64
# encoded_text = base64.b64encode(text.encode()).decode()
# 
# print("Encoded:", encoded_text)
# 
# # Decode the Base64 encoded string
# decoded_text = base64.b64decode(encoded_text).decode()
# 
# print("Decoded:", decoded_text)


# import uuid
# 
# print(uuid.uuid4())