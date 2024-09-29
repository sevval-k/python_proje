def reverse_nested_list(input_list):
    # Listeyi tersine çevir
    reversed_list = []

    for item in input_list:
        if isinstance(item, list):
            # Eğer eleman bir listeyse, iç listeyi tersine çevir
            reversed_list.append(reverse_nested_list(item))
        else:
            # Diğer türdeki elemanları ekle
            reversed_list.append(item)

    return reversed_list[::-1]  # Dış listeyi tersine çevir

# Örnek kullanım
input_data = [[1, 2], [3, 4], [5, 6, 7]]
output_data = reverse_nested_list(input_data)
print(output_data)  # [[[7, 6, 5], [4, 3], [2, 1]]]
