list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

sumed_list = [
    a + b for a, b in zip(list_a, list_b) #pode ser usado o zip.longest tmb                      
]

print(sumed_list)