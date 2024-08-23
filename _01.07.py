count = int(input())
file = open("text.txt", "w")


def add_new_person(file=open("text.txt", "w")):
    name = input()
    l_name = input()
    file.writelines(f'{name} {l_name}')


def output_pers(file = open("text.txt", "r")):
    for i in range(count):
        line = file.readline()
        print(line)
    file.close()


for i in range(count):
    add_new_person()
file.close()
output_pers()
file.close()
