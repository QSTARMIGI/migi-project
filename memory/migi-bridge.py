import os

# This is the "Dispatcher" for the Migi Machine
def init_migi():
    print("💠 MIGI BRIDGE ONLINE 💠")
    print("Stitching local engine with OpenAI history...")
    
    # Check if the memory folder exists
    if os.path.exists("./memory"):
        print("[SUCCESS] Memory vault located.")
    else:
        print("[ERROR] Memory vault not found. Check file path.")

if __name__ == "__main__":
    init_migi()