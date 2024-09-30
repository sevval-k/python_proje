def reverse_nested_list(input_list):
    # Listeyi tersine çeviren bir fonkşyon belirle
    reversed_list = []

    for item in input_list:
        if isinstance(item, list): 
             
            reversed_list.append(reverse_nested_list(item)) #item bir listeyse, fonksiyonu kendisi tekrar çağırır (reverse_nested_list(item)) ve 
                                                            #alt listeyi ters çevirip sonucu reverse_list'e ekler.
        else:
            # Diğer türdeki elemanları ekle
            reversed_list.append(item)

    return reversed_list[::-1]  #  #[start:stop:step] şeklinde çalışır ve step negatif olduğunda listeyi ters sırayla alır.

# Örnek kullanım
input_data = [[1, 2], [3, 4], [5, 6, 7]]
output_data = reverse_nested_list(input_data)
print(output_data)  # [[[7, 6, 5], [4, 3], [2, 1]]]
