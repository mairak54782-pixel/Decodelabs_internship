# ======================================================================
# PROJECT 1: NOVA AI - UPGRADED WITH MULTIPLE JOKES & BETTER MATCHING
# DecodeLabs Internship 2026
# ======================================================================

import streamlit as st
import datetime
import random
import re
import difflib

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Nexus AI | DecodeLabs",
    page_icon="🧠",
    layout="centered"
)

# ---------- AI ENGINE ----------
BOT_NAME = "Nexus"
COMPANY = "DecodeLabs"

# ---- Multiple Jokes (Now 10+ variations!) ----
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐞",
    "What do you call a snake that builds computers? A Viper! 🐍",
    "Why was the developer unhappy? Because his variables were out of scope! 😅",
    "What's a programmer's favorite hangout? The Foo Bar! 🍻",
    "Why do Java developers wear glasses? Because they can't C#! 👓",
    "What is the object-oriented way to become wealthy? Inheritance! 💰",
    "Why did the programmer quit his job? Because he didn't get arrays! 😂",
    "What do you call a programmer from Finland? Nerdic! 🇫🇮",
    "Why do Python programmers have messy hair? Because they don't use combs! (comb = combination)",
    "What's a computer's favorite snack? Microchips! 🍟"
]

# ---- Main Responses ----
RESPONSES = {
    # Greetings
    "hello": f"Hello there! I'm {BOT_NAME}. How can I help you build something legendary?",
    "hi": f"Hi! Ready to dive into AI logic?",
    "hey": f"Hey! Let's make today productive!",
    "how are you": f"I'm running on pure logic, so I'm perfect! How about you?",
    
    # Feelings
    "i am sad": f"Don't worry! Every bug has a fix. Stay strong! 💪",
    "i am happy": f"That's the spirit! Happy coding! 😄",
    "i am tired": f"Take a break, grab some coffee, and come back stronger! ☕",
    
    # Bot Identity
    "who are you": f"I am {BOT_NAME}, a rule-based White Box AI. My logic is 100% transparent.",
    "what is your name": f"My name is {BOT_NAME}. I run on a Hash Map for O(1) lookups!",
    "what can you do": f"I can chat, calculate (calc 5+3), tell time/date, and remember our conversation!",
    
    # Time, Date, Day
    "time": f"🕒 Current time: {datetime.datetime.now().strftime('%I:%M:%S %p')}",
    "date": f"📅 Today's date: {datetime.datetime.now().strftime('%B %d, %Y')}",
    "day": f"📅 Today is {datetime.datetime.now().strftime('%A')}",
    
    # DecodeLabs
    "decodelabs": f"🔥 {COMPANY} - Where AI engineers are made!",
    "internship": f"Welcome to the {COMPANY} Internship! You're building production-ready AI!",
    
    # Thanks & Farewell
    "thanks": f"You're welcome! Don't forget to star this project ⭐",
    "thank you": f"Anytime! Happy to help! 🙌",
    "bye": f"Goodbye! Stay curious and keep coding! 👋",
    "goodbye": f"Farewell! See you tomorrow!",
}

# ---- AI Keywords (For better partial matching) ----
KEYWORDS = {
    "ai": "Artificial Intelligence is the new electricity. We're building the future, one rule at a time! 🧠",
    "machine learning": "ML is cool, but remember: Garbage In, Garbage Out. Clean your data! 📊",
    "python": "Python is the language of AI. Simple, powerful, and loved by developers worldwide! 🐍",
    "algorithm": "An algorithm is a sequence of steps. My core is a Hash Map—O(1) baby! 📈",
    "bug": "Bugs are just unexpected features! Let's debug together. 🐛",
    "code": "Code is poetry. Every 'if' statement is a stanza in the poem of logic. ✍️",
    "data": "Data is the new oil. But unlike oil, data doesn't hurt the planet! 🌍",
    "neural network": "NNs are black boxes. I am a white box. Know the difference! 🧩",
    "internship": f"Welcome to the {COMPANY} Internship. Project 1 is your foundation! 🚀",
}

# ---- Fallback Responses ----
FALLBACKS = [
    "Hmm, I don't understand that. Try 'hello', 'time', or 'joke'.",
    "My dictionary doesn't have that key yet. Feel free to teach me!",
    "Not in my knowledge base. Try asking about 'date' or 'day'.",
    "I'm still learning! Try 'who are you' or 'what can you do'."
]

