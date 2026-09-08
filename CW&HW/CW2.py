head = """Bookstore Receipt
Order details"""

book_1 = "\n\tBook title: {}, - {}".format("Python basics", 450)
book_2 = "\n\tBook title: {}, - {}".format("Data science intro", 600)

total = "\n\ttotal is = {}".format(450+600)
ty = "\nThank you for shopping"

receipt = head + book_1 + book_2 + total + ty
print(receipt.upper())