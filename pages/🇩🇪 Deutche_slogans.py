import os 
import langchain
import streamlit as st 
import time
import re

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chains import LLMChain

apikey = os.getenv('OPENAI_API_KEY')
  
#App framework

st.sidebar.success('Select a page above!')

st.title('Coolblue slogan generator📝')
st.markdown("""Willkommen beim Coolblue Slogan-Generator! Hier können Sie Slogans im Coolblue-Stil für praktisch alles und jedes erstellen. Legen Sie los, produzieren Sie und beeindrucken Sie 🤠. """ )
object = st.text_input(' **Geben Sie das Objekt ein, für das Sie einen Slogan möchten.** ')

#Chatmodel
chat_model= ChatOpenAI(temperature=0.7, model="gpt-4")

#Prompt template
system_message_prompt = SystemMessagePromptTemplate.from_template("Sie sind ein kreativer Slogan-Schreiber für Coolblue. Coolblue verwendet Wortspiele, um Objekte oder Dinge humorvoll in einem Slogan zu beschreiben. Sie nutzen den Humor von Coolblue, um anderen beim Erstellen von Slogans zu helfen.")
slogan_examples = "\nGRATIS // Du Glückspilz. ;\nKASSENRABATT // Schnäppchenatmung. ;\nVORBESTELLUNG // Appetitmacher. ;\nEINBAUSERVICE // Anschließend alles in Ordnung. ;\nCOOLBLUE-GUTHABEN // Digitales Sparschwein. ;\nDEINE E-MAILADRESSE // Einzigartig wie du. ;\nABHOLUNG IM STORE // Jeder Schritt hält fit. ;\nGELIEFERT // Schneller als du denkst. ;\nLIEFERUNG // Ich weiß, wo dein Haus wohnt. ;\nBEI DEN NACHBARN // Austausch gegen Kekse. ;\nLIEFERTERMIN // So vorhersehbar. ;\nSPARLADEN // Da sparst du Watt. ;\nGESCHENKGUTSCHEIN // Lizenz zum Kaufen. ;\nRECHNUNG // Geht auf dich. ;\nGESCHICHTE // Was bisher geschah. ;\nSOLARMODULE // Hat Watt. ;\nLAGER // Prost. ;\nTROCKNEN // Mehr als heiße Luft. ;\nGAMING // Fingergymnastik. ;\nWEIHNACHTSGESCHENKE // Diesmal keine Socken. ;\nKUNDE // König. ;\nBEWERTUNGEN // Sterne gucken. ;\nDECKE // Wollfühlfaktor. ;\nRUHEZONE // Chill mal. ;\nSOCKEN // Tschüss kalte Füße. ;\nCYBER MONDAY // Lass es klicken. ;\nZWEITE CHANCE // Liebe auf den zweiten Blick. ;\nDEIN ALTGERÄT // Tschüssikostnie. ;\nSPÜLMASCHINENABO // Glanzleistung. ;\nAUGMENTED REALITY // Ich sehe was, was du nicht siehst. ;\nBABYPHONE // Hör mal, wer da heult. ;\nGRILLS // Dreh mal den Spieß um. ;\nSTANDMIXER // Zum Durchdrehen. ;\nINDUSTRIESTAUBSAUGER // Anti-Staub-AG. ;\nHERDE // Feuer und Flamme. ;\nGAMING-MÄUSE // Wollen nur spielen. ;\nHOCHDRUCKREINIGER // Der Sprühling ist da. ;\nLADESÄULEN // Volt tanken. ;\nMOTHERBOARDS // Plattenbau. ;\nPOWERBANKS // Reservesaft. ;\nRUCKSÄCKE // Gut zu Schultern. ;\nSPARSAME WASCHMASCHINEN // Da bleibt Watt übrig. ;\nUPGRADE KIT // Spiel, Bausatz und Sieg. ;\nBERATUNG // Mit Rat zur Tat. ;"
human_message_prompt = HumanMessagePromptTemplate.from_template("Zwischen den dreifachen Backticks ``` finden Sie Beispiele für ein Objekt mit seinem entsprechenden Coolblue-Slogan. Stellen Sie sicher, dass Sie einen neuen Slogan erstellen, der zum Objekt passt und im humorvollen Stil der Beispiele gehalten ist. Das Format der Beispiele ist Objekt // Slogan und sie werden durch ; getrennt\n\n```{}```\n\nErstellen Sie nun drei verschiedene Slogans mit einem Coolblue-Wortspiel für {} ##format Stellen Sie sicher, dass jeder Slogan wie das Beispiel aussieht und setzen Sie ein ';' zwischen den Slogans.".format(slogan_examples, object))
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

#LLM Chain
slogan_chain = LLMChain(llm=chat_model, prompt=chat_prompt, verbose = True)

if st.button('Beginne zu schreiben!'):
    try:
        if object:
            response = slogan_chain.run({"object": object})

            slogans = re.split(r'\. |\; |; ', response)
            for slogan in slogans:
                if slogan:  
                    st.write(slogan.strip())  

    except Exception as e:
        st.error(f"an error occurred:{e}")

st.markdown("""
---
Möglich gemacht durch Jesse Kuipers | jesse.kuipers@coolblue.nl | https://www.linkedin.com/in/jessekuipers/

Version: 2.0.0
""")
