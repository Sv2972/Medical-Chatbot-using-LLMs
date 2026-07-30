import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
try:
    # This configures the library with your key from the environment
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    print("Successfully configured API key.")
    print("Checking for available models...")

    # List the models your key has access to
    model_found = False
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f" - {m.name}")
            if "gemini-pro" in m.name:
                model_found = True

    if model_found:
        print("\nSuccess! Your API key is working and has access to Gemini models.")
    else:
        print("\nWarning: Your API key is valid but may not have access to Gemini-Pro.")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("This could mean your API key is invalid or not set correctly.")