from textblob import TextBlob
import colorama
from colorama import Fore,Style

colorama.init()

print(f"{Fore.CYAN} -------Welcome to the Sentiment Analysis Tool!--------{Style.RESET_ALL}")

user_name = input(f"{Fore.GREEN} Please enter your name: ")
print(f"{Fore.WHITE} Hello, {user_name}! Let's analyze the sentiment of your text.{Style.RESET_ALL}") 

conversation_history = []

while True:
    user_input = input("Enter text to analyze (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thank you for using the Sentiment Analysis Tool. Goodbye!")
        break

    # conversation_history.append(f"User: {user_input}")

    blob = TextBlob(user_input)
    sentiment = blob.sentiment

    response = f"{Fore.LIGHTCYAN_EX} ---Sentiment Analysis:\n- Polarity: {sentiment.polarity}\n- Subjectivity: {sentiment.subjectivity}--{Style.RESET_ALL}"
    print(response)

    conversation_history.append(f"User: {user_input} \t Bot: {response}")

    print("\nConversation History:")
    for i,entry in enumerate(conversation_history):
        print(f"S.No:{i+1}. - {entry}")
    print("\n")