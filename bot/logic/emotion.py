# emotion.py
def detect_emotions_and_symptoms(text: str) -> dict:
    # This will hold results
    results = {
        "symptoms": [],
        "emotions": []
    }

    # List of keywords (for now, keep it simple)
    symptom_keywords = ["fever", "cough", "headache", "nausea", "sore throat", "fatigue"]
    emotion_keywords = ["fever", "headache", "cough", "nausea", "fatigue", "sore throat", "chills"]

    # Lowercase for comparison
    lowered = text.lower()

    # Find matches by looping through
    for word in symptom_keywords:
        if word in lowered:
            results["symptoms"].append(word)

    for word in emotion_keywords:
        if word in lowered:
            results["emotions"].append(word)

    return results

