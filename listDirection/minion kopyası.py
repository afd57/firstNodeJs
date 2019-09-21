def minion_game(string):
    vowels = ['A','E','I','O','U']
    stuart = 0
    kevin = 0
    for i in range(0,len(string)):        
        for j in range(len(string)-i,0,-1):
            if i != j and i < j:
                print(string[i:j],i,j)
                if string[i:j][0] in vowels:
                    stuart += 1
                else:
                    kevin += 1
    if stuart > kevin:
        print('Stuart',stuart)
    else:
        print('Kevin',kevin)
    # your code goes here


def minion_game_2(input_str):
    vowels = ['A','E','I','O','U']
    stuart = 0
    kevin = 0
    sub_strings =[]
    for i in range(len(input_str)+1):
        for j in range(i):
            if(i != j):
                sub_strings.append(input_str[j:i])
    print(sub_strings)

    new_list = []

    for sub_string in sub_strings:
        if sub_string in new_list:
            continue
        new_list.append(sub_string)

    for sub_string in new_list:
        temp_string = input_str
        
        score = len(temp_string.split(sub_string))-1
        for i in range(len(input_str)+1):
            



        print(sub_string,score)
        if sub_string[0] in vowels:
            kevin = kevin + score
        else:
            stuart = stuart + score
    
    print(stuart)
    print(kevin)
    

if __name__ == '__main__':
    minion_game_2('BANANA')