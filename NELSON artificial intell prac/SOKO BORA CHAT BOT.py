# Soko Bora Supermarket Customer Help Desk
# 1. Display the welcome message
print("Welcome to Soko Bora Supermarket Customer Help Desk!")

# 2. Keep asking the customer questions
while True:
    question = input("Customer: ").lower()

    # 3. Match the customer's question to a keyword
    if "delivery" in question:
        print("Chatbot: Standard delivery takes 3-5 business days.")

    elif "payment" in question:
        print("Chatbot: We accept M-Pesa, Visa and Mastercard.")

    elif "return" in question:
        print("Chatbot: Items can be returned within 7 days of purchase.")

    elif "hours" in question:
        print("Chatbot: We are open Monday to Saturday, 8am to 6pm.")

    elif question == "exit":
        print("Chatbot: Thank you for contacting Soko Bora Supermarket. Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I did not recognize that keyword.")