from flask import Flask, render_template, request, jsonify,redirect
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import kg
from kg import knowledge_graph

from transformers import AutoModelForCausalLM, AutoTokenizer,AutoModelForSequenceClassification

import torch


tokenizer = AutoTokenizer.from_pretrained('law-ai/InLegalBERT')
model = AutoModelForSequenceClassification.from_pretrained("C:\\Users\\SHRIYA SENTHILKUMAR\\Downloads\\ChatBot\\ChatBot\\intent_classification_model2")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    text= find_similarity(input)
    return text

    
#def get_narration():
 #   return ("It seems that you would like to narrate your incident. Kindly feel free to narrate!")


@app.route("/handle_narration", methods=["GET", "POST"])
def handle_narration():
    user_input = request.form["narration"]
    reply_message,pred_intent = intent_identification(user_input)
    pred_intent=pred_intent.lower()
    defn=kg.knowledge_graph[pred_intent]["defined as"]
    return  reply_message+defn

@app.route("/handle_law", methods=["GET", "POST"])
def handle_law():
    user_input = request.form["law"]
    reply_message = search_kg(user_input)
    return reply_message


def search_kg(input):
    content = kg.knowledge_graph[input]["law_defined"]
    return content


@app.route("/handle_proc", methods=["GET", "POST"])
def handle_proc():
    user_input=request.form["proc"]
    reply_message= steps(user_input)
    return reply_message

def steps(input1):
    content = kg.knowledge_graph[input1]["reporting_steps"]
    return content



def intent_identification(narration_story):
    inputs = tokenizer(narration_story, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
    predicted_labels = torch.argmax(outputs.logits, dim=1).tolist()
    label_mapping = {0: 'Cyber Bullying', 1: 'Cyber Defamation', 2: 'Cyber Harassment', 3: 'Cyber Stalking', 4: 'Hacking', 5: 'Phishing', 6: 'Privacy'}
    predicted_intent = [label_mapping[label] for label in predicted_labels]
    reply_message = f"Based on your narration, I feel that the incident is : {predicted_intent[0]}. "
    return reply_message,predicted_intent[0]


def find_similarity(input_text):
    options = [
    "Get personalized help by narrating your incident.",
    "Get to know about the Law.",
    "Procedures to File a Complaint"
    ]
    corpus = options + [input_text]
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    most_similar_index = similarity_scores.argmax()
    most_similar_option = options[most_similar_index]
    print("Most Similar Option:", most_similar_option)
    print("Cosine Similarity Score:", similarity_scores.max())

    return most_similar_option

    
def get_Chat_response(text):
    return text


if __name__ == '__main__':
    app.run()
