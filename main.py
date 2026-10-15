import os
import random
from datetime import datetime

print("Initializing Touchline Studio - Viral Content Agent...")

def check_viral_trends():
    print("Scanning global viral trends and high-engagement topics...")
    viral_topics = [
        "Mind-blowing psychological facts everyone should know",
        "Top productivity hacks used by high achievers",
        "Incredible technology breakthroughs in 2026",
        "Unbelievable science and space mysteries"
    ]
    selected_topic = random.choice(viral_topics)
    return selected_topic

def generate_content(topic):
    print(f"Generating high-retention script and caption for: {topic}...")
    script = f"Fast-paced 30-second script designed for high viewer retention about: {topic}"
    caption = f"Wait until the end! 🤯 What do you think? Let me know in the comments. 👇 #viral #trending #reels #explore"
    return script, caption

def run_agent_workflow():
    print(f"--- Running automated viral Reels workflow at {datetime.now()} ---")
    topic = check_viral_trends()
    script, caption = generate_content(topic)
    
    live_mode = os.environ.get("LIVE_MODE", "false").lower() == "true"
    
    if live_mode:
        print("Live mode is ON: Publishing viral reel to Instagram Graph API...")
    else:
        print("Preview mode is ON: Viral content draft saved locally.")
        os.makedirs("./output/preview", exist_ok=True)
        with open("./output/preview/latest_draft.txt", "w") as f:
            f.write(f"Topic: {topic}\nScript: {script}\nCaption: {caption}")
        print("Draft saved successfully to ./output/preview/latest_draft.txt")

if __name__ == "__main__":
    run_agent_workflow()
