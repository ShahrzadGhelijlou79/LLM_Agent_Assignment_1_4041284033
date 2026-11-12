import argparse
import json
import os
from agent import ReasoningAgent

def main():
    parser = argparse.ArgumentParser(description="LLM Reasoning Agent CLI")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output JSON file")
    args = parser.parse_args()

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"Input file not found: {args.input}")

    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    agent = ReasoningAgent()
    results = []

    # اگر داده‌ها به صورت لیست بودند، هر آیتم را جداگانه بررسی کن، وگرنه خودِ داده‌ها را به صورت لیست تکی در نظر بگیر
    items = data if isinstance(data, list) else [data]

    for item in items:
        problem_id = item.get("id")
        problem_text = item.get("problem")
        
        answer = agent.solve(problem_text)
        
        results.append({
            "id": problem_id,
            "answer": answer
        })

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    main()