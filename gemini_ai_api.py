import google.generativeai as genai

def get_gemini_response(question) :
    genai.configure(api_key="YOUR_API_KEY")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(question)
    return response.text


if __name__ == "__main__" :
    question = input("ENTER THE QUESTION: ")
    data_value = get_gemini_response(question)
    print(data_value)
