# ============================================================
#  DecodeLabs
#  Project 1: Rule-Based AI Chatbot (Complete Version)
#  Skills: Control Flow, Decision Logic, Basic AI Concepts
#
#  Architecture: IPO Model
#    INPUT  → Sanitization & Normalization
#    PROCESS→ Intent Matching via Dictionary O(1)
#    OUTPUT → Response Generation + Feedback Loop
# ============================================================

import time

# ── ANSI COLOR CODES (Terminal Styling) ──────────────────────
class Color:
    TEAL    = '\033[38;5;36m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'
    GRAY    = '\033[90m'
    BOLD    = '\033[1m'
    RESET   = '\033[0m'
    CYAN    = '\033[96m'


# ── PHASE 2: KNOWLEDGE BASE (Dictionary — O(1) lookup) ──────
#    Using dict instead of if-elif ladder avoids O(n) scanning.
#    dict.get(key, fallback) is always O(1) constant time.
RESPONSES = {
    # ── Greetings ────────────────────────────────────────────
    "hello":            "Hello! I'm DecoBot, your rule-based AI assistant. How can I help you today?",
    "hi":               "Hey! Great to see you. Ask me about AI, Python, or this project.",
    "hey":              "Hey there! I'm running on pure rule-based logic. What's on your mind?",

    # ── Farewells ────────────────────────────────────────────
    "thanks":           "You're welcome! Anything else I can assist with?",
    "thank you":        "My pleasure! Always here to help.",

    # ── Help ─────────────────────────────────────────────────
    "help":             "I can answer questions on: AI, Python, this project, DecodeLabs, IPO model, dictionaries, and loops. Try one!",

    # ── AI Topics ────────────────────────────────────────────
    "what is ai":       "AI (Artificial Intelligence) is the simulation of human intelligence by machines. Rule-based AI uses explicit logic rules. Advanced AI uses machine learning and neural networks.",
    "ai":               "AI has two sides: (1) Probabilistic — neural networks that learn from data; (2) Deterministic — rule-based systems like this bot.",
    "neural network":   "Neural networks are probabilistic — they learn from data. This chatbot is deterministic — it follows explicit rules. Master rules before learning networks!",
    "machine learning": "Machine learning lets AI learn from data automatically. This project is the foundation — before ML, you must master deterministic control flow.",

    # ── Python ───────────────────────────────────────────────
    "what is python":   "Python is a high-level, readable programming language — the #1 choice for AI/ML. Libraries like NumPy, Pandas, and TensorFlow make it extremely powerful.",
    "python":           "Python is great for AI! Its clean syntax and powerful libraries (NumPy, Pandas, scikit-learn, TensorFlow) make it the industry standard.",

    # ── Project ──────────────────────────────────────────────
    "project 1":        "Project 1 specs: (1) while True input loop (2) sanitization: lower+strip (3) dictionary with 5+ intents (4) fallback for unknowns (5) clean exit command. All done right here!",
    "project":          "DecodeLabs Project 1 — Rule-Based AI Chatbot. Teaches control flow, decision logic, and basic AI through hands-on building.",
    "decodelabs":       "DecodeLabs is an AI training organization in Greater Lucknow, India. They help students build real-world AI portfolios through hands-on industrial projects.",
    "batch 2026":       "Batch 2026 is DecodeLabs current AI Industrial Training cohort — building projects to create professional AI portfolios.",

    # ── Architecture ─────────────────────────────────────────
    "ipo model":        "IPO = Input → Process → Output. Input: sanitize raw text. Process: dict.get() O(1) lookup. Output: print reply and loop back. Foundational blueprint for all controlled AI.",
    "what is ipo":      "IPO (Input-Process-Output) is the core architecture: raw input → sanitize → match intent → generate response → loop back. The backbone of this chatbot.",
    "dictionary":       "Python dict stores key-value pairs. dict.get(key, default) runs in O(1) constant time. A 10,000-rule dict is just as fast as a 2-rule dict!",
    "loop":             "The 'while True:' loop is the chatbot's heartbeat. It waits for input, processes it, and loops forever until a kill command (exit/quit) breaks the cycle.",
    "sanitize":         "Sanitization = raw_input.lower().strip(). Converts 'Hello  ', 'HELLO', 'hElLo' all to 'hello'. This ensures dictionary lookups always work correctly.",
    "o(1)":             "O(1) = constant time. Dictionary lookup is always O(1) regardless of size. If-elif chain is O(n) — gets slower as more rules are added.",
    "if else":          "If-elif chains scan rules one by one — O(n) linear complexity, hard to maintain. Dictionaries replace them with O(1) instant lookups.",
    "white box":        "A rule-based system is a 'white box' — every decision is fully traceable. Input → Logic → Output. No mystery, no hallucination risk. Essential for Finance and Healthcare compliance.",

    # ── Bot self-awareness ───────────────────────────────────
    "how are you":      "I'm a deterministic program — no feelings, but all systems nominal! The while loop is running and the dict is loaded and ready.",
    "who are you":      "I'm DecoBot v1.0, a rule-based chatbot for DecodeLabs Project 1. I use Python dictionaries for O(1) intent matching instead of slow if-elif ladders.",
    "what are you":     "I'm a rule-based AI chatbot. I simulate conversation through explicit if-else logic and dictionary lookups — no machine learning involved.",
}

