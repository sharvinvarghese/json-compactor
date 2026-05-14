# 🗜️ json-compactor

> **Compact JSON → Save Tokens → Cut LLM Costs**

A lightweight Python utility that converts pretty-printed or whitespace-heavy JSON into compact, single-line JSON — removing all unnecessary spaces, newlines, and indentation.

**Perfect for:** cutting token usage before sending JSON to LLMs like GPT-4, Claude, or Gemini. Typical savings: **20–40% fewer tokens** depending on indentation depth.

---

## 🚀 Why This Exists

When you send JSON to an LLM, every whitespace character counts as tokens:

```json
// Pretty JSON — 143 bytes, ~36 tokens
{
  "name": "Sharvin",
  "role": "developer",
  "skills": [
    "Python",
    "ML",
    "Data"
  ]
}
```

```json
// Compact JSON — 58 bytes, ~15 tokens ✅
{"name":"Sharvin","role":"developer","skills":["Python","ML","Data"]}
```

**That's a ~58% reduction on this example alone.**

---

## 📦 Installation

```bash
git clone https://github.com/sharvinvarghese/json-compactor.git
cd json-compactor
pip install -r requirements.txt
```

No external dependencies — uses Python's built-in `json` module only. Requires **Python 3.7+**.

---

## 🛠️ Usage

### 1. Single File

```bash
python json_compactor.py input.json
```

Compact and print to stdout.

```bash
python json_compactor.py input.json -o output.json
```

Save to a new file.

```bash
python json_compactor.py input.json --sort-keys
```

Also sort keys alphabetically (great for deterministic diffs).

```bash
python json_compactor.py input.json --no-stats
```

Suppress stats, just output the compacted JSON.

---

### 2. Pipe / Stdin

```bash
cat big_response.json | python json_compactor.py
```

Works seamlessly with Unix pipes.

```bash
curl https://api.example.com/data | python json_compactor.py
```

Compact an API response on the fly before processing.

---

### 3. Batch Folder

```bash
python batch_compact.py ./my_data_folder/
```

Compacts every `.json` file in the folder and saves results to `./my_data_folder/compacted/`.

```bash
python batch_compact.py ./datasets/ -o ./datasets/compact/ --sort-keys
```

Custom output folder + sorted keys.

---

### 4. Use in Python

```python
from json_compactor import compact_json, process_file

# Compact a string
raw = '{ "a": 1, "b": [1, 2, 3] }'
print(compact_json(raw))
# → {"a":1,"b":[1,2,3]}

# Compact a file
process_file("input.json", "output.json", sort_keys=True)
```

---

## 📊 Token Savings — Where It Helps Most

| Use Case | Typical Savings |
|---|---|
| LLM system prompts with embedded JSON config | 25–35% |
| API response caching before RAG indexing | 20–40% |
| JSON datasets sent to fine-tuning pipelines | 30–50% |
| Tool call outputs passed back into context | 20–30% |
| JSON schema definitions in prompts | 25–45% |
| Log files and audit trails | 35–55% |

> **Rule of thumb:** 1 token ≈ 4 characters. Every 4 bytes saved ≈ 1 fewer token.

---

## 🔢 CLI Reference

```
usage: json_compactor.py [-h] [-o OUTPUT] [--sort-keys] [--no-stats] [input]

positional arguments:
  input           Input JSON file (or omit to read from stdin)

optional arguments:
  -o, --output    Output file path
  --sort-keys     Sort JSON keys alphabetically
  --no-stats      Suppress size/token stats output
```

```
usage: batch_compact.py [-h] [-o OUTPUT] [--sort-keys] folder

positional arguments:
  folder          Folder containing .json files

optional arguments:
  -o, --output    Output folder (default: <folder>/compacted)
  --sort-keys     Sort JSON keys
```

---

## 🧪 Example Output

```
✅ Saved to: output.json
📦 Original : 4,320 bytes
📦 Compacted: 2,890 bytes
💾 Saved    : 1,430 bytes (33.1%)
🪙 Estimated tokens saved: ~357
```

---

## 🤖 LLM Integration Tips

1. **Before sending to API:** Run your JSON through `compact_json()` before embedding in prompts
2. **Cached API responses:** Compact once, store compact version — never re-expand
3. **RAG pipelines:** Store compact JSON in vector DBs to reduce context window usage
4. **Agentic tool calls:** Compact tool outputs before returning them to the LLM context
5. **Fine-tuning datasets:** Smaller training examples = faster training + lower cost

---

## 📁 Project Structure

```
json-compactor/
├── json_compactor.py    # Core single-file compactor
├── batch_compact.py     # Batch processor for folders
├── requirements.txt     # (empty — stdlib only)
├── README.md
└── examples/
    ├── sample_pretty.json
    └── sample_compact.json
```

---

## 📜 License

MIT License — free to use in personal and commercial projects.

---

## 🙋 Author

**Sharvin Varghese** — [@sharvinvarghese](https://github.com/sharvinvarghese)

> Built because every token counts. 🪙
