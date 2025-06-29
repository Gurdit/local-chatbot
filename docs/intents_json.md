# 📁 What is `intents.json`?

The `intents.json` file is used in rule-based chatbots to define user intents and expected responses. It maps what a user might say (patterns) to how the bot should respond.

---

## 📦 Structure

Each intent contains:
- **tag**: A label identifying the intent (e.g., `greeting`, `thanks`)
- **patterns**: Example user inputs for that intent
- **responses**: Possible bot replies for the intent
- **context** (optional): Manages conversation state

---

## 🧠 Example

```json
{
  "tag": "greeting",
  "patterns": ["Hi", "Hello", "Hey"],
  "responses": ["Hi there!", "Hello! How can I help you?"],
  "context": [""]
}