# ── FALLBACK RESPONSE ────────────────────────────────────────
FALLBACK = (
    "I don't have a rule for that yet. "
    "Try: hello, what is ai, python, project 1, ipo model, dictionary, or help."
)

# ── EXIT KEYWORDS ─────────────────────────────────────────────
EXIT_COMMANDS = {"exit", "quit", "bye", "goodbye"}


# ── HELPER FUNCTIONS ─────────────────────────────────────────

def print_header():
    """Prints the welcome banner."""
    w = 56
    print(f"\n{Color.TEAL}{'=' * w}{Color.RESET}")
    print(f"{Color.BOLD}{Color.TEAL}  DecoBot v1.0  --  Rule-Based AI Chatbot{Color.RESET}")
    print(f"{Color.GRAY}  DecodeLabs | AI Industrial Training Kit | Batch 2026{Color.RESET}")
    print(f"{Color.TEAL}{'=' * w}{Color.RESET}")
    print(f"{Color.GRAY}  Engine  : Dictionary O(1) lookup{Color.RESET}")
    print(f"{Color.GRAY}  Model   : IPO (Input → Process → Output){Color.RESET}")
    print(f"{Color.GRAY}  Rules   : {len(RESPONSES)} intents loaded{Color.RESET}")
    print(f"{Color.GRAY}  Tip     : Type 'help' to see topics. Type 'exit' to quit.{Color.RESET}")
    print(f"{Color.TEAL}{'-' * w}{Color.RESET}\n")


def get_response(clean_input: str) -> str:
    """
    PHASE 2 -- PROCESS (Intent Matching)
    Uses dict.get() for O(1) constant-time lookup with fallback.
    Professional alternative to an if-elif ladder.
    """
    return RESPONSES.get(clean_input, FALLBACK)


def simulate_typing(delay: float = 0.4):
    """Simulates bot thinking for better UX."""
    print(f"{Color.GRAY}  DecoBot is typing...{Color.RESET}", end="\r", flush=True)
    time.sleep(delay)
    print(" " * 30, end="\r")


# ── MAIN CHATBOT FUNCTION ─────────────────────────────────────

def chatbot():
    """
    Main chatbot loop.
    Implements the full IPO Model:
      INPUT  --> raw_input.lower().strip()    (Sanitization)
      PROCESS--> RESPONSES.get(key, FALLBACK) (Intent Matching)
      OUTPUT --> print(reply)                  (Response + Loop)
    """
    print_header()

    msg_count = 0

    # ── THE HEARTBEAT: Infinite Loop ─────────────────────────
    while True:

        try:
            # ── PHASE 1: INPUT & SANITIZATION ────────────────
            raw_input = input(f"{Color.CYAN}You: {Color.RESET}")
            clean_input = raw_input.lower().strip()   # normalize

            if not clean_input:           # skip empty input
                continue

            # ── EXIT STRATEGY: Kill Command ───────────────────
            if clean_input in EXIT_COMMANDS:
                print(f"\n{Color.GRAY}  [ while loop: BREAK ]{Color.RESET}")
                print(f"{Color.TEAL}DecoBot:{Color.RESET} Goodbye! Thanks for chatting. Session ended.\n")
                break                     # clean break -- loop terminates

            # ── PHASE 2: PROCESS (Dictionary Lookup O(1)) ────
            simulate_typing()
            reply = get_response(clean_input)

            # ── PHASE 3: OUTPUT ───────────────────────────────
            print(f"{Color.TEAL}DecoBot:{Color.RESET} {reply}\n")
            msg_count += 1

        except KeyboardInterrupt:
            print(f"\n\n{Color.YELLOW}  [ KeyboardInterrupt -- loop terminated ]{Color.RESET}")
            print(f"{Color.TEAL}DecoBot:{Color.RESET} Forced exit. Goodbye!\n")
            break

    print(f"{Color.GRAY}  [ Session ended | {msg_count} messages exchanged ]{Color.RESET}\n")


# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    chatbot()