#menghitung jumlah elemen
St = "Pelita Bangsa"
print(len(St))

#ditambah
t = "Universitas " + St
print(t)

#ditampilkan sesuai keinginan
u = "nadia " *3
print(u)

#menghitung jumlah elemen
String1 = 'Welcome to Universitas Pelita Bangsa' 
print("String with the use of Single Quotes: ") 
print(len(String1))

#menjabarkan kebawah elemen String1
for T in String1:
    print(T)

#menentukan apakah kalimat ini ada di dalam string1
print("Universitas" in String1)

Name = "Nadia Aulina Safari"

#mengecilkan elemen
print(Name.lower())
#menentukan apakah digit atau huruf
print(Name.isdigit())
#menentukan apakah ada kata tsb di dalam elemen
print(Name.find("Nadia"))
#memisahkan perkata dari elemen
print(Name.split())
#membuat kata tambahan
print("Welcome to {0} with {1}!".format(Name, "Friend"))
#mengganti elemen
print(Name.replace("Aulina Safari", "Aulina"))      

String2 = "I'm a college student" 
print("\nString with the use of Double Quotes: ") 
print(String2) 

String3 = '''I'm a new college student in "UPB"''' 
print("\nString with the use of Triple Quotes: ") 
print(String3) 

String4 = '''Pelita
Bangsa
University''' 
print("\nCreating a multiline String: ") 
print(String4) 

String5 = "Universitas Pelita Bangsa" 
print("Initial String: ", String5) 
# Printing First character 
print("First character of String is: ", String5[0]) 

String6 = "UPB" 
print("Initial String: ", String6) 
# Printing Last character 
print("Last character of String is: ", String6[-3])

 
# Creating a String 
String7 = "Information Technik" 
print("Initial String: ") 
print(String7) 
 
# Printing 3rd to 12th character 
print("\nSlicing characters from 3-12: ") 
print(String1[3:12]) 
 
# Printing characters between 
# 3rd and 2nd last character 
print("\nSlicing characters between " + 
      "3rd and 2nd last character: ") 
print(String1[3:-2]) 

 
#Program to reverse a string 
gfg = "Pelita Bangsa UPB" 
print(gfg[::-1])

# Program to reverse a string 
gfg = "universitaspelitabangsaa" 
# Reverse the string using reversed and join function 
gfg = "".join(reversed(gfg)) 
print(gfg) 

  
String1 = "Hello, I'm a Geek" 
print("Initial String: ") 
print(String1) 
 
print("Deleting character at 2nd Index: ") 
del String1[2] 
print(String1) 
    
#Python Program to Delete 
# Input String 
 
String8 = "Hello, I'm Nadia" 
print("Initial String: ") 
print(String8) 
 
# Deleting a String 
# with the use of del 
del String8
print("\nDeleting entire String: ") 
print(String8)

# Initial String 
String9 = '''I'm a "Geek"''' 
print("Initial String with use of Triple Quotes: ") 
print(String9) 
 
# Escaping Single Quote 
String10 = 'I\'m a "Geek"' 
print("\nEscaping Single Quote: ") 
print(String10) 
 
# Escaping Double Quotes 
String11 = "I'm a \"Geek\"" 
print("\nEscaping Double Quotes: ") 
print(String11) 
 
# Printing Paths with the 
# use of Escape Sequences 
String12 = "C:\\Python\\Geeks\\" 
print("\nEscaping Backslashes: ") 
print(String12) 
# Printing Paths with the 
# use of Tab 
String13 = "Hi\tGeeks" 
print("\nTab: ") 
print(String13) 
# Printing Paths with the 
# use of New Line 
String14 = "Python\nGeeks" 
print("\nNew Line: ") 
print(String14)