# ---- Joke Index for multiple jokes ----
if "last_joke_index" not in st.session_state:
    st.session_state.last_joke_index = -1

def get_new_joke():
    """Returns a new joke (different from the last one if possible)"""
    if len(JOKES) <= 1:
        return JOKES[0]
    
    # Try to get a different joke
    available = [i for i in range(len(JOKES)) if i != st.session_state.last_joke_index]
    new_index = random.choice(available)
    st.session_state.last_joke_index = new_index
    return JOKES[new_index]

def get_response(user_input):
    clean = user_input.lower().strip()
    
    # ---- 1. Calculator ----
    if "calc" in clean or any(op in clean for op in ['+', '-', '*', '/']):
        try:
            expr = clean.replace("calc", "").strip()
            if re.match(r'^[\d+\-*/().%]+$', expr):
                result = eval(expr, {"__builtins__": None}, {})
                return f"🧮 Result: {result}"
        except:
            pass
    
    # ---- 2. Joke Variations ----
    if "joke" in clean or "funny" in clean:
        return get_new_joke()
    
    # ---- 3. Exact Match ----
    if clean in RESPONSES:
        return RESPONSES[clean]
    
    # ---- 4. Partial Match with RESPONSES ----
    for key in RESPONSES:
        if key in clean or clean in key:
            return RESPONSES[key]
    
    # ---- 5. Keyword Matching (New!) ----
    for keyword, response in KEYWORDS.items():
        if keyword in clean:
            return response
    
    # ---- 6. Fuzzy Match ----
    close = difflib.get_close_matches(clean, list(RESPONSES.keys()), n=1, cutoff=0.6)
    if close:
        return RESPONSES[close[0]]
    
    # ---- 7. Dynamic Time/Date ----
    if any(word in clean for word in ['time', 'clock']):
        return f"🕒 {datetime.datetime.now().strftime('%I:%M:%S %p')}"
    if any(word in clean for word in ['date', 'today']):
        return f"📅 {datetime.datetime.now().strftime('%B %d, %Y')}"
    if any(word in clean for word in ['day', 'weekday']):
        return f"📅 {datetime.datetime.now().strftime('%A')}"
    
    # ---- 8. Context Memory ----
    if "why" in clean and len(st.session_state.get("context", [])) > 0:
        last_topic = st.session_state.context[-1]
        return f"You asked about '{last_topic}' earlier. What exactly bothers you?"
    
    # ---- 9. Fallback ----
    return random.choice(FALLBACKS)

# ---------- SESSION STATE ----------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"🌟 Welcome to {COMPANY}! I'm {BOT_NAME}. Ask me anything!"}
    ]
if "context" not in st.session_state:
    st.session_state.context = []

# ---------- STREAMLIT UI ----------
st.title("🧠 Nexus AI")
st.caption(f"DecodeLabs Internship 2026 | Project 1")

# Sidebar
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("🔄 Reset Conversation"):
        st.session_state.messages = []
        st.session_state.context = []
        st.session_state.last_joke_index = -1
        st.rerun()
    
    st.divider()
    st.markdown("**💡 Quick Commands**")
    st.code("""
hello
how are you
time
date
joke
another joke
calc 5 + 3
who are you
tell me about ai

    """, language="text")
    
    st.divider()
    st.caption(f"Made with ❤️ for {COMPANY} Batch 2026")

# Display Messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Quick Reply Buttons
col1, col2, col3, col4 = st.columns(4)
if col1.button("👋 Hello"):
    st.session_state._input = "Hello"
if col2.button("🕒 Time"):
    st.session_state._input = "Time"
if col3.button("😂 Joke"):
    st.session_state._input = "Joke"
if col4.button("🧮 calc 5+3"):
    st.session_state._input = "calc 5 + 3"

# Chat Input
if "_input" in st.session_state:
    prompt = st.session_state._input
    del st.session_state._input
else:
    prompt = st.chat_input("Type your message here...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.context.append(prompt)  # Store for memory
    
    # Get bot response
    bot_reply = get_response(prompt)
    
    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    
    st.rerun()