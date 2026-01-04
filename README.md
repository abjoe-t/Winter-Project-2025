# Winter Project 2025: Sentiment Analytics Engine 🧠

## 📌 Project Overview
This project is a session-based Natural Language Processing (NLP) tool designed to analyze, score, and log human sentiment from textual data. Beyond simple classification, the system generates **confidence metrics**, aggregates **statistical insights**, and maintains a persistent **structured dataset** (CSV) for historical analysis.

## 🚀 Key Technical Features
- **NLP Polarity Scoring:** Uses `TextBlob` to calculate sentiment magnitude (-1.0 to +1.0).
- **Confidence Estimation:** Dynamic logic to categorize results (High/Medium/Low) based on score intensity.
- **Session Management:** unique UUIDs generated for every run to isolate experimental batches.
- **Data Persistence:** Automated appending of structured logs to `sentiment_dataset.csv`.
- **Statistical Aggregation:** Generates real-time distribution summaries (Mean Score, Class Counts) at the end of every session.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:**
  - `TextBlob` (NLP Core)
  - `uuid` (Session Tracking)
  - `csv` (Data Serialization)
  - `datetime` (Temporal Logging)

## 📊 Workflow
1. **Input:** User provides text samples.
2. **Process:** System calculates Polarity and Subjectivity.
3. **Logic:** Derives Sentiment Label and Confidence Level.
4. **Log:** Appends data to CSV with Timestamp and Session ID.
5. **Output:** Displays immediate analysis and end-of-session statistical summary.

## 👤 Author
- **Name:** ABJOE T
- **Reg No:** RA2411026011230
- **Department:** CINTEL (CSE - AIML)
