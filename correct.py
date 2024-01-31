# Here you should enter the api key which you've purchased it from openAI web site, Your rest of the code is correct 
import openai #Import openai module from python index packaging manager
import gradio #Import gradio module from python index packaging manager

openai.api_key = "####" #Here you should enter the api key which you've purchased it from openAI web site

messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}] 

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Real Estate Pro")

demo.launch(share=True)
