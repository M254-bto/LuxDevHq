import requests
import pandas as pd



res = requests.get("https://randomuser.me/api/?results=100").json()['results']


people_list = []     #creates empty list
for i in range(100):   #loop that accesses the results list (has individual dictionaries)
    person = res[i] 
    name = person['name']['title'] + ' ' + person['name']['first'] + ' ' + person['name']['last']
    gender = person['gender']
    email = person['email']
    people_list.append({'Name': name,'Gender':gender, 'Email':email}) #Appends the columns into a list
    
data = pd.DataFrame(people_list)     #Appends the peoples list the dataframe
male_data = data[data['Gender'] == 'male'].reset_index()
del male_data['index']

print(male_data.head())
