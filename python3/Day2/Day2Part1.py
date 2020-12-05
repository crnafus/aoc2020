# Problem: find the count of valid passwords. Each day shows the # of required letters, and then the password submitted
# ex: 1-4 l : abcwer  <--- password requires 1 - 4 l's, and the password was abcwer. Therefore this is an invalid password.

def main():
    inputList = []
    with open('Day2Input.txt') as openfileobject:
        validPasswordCount = 0
        for line in openfileobject:
            firstNum = line.split('-')[0]
            secondNum = line[(len(firstNum) + 1):].split(' ')[0]
            letterToSearchFor = line[(len(firstNum) + 1 + len(secondNum) + 1):].split(':')[0]
            password = line.rsplit(':')[1].strip(' ').strip('\n')
            letterCount = 0
            
            for char in password:
                if(char == letterToSearchFor):
                    letterCount+=1
            if(letterCount >= int(firstNum) and letterCount <= int(secondNum)):
                validPasswordCount+=1
    print("Total number of valid passwords: " + str(validPasswordCount))
        
if __name__ == "__main__":
    main()


#     >>> s1.split(':')
# ['Username', ' How are you today?']
# >>> s1.split(':')[0]
# 'Username'
