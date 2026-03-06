# AI Workflow Engine (CLI Version)

🚀 **Project - AI Workflow Engine (CLI)**

A structured, step-based AI workflow runner designed for automation, validation, tracing, and retry logic — **not a chatbot**, but a mini orchestration engine.

---

## 🧠 Overview

This project demonstrates:

- Step-based workflow execution
- Tool abstraction and modular design
- JSON output validation
- Retry logic for robust workflows
- Trace logging for debugging and monitoring
- Clean architecture with a backend-first mindset

This is a showcase of engineering maturity in building maintainable AI systems.

---

## 📁 Project Structure

```bash
ai-workflow-engine/
│
├── main.py # Entry point for CLI workflow execution
├── workflow.py # Workflow orchestration logic
├── config.py # Configuration variables
├── steps/ # Individual workflow step modules
│ ├── data_loader.py
│ ├── anomaly_detector.py
│ ├── llm_step.py
│ ├── validator.py
│ └── logger.py
├── traces/ # Logs and workflow traces
├── sample.csv # Example input data
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md



