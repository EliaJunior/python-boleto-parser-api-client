# 🇧🇷 Python Boleto Parser API (Brazil OCR)

> A High-performance API to extract data from Brazilian Bank Slips (Boletos Bancários) converting PDF to JSON.

[![RapidAPI](https://img.shields.io/badge/RapidAPI-Connect-blue)](https://rapidapi.com/seu-user/api/boleto-parser-brazil)
[![Python](https://img.shields.io/badge/Made%20with-Python-yellow)](https://www.python.org/)

## 🚀 What does it do?

Stop writing complex Regex to parse bank slips. This API detects and extracts:
- **Barcode (Linha Digitável):** Ready for payment integration.
- **Amount (Valor):** Accurate currency parsing.
- **Due Date (Vencimento):** DD/MM/YYYY format.
- **Beneficiary:** Identifies the receiver (Name/CNPJ).

## 🛠️ Usage Example

You can use the native `requests` library in Python.

1. **[Get your Free API Key here](https://rapidapi.com/seu-user/api/boleto-parser-brazil)** (RapidAPI handles the keys).
2. Run the code:

```python
import requests

url = "[https://boleto-parser-brazil.p.rapidapi.com/parse](https://boleto-parser-brazil.p.rapidapi.com/parse)"

payload = { "file": open("my_boleto.pdf", "rb") }
headers = {
    "X-RapidAPI-Key": "YOUR_API_KEY_HERE",
    "X-RapidAPI-Host": "boleto-parser-brazil.p.rapidapi.com"
}

response = requests.post(url, files=payload, headers=headers)

print(response.json())

📦 Response Format
{
  "data": {
    "amount": "270,00",
    "due_date": "21/02/2025",
    "barcode": "07790001161211599379702131089654499990000027000",
    "beneficiary": "53.887.588"
  }
}

⚠️ Requirements
Only Digital PDFs are supported with 100% accuracy.

Scanned images/photos inside PDFs may fail or have lower accuracy.

Maintained by ED Engenharia
