#напиши тут свою програму
def read_file(name_file):
    with open (name_file,"r",encoding='utf-8') as file:
        data = file.read()
        file.close()
        return data
    
def add_to_file(name_file, new_info):
    with open(name_file, "a", encoding='utf-8') as file:
        file.write ("\n"+new_info)
        file.close()
data_file = read_file ("quotes1. txt")

add_to_file ("quotes1. txt", "")
print (data_file)