import sys as system
system.stdout.write("Wpisz dowolny napis: ")
napis = system.stdin.readline()
system.stdout.write(napis)

litera = "a"

count = napis.count(litera)
print("Liczba 'a' w napisie:",count)