# Update Values in Dictionaries and Lists
from re import S


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students[0])

sports_directory["soccer"][0] = "Andres"
print(sports_directory['soccer'])

z[0]["y"] = 30
print(z)

#2 Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterate_dictionary(stu):
    for each_dict in stu:
        # for key, val in each_dict.items():
            # print(key, " - ", val)
        #that way on 2 different lines

        print("first_name - " + each_dict["first_name"] + ", last_name - " + each_dict["last_name"]) #is that cheating?
        #doesn't seem to work using .keys/.values or .items

iterate_dictionary(students) 

def iterate_dictionaryb(stu):
    for each_dict in stu:
        key_names = []
        value_names = []
        for key, val in each_dict.items():
            key_names.append(key)
            value_names.append(val)
        print(key_names[0] + " - " + value_names[0] + ", " + key_names[1] + " - " + value_names[1]) # That looks better
        #still, i feel like there is an easier way to do that
            
iterate_dictionaryb(students)

#3 Get Values from a List of Dictionaries
def interate_dictionary2(key_name, stu):
    for obj in stu:
        print(obj[key_name])

interate_dictionary2("last_name",students)    

#4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dojo_info):
    
    for key in dojo_info:
        print("-----------------")
        print(len(dojo_info[key]), key.upper())
        for location in dojo_info[key]:
            print(location)

print_info(dojo)