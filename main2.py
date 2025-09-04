from textblob import TextBlob
# import nltk
# nltk.download('punkt')


user_input = input("Enter text to analyze: ")
blob = TextBlob(user_input)
sentiment = blob.sentiment
print(f"Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}")


if sentiment.polarity > 0.25:
    print("The sentiment of the text is Positive.")

elif sentiment.polarity < -0.25:
    print("The sentiment of the text is Negative.")

else:
    print("The sentiment of the text is Neutral.")