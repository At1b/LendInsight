import os
import gdown

MODEL_PATH = "models/random_forest_model.pkl"

FILE_ID = "1qVkNDyGijI1LjkVEfqCmB_MXyD52DjcF"

URL = f"https://drive.google.com/uc?id={FILE_ID}"

def ensure_model():
    os.makedirs("models", exist_ok=True)

    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        gdown.download(URL, MODEL_PATH, quiet=False)