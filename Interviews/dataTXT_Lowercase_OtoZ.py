def process(file_name):
    
# Файл автоматически закрывается при выходе из блока with
    with open(file_name, 'r') as file:
        for line in file:
            print(line)
        
    


process('data.txt')

# Менеджеры контекста в Python представляют собой конструкцию языка, предназначенную для облегчения управления ресурсами, такими как
# файлы, сетевые соединения или базы данных. Они используются с использованием ключевого слова with и предоставляют чистый и
#  безопасный способ управления ресурсами, так чтобы они освобождались (закрывались) правильно даже в случае возникновения исключений.
# Менеджеры контекста должны реализовывать два метода: __enter__ и __exit__.