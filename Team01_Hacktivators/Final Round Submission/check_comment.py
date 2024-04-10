from transformers import pipeline
classifier = pipeline("zero-shot-classification")

def classify_input(input_text, prompt, label):
    classification = classifier(input_text, candidate_labels=[label], prompt=prompt)
    scores = classification['scores']
    print(scores[0])
    return scores[0] > 0.5


prompt = "whether is related to this"
def reply_comment(input_text):
    if classify_input(input_text, prompt, "availability of product"):
        return("Please dm us")
    elif classify_input(input_text, prompt, "pricing") or input_text == 'pp':
        return("Please dm us")
    elif classify_input(input_text, prompt, "need for product"):
        return ("Please visit our website. If you have any query dm us. The ordering from dms will be available shortly.")
    elif classify_input(input_text, prompt, "good feedback"):
        return ("Thank you for your feedback")
    elif classify_input(input_text, prompt, "bad feedback"):
        return('sorry to hear that. Let us know your problem through dm.')
