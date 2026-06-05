# 🤖 DecoBot — Rule-Based AI Chatbot
> Project 1 | Foundation Phase


Overview

DecoBot is a **rule-based AI chatbot** built in Python as part of DecodeLabs' AI Industrial Training Program. It simulates intelligent conversation using explicit control flow and dictionary-based intent matching** — no machine learning involved.
This project is the foundation of AI engineering: before building systems that learn, you must master systems that think through rules.

---

## 🎯 Project Goal

Build a simple rule-based chatbot that:
- Responds to predefined user inputs using a **Python dictionary**
- Runs in a **continuous while loop** (the "heartbeat")
- Handles **input sanitization** (case & whitespace)
- Provides a **fallback response** for unknown inputs
- Supports a **clean exit command** to terminate the session

---

## 🏗️ Architecture — The IPO Model

```
┌─────────────────────────────────────────────────────────┐
│                    IPO ARCHITECTURE                      │
├──────────────┬──────────────────────┬───────────────────┤
│    INPUT     │       PROCESS        │      OUTPUT       │
│              │                      │                   │
│ raw_input    │  responses.get()     │  print(reply)     │
│ .lower()     │  O(1) dict lookup    │  → loop back      │
│ .strip()     │  + fallback          │                   │
└──────────────┴──────────────────────┴───────────────────┘
```

---

## 📂 Project Structure

```
decobot-project1/
│
├── decobot_project1.py     # Python chatbot (terminal version)
├── decobot_ui.html         # Browser UI (dark theme, HTML/CSS/JS)
└── README.md               # This file
```

---

## ⚙️ Key Concepts

 1. The Heartbeat — Infinite Loop
```python
while True:
    user_input = input("You: ")
    if user_input in EXIT_COMMANDS:
        break                  # kill command — clean exit
    reply = get_response(user_input)
    print(f"DecoBot: {reply}")
```

### 2. Input Sanitization
```python
raw_input  = input("You: ")
clean_input = raw_input.lower().strip()
# "Hello  " → "hello"
# "HELLO"   → "hello"
# "hElLo"   → "hello"
```
 3. Knowledge Base — Dictionary O(1)
```python
responses = {
    "hello":       "Hello! How can I help you today?",
    "what is ai":  "AI is the simulation of human intelligence by machines.",
    "python":      "Python is the #1 language for AI/ML development.",
    # ... 25+ intents
}
```

### 4. The .get() Method — Professional Approach
```python
# ❌ Anti-pattern — O(n) if-elif ladder
if clean_input == "hello":
    reply = "Hello!"
elif clean_input == "hi":
    reply = "Hey there!"
... 20 more elifs

 Professional — O(1) dictionary lookup
reply = responses.get(clean_input, "I don't understand that yet.")
```

 5. Exit Strategy
```python
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}

if clean_input in EXIT_COMMANDS:
    print("DecoBot: Goodbye!")
    break
```

---

## 📊 Algorithmic Efficiency

| Method     | Time Complexity | Scales Well? |
|------------|-----------------|--------------|
| if-elif    | O(n) — linear   | ❌ No        |
| dict.get() | O(1) — constant | ✅ Yes       |

A dictionary with **10,000 rules** performs just as fast as one with **2 rules**. An if-elif chain gets slower with every rule added.

---

## ✅ Project Specifications Checklist

- [x] **INPUT LOOP** — Continuous `while True` cycle
- [x] **SANITIZATION** — Handle case & whitespace with `.lower().strip()`
- [x] **KNOWLEDGE BASE** — Dictionary with 25+ intents
- [x] **FALLBACK** — Default response for unknown inputs
- [x] **EXIT STRATEGY** — Clean `break` on exit command

---

## 🚀 How to Run

### Terminal Chatbot (Python)
```bash
# Make sure Python 3 is installed
python decobot_project1.py
```

**Sample Session:**
```
========================================================
  DecoBot v1.0  --  Rule-Based AI Chatbot
  DecodeLabs | AI Industrial Training Kit | Batch 2026
========================================================
  Engine  : Dictionary O(1) lookup
  Model   : IPO (Input → Process → Output)
  Rules   : 25 intents loaded
--------------------------------------------------------

You: hello
DecoBot: Hello! I'm DecoBot, your rule-based AI assistant.

You: what is ai
DecoBot: AI is the simulation of human intelligence by machines...

You: exit
  [ while loop: BREAK ]
DecoBot: Goodbye! Thanks for chatting. Session ended.
```

### Browser UI (HTML)
```
Simply open decobot_ui.html in any web browser.
No installation required.
```

---

## 💡 Why Rule-Based AI Still Matters

Even in the era of ChatGPT and LLMs, rule-based systems are critical:

| Property        | Rule-Based ✅    | LLM Only ⚠️     |
|-----------------|-----------------|-----------------|
| Traceability    | Full (white box)| Limited         |
| Hallucination   | Zero risk       | Possible        |
| Compliance      | Guaranteed      | Not guaranteed  |
| Speed           | O(1) instant    | API latency     |

> *Frameworks like NVIDIA NeMo and Llama Guard use rule-based guardrails on top of LLMs for exactly this reason. This project builds that control layer.*

---

## 🔧 Tech Stack

| Layer    | Technology              |
|----------|-------------------------|
| Backend  | Python 3                |
| Logic    | Dictionary + while loop |
| Terminal | ANSI color codes        |
| UI       | HTML5, CSS3, JavaScript |
| Font     | JetBrains Mono, Space Grotesk |

---

## 🌱 Future Improvements

- [ ] Add keyword/substring matching (not just exact match)
- [ ] Connect to a real NLP library (spaCy / NLTK)
- [ ] Store conversation history to a `.txt` or `.json` file
- [ ] Add multi-turn context (remember previous messages)
- [ ] Integrate with an LLM API as fallback (hybrid architecture)


---

> *"An LLM without rules is a hallucination engine.*
> *Today, we build the skeleton that holds the intelligence."*
> — DecodeLabs, Module 01
