# Start your fluency challenge here!
import re
def halved(lst):
    return [i/2 for i in lst]
    
print(halved([6,8,10]))

def only_positive(lst):
    return [i for i in lst if i > 0]
    
print(only_positive([-1,2,-3,22]))
    
def add(lst):
    return sum(lst)
    
print(add([2,3,4]))
    
def stripped_strings(lst):
    return [re.sub('\W','',string) for string in lst]

print(stripped_strings(['abc-d!hd']))

def find_special(lst):
     return [lst[i] for i in range(len(lst)) if lst[i] == "special"][0]
    
    
print(find_special(['bye','special']))

contacts = [
  {"name": 'Reuben', "phone_number": '9196218777'},
  {"name": 'Laisha', "phone_number": '0123334766'},
  {"name": 'Cielo', "phone_number": '764'},
  {"name": 'Maya', "phone_number": '7653324599'}
]

def valid_contacts(lstObj):
    return [contact for contact in lstObj if len(contact['phone_number'])== 10]
print(valid_contacts(contacts))


def contact_name(lstObj):
    return [contact['name'] for contact in lstObj]

print(contact_name(contacts))
    
