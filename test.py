'''
    Phương thức <File_name>.seek(offset)
    Chức năng: Giúp di chuyển con trỏ từ vị trí đầu file đến vị trí offset
    offset là 1 số tự nhiên
'''
f = open('test.txt', 'r')
print(f.read())

f.seek(3)

print(f.read())




