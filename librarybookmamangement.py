books = ["python","java","c++","sql"]

print("Available books:")
for i in books:
    print(i)

    books.remove("java")
    print("Books After Issue")

    for i in books:
        print(i)