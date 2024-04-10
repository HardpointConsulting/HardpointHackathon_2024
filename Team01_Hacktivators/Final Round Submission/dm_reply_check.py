from transformers import pipeline
classifier = pipeline("zero-shot-classification")

def classify_input(input_text, prompt, label):
    classification = classifier(input_text, candidate_labels=[label], prompt=prompt)
    scores = classification['scores']
    print(scores[0])
    return scores[0] > 0.7


prompt = "whether is related to this"

def dm_reply(user):
    # user = input("user")
    if classify_input(user, prompt, "informal geetings like hi, hello"):
        return("Hi Welcome to ...")
    elif classify_input(user, prompt, "positive feedback"):
        return("Thank you for your feedback")
    elif classify_input(user, prompt, "availability of product"):
        return("Please check our website for availability")
    elif classify_input(user, prompt, "negative feedback"):
        return('sorry to hear that. Let us know your problem.')
    elif classify_input(user, prompt, "pricing") or user == 'pp':
        return("Please check out website")
    elif classify_input(user, prompt, 'delivery'):
        return ("We usually deliver the product in 7 days.")
    elif classify_input(user, prompt, "payment method"):
        return ("Both online payment and cash on delivery is available. Please check out our website.")
