# 🎙️ Voice-Based Government Scheme Agent (Telugu)

## 📌 Project Overview

This project implements a **voice-first, agentic AI system** that helps users **identify and apply for government and public welfare schemes** using **spoken Telugu**.

The system goes beyond a simple chatbot by demonstrating:
- reasoning
- planning
- tool usage
- conversation memory
- failure handling  

All interactions operate **end-to-end in a native Indian language (Telugu)**.

---

## 🎯 What the Agent Does

Users can speak naturally in Telugu, and the agent will:

- 🎧 Understand speech using **Speech-to-Text (STT)**
- 🧾 Collect eligibility information
- 🧠 Determine eligible schemes using **rule-based reasoning**
- 📚 Retrieve scheme details using **RAG (FAISS)**
- 📝 Guide users through **application steps**
- 🔊 Respond back in **Telugu speech (TTS)**

---

## 📍 Problem Statement Alignment

This project directly satisfies the mandatory scenario:

> **Build a Voice-Based Native Language Service Agent that helps users identify and apply for government or public welfare schemes.**

### ✔ Key Guarantees

- **Voice-first**  
  Voice input and voice output are mandatory and fully implemented.

- **Native Language**  
  Telugu is used across the entire pipeline:STT → Agent → RAG → TTS

- **Agentic Workflow**  
Planner–Executor–Evaluator loop implemented using a state machine.

- **Tool Usage**  
- Eligibility Engine  
- Retrieval-Augmented Generation (FAISS)

- **Memory**  
Conversation state maintained across turns.

- **Failure Handling**  
Handles invalid inputs, missing data, retries, and contradictions.

---

## 🏗️ System Architecture

### 🔹 High-Level Architecture Diagram
![WhatsApp Image 2025-12-19 at 11 32 33 PM](https://github.com/user-attachments/assets/c4ca48cf-34d7-4964-928e-005e013a2e14)





## 🔁 Agent Lifecycle & Decision Flow

### 1️⃣ Planner
The planner decides:
- What information is missing
- Whether to:
  - ask eligibility questions
  - run the eligibility engine
  - call the RAG tool
  - loop or exit

---

### 2️⃣ Executor
The executor performs actions using tools:

- **Eligibility Engine**
  - Rule-based evaluation
  - Uses user profile and scheme constraints
  - Deterministic (no hallucination)

- **RAG Tool (FAISS)**
  - Retrieves Telugu scheme knowledge
  - Covers benefits, documents, and application steps

---

### 3️⃣ Evaluator
The evaluator:
- Validates user inputs
- Handles contradictions (e.g., invalid gender, wrong scheme number)
- Requests clarification when needed
- Decides whether to continue or terminate

This loop continues until the user exits.

---

## 🧠 Memory Design

The agent maintains **conversation memory** using an in-memory state object:
- Stores eligibility answers across turns  
- Prevents re-asking already answered questions  
- Ensures consistent reasoning throughout the conversation  
- Supports exploration of multiple schemes in a single session  

---

## 🧰 Tools Used

### 🛠️ Tool 1: Eligibility Engine

A **rule-based, deterministic eligibility engine** used to determine scheme eligibility.

**Key characteristics:**
- No LLM hallucination risk  
- Fully explainable and deterministic  

**Checks conditions such as:**
- Age  
- Occupation  
- Income  
- BPL status  
- Marital status  
- Pregnancy status  

---

### 🛠️ Tool 2: RAG (Retrieval-Augmented Generation)

Used to retrieve scheme-related information after eligibility is determined.

**Key components:**
- Telugu government scheme knowledge corpus  
- Vectorized using multilingual sentence embeddings  
- FAISS used as the vector store  
- Agent-controlled retrieval (scheme-level constraint to avoid cross-scheme errors)  

---


---

## 🔊 Voice Pipeline

### Speech-to-Text (STT)
- **Model:** `ai4bharat/indic-seamless`  
- **Input:** Telugu speech  
- **Output:** Telugu text  

### Text-to-Speech (TTS)
- **Model:** `ai4bharat/indic-parler-tts`  
- **Input:** Telugu text  
- **Output:** Natural Telugu speech  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone <your-github-repo-url>
cd voice-agent

⚙️ Setup Instructions
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate the environment:

Linux / macOS

source venv/bin/activate


Windows

venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If Torch fails on Windows:

pip install torch --index-url https://download.pytorch.org/whl/cpu

4️⃣ Run the Agent
python main.py ```

🗣️ Example Voice Interaction
User (Telugu voice)

“నాకు ఏ పథకం అర్హత ఉందో చెప్పండి”

Agent Behavior

Asks eligibility questions

Determines eligible schemes

Explains scheme details

Guides application steps

Responds via Telugu speech
❌ Failure Handling Examples
Scenario	Agent Behavior
Invalid input	Asks user to retry
Missing information	Requests clarification
Wrong scheme number	Re-prompts
No eligible schemes	Graceful explanation
STT failure	Asks user to speak again
📊 Evaluation Artifacts

The repository supports:

✅ Successful interactions

✅ Failed interactions

✅ Edge cases (invalid inputs, contradictions)

🏁 Conclusion

This project demonstrates a real-world, production-style voice-based agent built for public service accessibility in native Indian languages.

It showcases:

Agentic reasoning

Tool orchestration

Retrieval systems (RAG + FAISS)

Voice AI integration (STT + TTS)

Fully aligned with the assignment’s goals.

🙏 Acknowledgements

AI4Bharat — IndicSeamless, IndicParlerTTS

Hugging Face Transformers
