from pyexpat.errors import messages
import openai
from openai import OpenAI
import argparse

# Initialize the OpenAI API client
client = OpenAI(api_key='sk-proj-W2RoLmxiuJ5wozahkJLxT3BlbkFJotsGS1sMVbRZ0fK9HVhh')

def bold(text):
      bold_start = "\033[1m"
      bold_end = "\033[0m"
      return bold_start + text + bold_end

def blue(text):
      blue_start = "\033[34m"
      blue_end = "\033[0m"
      return blue_start + text + blue_end

def red(text):
      red_start = "\033[31m"
      red_end = "\033[0m"
      return red_start + text + red_end


print(red("HELLO! How may I assist you today? Enter something below:"))

#Personality c
#chatbot
def main():
       parser = argparse.ArgumentParser(description="Simple command line chatbot with GPT-4")
       parser.add_argument("--personality", type=str, help="A brief summary of the chatbot's personality", default="friendly and helpful chatbot")

       args = parser.parse_args()

       initial_prompt=f"You are a conversational chatbot. Your personality is: {args.personality}"
       messages = [{"role": "system", "content": initial_prompt}]

#Maybe add enhance initial_prompts? Like emotions, User Demographics (when being asked for sensitive information)

def detect_sensitive_info(user_input, sensitive_keywords):
      for sensitive_keyword in user_input:
            if sensitive_keyword in user_input.lower():
                  print(red("Warning: You have entered sensitive information. Please make sure it is not too revealing."))
                  break 

messages = []

try:
    while True:    
            user_input = input(blue("You: "))
            messages.append({"role": "user", "content": user_input})

        # Call OpenAI API to get a response
            res = client.chat.completions.create(
            model="gpt-4",
            messages = messages    
            )

            assistant_message = res.choices[0].message.content
            messages.append({"role": "assistant", "content": assistant_message})
            
            #messages.append(res["choices"][0]["message"].to_dict())
            print("Assistant", assistant_message.strip())
            print("MESSAGES", messages)



except KeyboardInterrupt:
        print("\nExiting...")
        
print(res)          

if __name__ == "__main__":
    main()

