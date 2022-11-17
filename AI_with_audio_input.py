#print loading since it takes so long to load :(
print("Loading whisper model...")

#import necessary dependancies
import whisper
from googletrans import Translator
import openai
from api_key import api_data

#define translator and load whisper model
translator = Translator()
model = whisper.load_model("small")			

#get open AI key and define coompletion
openai.api_key=api_data
completion=openai.Completion()

#define function to transcribe audio
def transcribe_and_translate(audio_in):
	result = model.transcribe(audio_in)
	if result["language"] != "en":
		lang = result["language"]
		translate_me = str(result["text"])
		translations = translator.translate(translate_me, src=lang)
		print("Origional language: %s" %lang)
		return(translations.text)
	else:
		return(result["text"])

#define funcrion for AI reply to text
def Reply(question):
	prompt=f'Josh: {question}\nOpenAI:'
	response=completion.create(
		prompt=prompt,
		engine="text-davinci-002",
		max_tokens=300,
		top_p=1,
		presence_penalty=0.6)
	answer=response.choices[0].text.strip()
	return answer

#loops asking for audio input for AI
while True:
	audio_or_text = input("Do you want to enter a prompt for OpenAI by (a) text or (b) audio?\n")

	if audio_or_text == "a":
		while True:
			inp = input("Enter prompt for OpenAI ('q' to break):")
			if inp == "q":
				break
			ans = Reply(inp)
			print(f'OpenAI: {ans}')

	if audio_or_text == "b":
		while True:
			audio = input("Enter path for audio file to transcribe and input to AI ('q' to break)\n(non-English audio will be automatically detected and translated to English)\n:")
			if audio == "q":
				break
			text_from_audio = transcribe_and_translate(audio)
			ans = Reply(text_from_audio)
			print(f'Input: {text_from_audio}')
			print(f'OpenAI: {ans}')

	if audio_or_text not in ("a", "b", "q"):
		print("Please enter 'a' or 'b' or ('q' to quit)")

	elif audio_or_text == "q":
		exit()
