import json

def go_back(item, parents,step=-2):
    """
    element of dictionary, all previous elements ->
    previous element, all previous elements without current one 

    The function turns back in the tree
    """
    try:
        item = parents[step]
        if len(parents) > 2:
            parents = parents[:-1]
    except:
        item = data
        parents = [data]

    
    return item, parents
    

def for_dict(item, parents):
    """
    this function is to display and navigate through the dictionary
    """
    while True:
        
        if type(item) == list:
            for_list(item, parents)
            break

        if type(item) != dict:
            print()
            print("The value is",item)
            print()
            answ = input(" You are in the lovest stage of the json file"+
                            "\nWould you like to go back? [Y/N] ")
            if len(answ) < 1:
                    break      
            while answ != "Y" and answ != "N":
                answ = input(" You are in the lovest stage of the json file"+
                            "\nWould you like to go back? [Y/N] ")
                if len(answ) < 1:
                    break 
            
            if answ == "Y":
                item, parents = go_back(item, parents)
                continue
            else :
                break

        print()
        print("---There are these keys in the chosen dictionary---")
        for el in item.keys():
            print(el)
        # print("--------------------------")
        print()

        answ = input("In whick key would you like to go in the dictionary?"+
                    "\nor enter 'gb' to go back in the tree ")
        if len(answ) < 1:
            break
        # item = answ 
        
        while answ not in item.keys() and answ != "gb":
            answ = input("In whick key would you like to go in the dictionary?"+
                        "\nor enter 'gb' to go back in the tree ")
            if len(answ) < 1:
                break 
        if answ == "gb":
            item, parents = go_back(item, parents)
            continue

        item = item[answ]
        parents.append(item)


def for_list(item, parents):
    """
    this function is to display and navigate through the list
    """
    while True:
        if type(item) == dict:
            for_dict(item, parents)
            break
        if type(item) != list and type(item) != dict:
            print()
            print("The value is", item)
            print()
            answ = input(" You are in the lovest stage of the json file"+
                            "\nWould you like to go back? [Y/N] ")
            if len(answ) < 1:
                    break         
            while answ != "Y" and answ != "N":
                answ = input(" You are in the lovest stage of the json file"+
                            "\nWould you like to go back? [Y/N] ")
                if len(answ) < 1:
                    break 
            
            if answ == "Y":
                item, parents =  go_back(item, parents)
                continue
            else :
                break
                         
                

        print()
        print("---You are in the chosen list item---")
        print(f"---Here are {len(item)} elements with the same keys---")
        print()

        while True:
            try:
                answ = input(f"In which list item would you like to go? (only number from 1 to {len(item)})"+
                                "\nor enter 'gb' to go back ")
                if len(answ) < 1:
                    break
                # item = answ 
                
                while answ != "gb" and (int(answ) - 1) not in range(len(item)):
                    answ = input(f"In which list item would you like to go? (only number from 1 to {len(item)}) "+
                                "\nor enter 'gb' to go back ")
                    if len(answ) < 1:
                        break
                break
                
            except:
                continue        
        if len(answ) < 1:
                    break
        
        if answ == "gb":
            item, parents = go_back(item, parents)
            continue

        item = item[int(answ) - 1]
        parents.append(item)


if __name__ == "__main__":
    path = "Twitter.json"
    with open(path, 'r', encoding="utf-8") as f:
        data = json.load(f)

    item = data
    parents = [data]
    for_dict(item, parents)