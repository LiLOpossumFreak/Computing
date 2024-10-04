#Input Validation - Book Catalogue

print("""
      MENU OPTIONS
      1. Add Book
      2. View Catalog
      3. Search Books
      4. Exit""")
options = int(input("Please answer one of the options above!! I'm begging you PLEASE BRO: "))
while options <1 or options >4 :
    options = int(input("ERROR!!!!!!!!!!Please answer one of the options above!! I'm begging you PLEASE BRO: "))