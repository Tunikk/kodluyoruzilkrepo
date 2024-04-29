def flatten_list(input_list):
    flattened_list = []
    for item in input_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

def reverse_nested_list(input_list):
    reversed_list = []
    for item in input_list[::-1]:
        if isinstance(item, list):
            reversed_list.append(reverse_nested_list(item))
        else:
            reversed_list.append(item)
    return reversed_list

# Kullanıcıdan giriş al
def get_input():
    user_input = input("Lütfen bir liste girin (örneğin, [[1,'a',['cat'],2],[[[3]],'dog'],4,5]): ")
    try:
        parsed_input = eval(user_input) # Kullanıcı girdisini değerlendir
        return parsed_input
    except:
        print("Geçersiz giriş! Lütfen doğru bir Python liste formatı girin.")
        return None

# Kullanıcıdan alınan giriş üzerinde işlemleri gerçekleştir
def process_input():
    input_list = get_input()
    if input_list is not None:
        print("Düzleştirilmiş Liste:", flatten_list(input_list))
        print("Ters Çevrilmiş İç İçe Liste:", reverse_nested_list(input_list))

# Programı çalıştır
process_input()
