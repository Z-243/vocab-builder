# 📚 Vocabulary Builder

A Python-based **vocabulary learning game** that quizzes you on words and their definitions.  
It uses **JSON** and **CSV** files to store definitions and track your progress over time.

---

## 🚀 Features
- Reads **`definitions.json`** to get word meanings.
- Keeps track of previously encountered words in **`words_history.csv`**.
- Shows **word + definition** the first time you encounter it.
- Quizzes you on the definition in subsequent encounters.
- Keeps a **score tally** and ends the game when you miss a definition.
- Congratulates you if you complete the entire list.

---

## 🗂 Data File Formats

### **`definitions.json`**
```json
{
  "coruscating": "Sparkling or flashing with brilliance.",
  "ungentle": "Lacking kindness or gentleness.",
  "dulcimer": "A stringed musical instrument.",
}
```

### **`words_history.csv`**
```csv
"waned"
"warder"
"truculent"
"beset"
"waned"
```
> Each row contains a word you have already encountered.

---

## 💻 How It Works
1. **Load data**
   - Import word definitions from `definitions.json`.
   - Import previously encountered words from `words_history.csv`.

2. **Quiz logic**
   - A random or sequential word is selected.
   - If the word is new:
     - Show the definition along with the word.
   - Prompt the user to type the correct definition.
   - If correct:
     - Increment score and add the word to encounter_words set.
   - If incorrect:
     - End the game and display the correct answer.

3. **Game completion**
   - If all words are answered correctly, display a winning message.

---

## 🛠 Dependencies
- Python 3.x
- No external libraries required (uses built-in `json` and `csv` modules).

---

## ▶️ Usage
```bash
python play.py
```
Then follow the on-screen prompts to play.

---

## 📝 Example Gameplay
```
Define: loquacious
loquacious -> tending to talk a great deal
Answer: tending to talk a great deal
Correct!

Define: serendipity
Answer: the occurrence of events by chance in a happy way
Correct!

Congratulations! You have completed the game.
Top Score: 2
```

---

## 📌 Notes
- Ensure `definitions.json` contains all words you want to quiz on.
- If a word in the game is missing from `definitions.json`, it will be skipped.
- `words_history.csv` ensures you don’t get shown definitions for words you’ve already mastered.

