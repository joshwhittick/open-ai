import openai
from api_key import api_data

openai.api_key=api_data

completion=openai.Completion()

def Reply(question):
	prompt=f'Josh: {question}\n Jarvis'
	response=completion.create(prompt=prompt, engine="text-davinci-002", stop=['\Josh'], max_tokens=300)
	answer=response.choices[0].text.strip()
	return answer


ans = Reply(input("Enter promt for OpenAI:" ))

print(ans)
