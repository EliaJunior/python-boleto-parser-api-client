import requests
import json
import os

#Configuration
# ---------------------------------------------------------
# 🔑 Get your Free API Key here: 
# https://rapidapi.com/junioroliveira944/api/boleto-parser-brazil
API_KEY = "YOUR_RAPIDAPI_KEY_HERE" 

# API Endpoint
API_HOST = "boleto-parser-brazil.p.rapidapi.com"
URL = f"https://{API_HOST}/parse"

# File to test (Put a real PDF in the same folder)
FILE_NAME = "boleto_sample.pdf"
# ---------------------------------------------------------

def parse_boleto():
    # Check if file exists
    if not os.path.exists(FILE_NAME):
        print(f"❌ Error: The file '{FILE_NAME}' was not found in this folder.")
        print("   -> Please add a valid PDF boleto and rename it, or update the FILE_NAME variable.")
        return

    print(f"🚀 Sending '{FILE_NAME}' to Boleto Parser Brazil...")

    try:
        # Open file in Binary mode
        with open(FILE_NAME, "rb") as pdf_file:
            
            # Payload definition
            payload = {"file": pdf_file}
            
            # Headers with Authentication
            headers = {
                "x-rapidapi-key": API_KEY,
                "x-rapidapi-host": API_HOST
            }

            # Send POST Request
            response = requests.post(URL, files=payload, headers=headers)

            # Handle Response
            if response.status_code == 200:
                print("\n✅ SUCCESS! Data Extracted:")
                data = response.json()
                
                # Pretty Print JSON
                print(json.dumps(data, indent=4, ensure_ascii=False))
                
                # Example of accessing specific fields
                if data.get("success"):
                    amount = data["data"]["amount"]
                    print(f"\n💰 Amount detected: R$ {amount}")
            
            elif response.status_code == 403:
                print("\n❌ Authentication Error (403):")
                print("   -> Did you subscribe to the Free Plan on RapidAPI?")
                print("   -> Check if your API_KEY is correct.")
            
            else:
                print(f"\n❌ Error {response.status_code}:")
                print(response.text)

    except Exception as e:
        print(f"\n❌ Connection Error: {e}")

if __name__ == "__main__":
    parse_boleto()
