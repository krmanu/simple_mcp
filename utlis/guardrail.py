import re

PROMPT_INJECTION_PATTERNS = [
    "ignore previous instructions",
    "ignore all instructions",
    "reveal system prompt",
    "show system prompt",
    "bypass security",
    "developer mode",
    "act as administrator"
]

BLOCKED_TOPICS = [
    "malware",
    "phishing",
    "ransomware",
    "password cracking",
    "credit card fraud"
]

def input_guardrail(query):

    query_lower = query.lower()

    for pattern in PROMPT_INJECTION_PATTERNS:
        if pattern in query_lower:
            return False , "Your query contains potentially harmful instructions. Please rephrase your question."
    
    for topic in BLOCKED_TOPICS:
        if topic in query_lower:
            return False , "Your query contains a blocked topic. Please ask about something else."
    
    return True, None

def output_guardrail(response):

    response = re.sub(
        r"\S+@\S+\.\S+",
        "[EMAIL_REDACTED]",
        response
    )

    response = re.sub(
        r"\b\d{10}\b",
        "[PHONE_REDACTED]",
        response
    )

    response = re.sub(
        r"\b\d{16}\b",
        "[CARD_REDACTED]",
        response
    )

    return response