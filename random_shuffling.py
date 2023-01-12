"""A function that randomly puts people into groups"""

import random, sys

def list_title_string(list):
    """ This function lists all the list items as a single sentence """
    sentence = ''
    for i in range(len(list)):

        if(len(list) >= 3):
            if(i == (len(list) - 2)):
                sentence += list[i].title() + ', and '
            elif(i == (len(list) - 1)): 
                sentence += list[i].title()
            else:
                sentence += list[i].title() + ", "
        else:
            if(i == (len(list) - 2)):
                sentence += list[i].title() + ' and '
            elif(i == (len(list) - 1)): 
                sentence += list[i].title()
            else:
                sentence += list[i].title() + ", "

    return sentence

def shift(my_list):
    """ This function removes and stores the first item in the list """

    if(len(my_list) > 0):
        first_item = my_list[0]
        del my_list[0]
        return first_item

def shuffle_people(people, grouping):
    """This function adds the people to the groups based on the specified numbers per group"""
    groups = []
    new_people = []

    while len(people) > 0: # while the length of people is greater than zero             
        random_person = random.choice(people)
        current_index = people.index(random_person)
        new_people.append(random_person) # add a random person to my new people list 
        del people[current_index]# delete the person from the initial list

    # print(new_people)
        
    for number in range(len(grouping)): # add  emanpty list to represent each group
        groups.append([])

    for index, group in enumerate(groups): # loop through the empty groups
        while (len(groups[index]) < (grouping[index])): 
            new_person = shift(new_people)
            if(new_person == None):
                print("Your list is not large enough to be split into the specified groups. Fix that and try again😐")
                sys.exit()
            groups[index].append(new_person)

    parent_list_len = len(new_people)    
    if parent_list_len > 1:
        print(f"{parent_list_len} people; {(list_title_string(new_people))} do not belong to any group")
    elif parent_list_len == 1:
        print(f"{parent_list_len} person; {(list_title_string(new_people))} does not belong to any group")
 
    return groups

print(shuffle_people(['Chizzy', 'Jane', 'John', 'Frodo', 'Kim'], [2, 1, 2]))