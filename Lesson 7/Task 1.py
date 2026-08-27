#Task 1
raw_user_record = input()
user_data = raw_user_record.split(';')
for i in range(len(user_data)):
    user_data[i] = user_data[i].strip()
user_data[0] = f'UID-{user_data[0]}'
user_data[1] = user_data[1].title().replace('_', ' ')
user_data[2] = user_data[2].upper()
user_data[3] = user_data[3].lower()
result = "|".join(user_data)
print(result)