def countVowels():
    str1 = 'hello'
    vowels = 'aeiouAEIOU'
    count = 0

    for i in str1:
        if i in vowels:
            count+=1
    return (f'total count of vowels are: {count}')     

#print(countVowels())   

str1= "hello" 
rev= '' 
for i in str1[::-1]:
    rev+=i
   
print(rev)


# pallindrome or not

def paillndronme(string):
    rev = string[::-1]

    if string == rev:
        print(f"{string} is an Pallindrome")
    else:
        print(f'{string} is not pallindrome')   
    
paillndronme('madam')

str2 = "Hello"
vowels = 0
consolant = 0
for i in str2:
    if i in 'aeiouAEIOU':
        vowels += 1
    else:
        consolant += 1
print(f'Total Vowels Are: {vowels}') 
print(f'total Consolants are: {consolant}')           




