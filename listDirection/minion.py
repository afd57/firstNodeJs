def minion_game(string):
    vowels = ['A','E','I','O','U']
    stuart = 0
    kevin = 0
    for i in range(0,len(string)):
        score = len(string) - i + 1
        if string[i] in vowels:
            kevin += score
        else:
            stuart += score
    if stuart > kevin:
        print('Stuart',stuart)
    elif kevin > stuart:
        print('Kevin',kevin)
    else:
        print('Draw')
    # your code goes here

sub_strings = []
def substring(str):
    for i in range(len(str)):
        print(str[i:])
        sub_strings.append(str[i:])
        substring(str[i:i-1])

def minion_game_2(input_str):
    S = input_str
    n = len(S)
    # consonents
    stuart = 0
    # vowels
    kevin = 0

    for i in range(n):
        if S[i] in ('A', 'E', 'I', 'O', 'U'):
            kevin += n - i
        else:
            stuart += n - i

    if kevin > stuart:
        print('Kevin', kevin)
        print('Stuart', stuart)
    elif stuart > kevin:
        print('Stuart', stuart)
        print('Kevin', kevin)

    else:
        print('Draw')


if __name__ == '__main__':
    input_str = 'BANANA'
    minion_game(input_str)