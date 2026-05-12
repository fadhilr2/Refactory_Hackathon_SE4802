import google.generativeai as genai

genai.configure(api_key="AIzaSyA5lpzzghR4j0V2l1Uzu_sXjbC40vo3W1M")

# Use the latest stable Flash-Lite model
model = genai.GenerativeModel('gemini-3.1-flash-lite')

response = model.generate_content("")
print(response.text)