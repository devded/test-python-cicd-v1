from datetime import datetime
print("Hello World! CICD")

print("Hello World")

data = datetime.now()
print(data)

with open('test.txt', 'w') as f:
    f.write(str(data))


