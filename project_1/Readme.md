# 🧠 Nova AI – Rule-Based Customer Support Chatbot

> **DecodeLabs Internship 2026** | Batch 2026 | Project 1

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red.svg)](https://streamlit.io)
[![DecodeLabs](https://img.shields.io/badge/DecodeLabs-Internship-1e293b)](https://decodelabs.tech)

A **production-ready, deterministic AI chatbot** built entirely with Python and Streamlit. Unlike black-box LLMs, this "White Box" AI uses Hash Maps for O(1) lookup speed, making it 100% transparent, traceable, and zero-hallucination.

---

## 📸 Live Demo

![Nexus AI Chatbot Screenshot](screenshot1.png)
![Nexus AI Chatbot Screenshot](screenshot2.png)

*Experience the modern, corporate-style chat interface with quick replies and instant feedback.*

---

## ✨ Advanced Features

| Feature | Description |
| :--- | :--- |
| **🧠 White Box Intelligence** | Every input maps to an explicit output. No mystery, no hallucinations. |
| **🗣 60+ Predefined Intents** | Handles greetings, feelings, tech questions, and DecodeLabs-specific queries. |
| **🧮 Interactive Calculator** | Type `calc 5 + 3` or `sqrt(16)` to get instant math results. |
| **📅 Smart Date & Time** | Tells you the exact time, current date, and the specific weekday (e.g., Wednesday). |
| **💬 Context Memory** | Remembers your previous messages. If you say "I am sad" and then "Why?", it recalls the context. |
| **👍 Customer Feedback Loop** | Thumbs Up/Down buttons on every bot message (Industry-standard for support). |
| **⚡ Quick Reply Chips** | One-click suggestion buttons (Hello, Time, Date, Joke, Calculator) for faster interaction. |
| **🔍 Fuzzy Matching** | Uses `difflib` to correct typos (e.g., "helo" → "Hello"). |
| **🎨 Modern Streamlit UI** | Beautiful, responsive, and mobile-friendly interface out of the box. |

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend Logic** | Python 3.11 (Rule-based, Dictionary Hash Map) |
| **Web Framework** | Streamlit (Fastest way to build data apps) |
| **Matching Engine** | `difflib` (Fuzzy string matching for typo tolerance) |
| **Math Parser** | Python `eval` with restricted globals (Safe calculator) |
| **UI/UX** | Streamlit Chat Components (`st.chat_message`, `st.chat_input`) |

---

## 🚀 How to Run Locally

Follow these simple steps to get the chatbot running on your machine.

**1. Clone the repository (or navigate to the project)**
```bash
cd Decodelabs_internship/project_1