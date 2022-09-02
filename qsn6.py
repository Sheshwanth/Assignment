Text="I am a teacher and I love to inspire and teach people"

#splitting the string and converting into set
unique_words=set(Text.split())
print(unique_words)

#using for loop to get the count of strings present in the set
count=0
for i in unique_words:
    count=count+1
print(count)