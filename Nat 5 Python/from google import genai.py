from google import genai
from PIL import Image
from google.genai import types
import os
import random

"""
Run the following command in the terminal:

pip install -q -U google-genai

Documentation:
https://ai.google.dev/gemini-api/docs

Generate your own API keys:
https://aistudio.google.com/app/apikey
"""

api_keys = ["AIzaSyABU4DguSbpessbqfV0AEjMFSynKjTWSAQ", "AIzaSyCmmsYKqIHjGdGiy8zrX2XzfRIuN_EENxk",
            "AIzaSyD9diW5vN1kXSLaQtuVgyQ_s6yPgHj__lw", "AIzaSyBE5LdVJ6lyFY5f6mys8Et5nDL3P8V_ZjU",
            "AIzaSyAQ2_hGDAHzXaUh22He_BgIFljdmbcEWPg", "AIzaSyCJl67jhLe8LOY9qgV11NhHW5FkPlnuCsU", 
            "AIzaSyCpeLShX5eK7JBZ3Pr7musyAeI4Oecp-ZY", "AIzaSyDrDGXP3nEPzUtwTQav6KrXSf5tamrsNGc",
            "AIzaSyAY5zG1jhLDR60u3NIcQpt2AIJyU7UMuTE", "AIzaSyC6zJQ4mXYh1fApVw8lcf-8iLPqlTCvbSQ"
            ]
api_key = api_keys[random.randint(0, len(api_keys))]

class GeminiAI:
    #This class handles the Text generation segment of the Gemini documentation
    def __init__(self, key):
        #Declaring and initialising AI variables
        self.client = genai.Client(api_key=key)
        self.response = None
        self.contents = None
        self.systemInstruction = None
        self.maxOutputTokens = 500
        self.temperature = 0.1
        self.chat = None
        self.configs = types.GenerateContentConfig(
            systemInstruction=self.systemInstruction,
            maxOutputTokens=self.maxOutputTokens,
            temperature=self.temperature
        )
        
    def updateKey(self, key):
        #Updates the key
        self.client = genai.Client(api_key=key)
        
    def AiResponse(self):
        #Gets a one time response from Gemini
        try:
            if self.contents:
                self.response = self.client.models.generate_content(
                    model="gemini-2.0-flash", contents=self.contents, config=self.configs
                )
        except Exception as e:
            print(f"There was an error: {str(e)}")
            
    def startChat(self):
        #Initiatalises a chat 
        self.chat = self.client.chats.create(model="gemini-2.0-flash", config=self.configs)
        
    def sendChatMessage(self, message):
        #Sends a chat message
        if self.chat:
            self.response = self.chat.send_message(message)
        
    def chatHistory(self):
        #returns the chat history
        if self.chat:
            return self.chat.get_history()
    
    def displayChatHistory(self):
        #Displays the Chat history
        if self.chat:
            for message in self.chat.get_history():
                print(f'role - {message.role}',end=": ")
                print(message.parts[0].text)
            
    def updateTemperature(self, newTemperature):
        #Updates the temperature
        #"temperature" is a parameter that controls the randomness and creativity of the model's output
        if newTemperature > 0.0 and newTemperature < 2.0:
            self.temperature = newTemperature
            self.updateConfig()
        
    def updateMaxOutputTokens(self, newMaxOutputTokens):
        #the maximum number of tokens that an AI model can produce as output in a single response
        if newMaxOutputTokens > 0:
            self.maxOutputTokens = newMaxOutputTokens
            self.updateConfig()
    
    def updateSystemInstruction(self, newSystemInstruction):
        #Updates the role (Character)
        self.systemInstruction = newSystemInstruction
        self.updateConfig()
        
    def updateConfig(self):
        #Updates the config when changed
        self.configs = types.GenerateContentConfig(
            systemInstruction=self.systemInstruction,
            maxOutputTokens=self.maxOutputTokens,
            temperature=self.temperature
        )
            
    def updateContents(self, newContents):
        #Updates the Contents of the message (Prompt)
        self.contents = [newContents]
        
    def openImage(self, Link=""):
        #Returns an Image Open Link
        #To get a response contents must be set to [self.openImage(Link), "Prompt"]
        # i.e. myAI.updateContents([myAI.openImage("Image.png"), "What is this image?"])
        if os.path.isfile(Link):
            return Image.open(Link)
        
    def getResponse(self):
        #returns a full response all at once
        if self.response:
            return self.response.text
        
    def displayResponse(self):
        #Displays a full response all at once
        if self.response:
            print(self.response.text)
        
    def displayChunkResponse(self):
        #displays the response as it arrives
        if self.response:
            for chunk in self.response:
                print(chunk.text, end="")
        
#Object Declaration
myAI = GeminiAI(api_key)

#Getting a basic response from gemini
myAI.updateContents("In a short sentence, What is an AI?")
myAI.AiResponse()
myAI.displayResponse()


"""
#Getting a basic response from gemini that displays as it comes in
myAI.updateContents("What is an AI?")
myAI.AiResponse()
myAI.displayChunkResponse()

"""


"""
#Getting gemini to respond to an image
myAI.updateContents([myAI.openImage("link_to_Png"), "What is this image?"])
myAI.AiResponse()
myAI.displayResponse()

"""

"""
#Getting gemini to play as a character
myAI.updateSystemInstruction("You are a cat")
myAI.updateContents("What are you?")
myAI.AiResponse()
myAI.displayResponse()
"""

"""
#Getting gemini to remember a conversation by initialising a conversation
myAI.startChat()
myAI.sendChatMessage("Hi")
myAI.displayResponse()
myAI.sendChatMessage("How are you?")
myAI.displayResponse()
"""

"""
#Getting Gemini to play as a character during a conversation
myAI.updateSystemInstruction("You are a cat")
myAI.startChat()
myAI.sendChatMessage("Hi")
myAI.displayResponse()
myAI.sendChatMessage("How are you?")
myAI.displayResponse()
"""