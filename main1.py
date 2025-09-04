from textblob import TextBlob

print("Welcome to the Sentiment Analysis Tool!")

user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Let's analyze the sentiment of your text.") 

conversation_history = []

while True:
    user_input = input("Enter text to analyze (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thank you for using the Sentiment Analysis Tool. Goodbye!")
        break

    # conversation_history.append(f"User: {user_input}")

    blob = TextBlob(user_input)
    sentiment = blob.sentiment

    response = f"Sentiment Analysis:\n- Polarity: {sentiment.polarity}\n- Subjectivity: {sentiment.subjectivity}"
    print(response)

    conversation_history.append(f"User: {user_input} \t Bot: {response}")

    print("\nConversation History:")
    for i,entry in enumerate(conversation_history):
        print(f"S.No:{i+1}. - {entry}")
    print("\n")