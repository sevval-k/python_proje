def flatten(input_list):
    result = []
    
    for item in input_list:
        if isinstance(item, list):
            result.extend(flatten(item))  # Eğer eleman bir listeyse, onu düzleştir ve ekle
        else:
            result.append(item)  # Diğer türdeki elemanları ekle

    return result

# Örnek kullanım
input_data = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
output_data = flatten(input_data)
print(output_data)  # [1, 'a', 'cat', 2, 3, 'dog', 4, 5]
