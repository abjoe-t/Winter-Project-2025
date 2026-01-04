"""
Winter Project 2024: Sentiment Analysis Engine & Logger
Author: ABJOE T
Reg No: RA2411026011230

Description:
A session-based NLP tool that analyzes text sentiment, calculates polarity confidence,
aggregates session statistics, and logs structured data to CSV for future analysis.
"""

import csv
import uuid
from textblob import TextBlob
from datetime import datetime

# --- LOGIC LAYER ---

def get_confidence_level(score):
    """
    Determines confidence based on polarity magnitude.
    """
    abs_score = abs(score)
    if abs_score > 0.6:
        return "High"
    elif abs_score > 0.3:
        return "Medium"
    else:
        return "Low"

def analyze_text(text, session_id):
    """
    Performs NLP analysis and returns a structured dictionary.
    Output is clean (no emojis) for data storage.
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Determine Label
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "session_id": session_id,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "text": text,
        "sentiment": sentiment,
        "polarity_score": round(polarity, 2),
        "confidence": get_confidence_level(polarity)
    }

def print_session_summary(data):
    """
    Calculates and prints statistical insights from the current session.
    """
    if not data:
        print("\n[System] No data to summarize.")
        return

    scores = [item["polarity_score"] for item in data]
    positives = sum(1 for i in data if i["sentiment"] == "Positive")
    negatives = sum(1 for i in data if i["sentiment"] == "Negative")
    neutrals =  sum(1 for i in data if i["sentiment"] == "Neutral")
    avg_score = sum(scores) / len(scores)

    print("\n" + "="*30)
    print(" 📊 SESSION ANALYTICS SUMMARY")
    print("="*30)
    print(f"Total Inputs Analyzed : {len(data)}")
    print(f"Sentiment Distribution: {positives} Pos | {negatives} Neg | {neutrals} Neu")
    print(f"Average Polarity      : {avg_score:.2f}")
    print("="*30 + "\n")

def save_to_csv(data_list, filename="sentiment_dataset.csv"):
    """
    Appends session data to a persistent CSV dataset.
    """
    if not data_list:
        return
        
    keys = data_list[0].keys()
    try:
        with open(filename, 'a', newline='', encoding='utf-8') as output_file:
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            # Write header only if file is new/empty
            if output_file.tell() == 0:
                dict_writer.writeheader()
            dict_writer.writerows(data_list)
        print(f"[System] Session data successfully appended to '{filename}'")
    except Exception as e:
        print(f"[Error] Data storage failed: {e}")

# --- PRESENTATION LAYER (UI) ---

def main():
    # Generate a unique ID for this specific run (Experiment ID)
    session_id = str(uuid.uuid4())[:8]
    
    print(f"=== 🧠 AI Sentiment Analytics Tool v2.5 ===")
    print(f"Session ID: {session_id}")
    print("Type 'exit' to end session and generate report.\n")

    session_data = []
    
    # UI Mapping (Emojis strictly for display, not database)
    emoji_map = {"Positive": "😊", "Negative": "😠", "Neutral": "😐"}

    while True:
        user_input = input(">> Enter text: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("\nFinalizing session...")
            print_session_summary(session_data)
            save_to_csv(session_data)
            break
        
        if not user_input:
            continue

        # Process
        result = analyze_text(user_input, session_id)
        session_data.append(result)
        
        # Display Result
        sent_label = result['sentiment']
        conf_label = result['confidence']
        score = result['polarity_score']
        
        print(f"   [Analysis] {sent_label} {emoji_map[sent_label]} | Score: {score} | Confidence: {conf_label}")

if __name__ == "__main__":
    main()
