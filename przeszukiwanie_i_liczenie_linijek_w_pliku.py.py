
name = input("wpisz nazwę pliku:")

try:
    file = open(name)
except:
    print("Nie można wyświetlić pliku -", name, "lub wpisano błędną nazwę.")
    exit()

subject = input("wpisz temat:")

counter = 0
for line in file:
    line = line.rstrip()
    if line.startswith(subject):
        counter = counter + 1
        print(line)

print("Jest", counter, "linijek z treścią -", subject,  "w pliku", name)

