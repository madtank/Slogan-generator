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

st.sidebar.success('Select a page above!')

 #App framework
st.title('Coolblue slogan generator📝')
st.markdown("""Welcome to the Coolblue slogan generator! Here, you can create slogans in the Coolblue style for practically everything and anything. Dive in, produce, and amaze 🤠. """ )
object = st.text_input(' **Enter the object for which you want a slogan.** ')

#Chatmodel
chat_model= ChatOpenAI(temperature=0.7, model="gpt-4")

#Prompt template
system_message_prompt = SystemMessagePromptTemplate.from_template("You are a creative slogan writer for Coolblue. Coolblue uses wordplay to humorously describe objects or things in a slogan. You use Coolblue's humor to help others create slogans.")
slogan_examples = "Cyber Monday // A big deal. ;\nNew // Yay, it's here. ;\nPre-order // Dibs. ;\nWishlist // Someday. ;\nFriends // Honest, direct, open. ;\nPackaging Machine // Automagic. ;\nStorefronts // Making an entrance. ;\nLog In // What a comeback. ;\nHome Office Store // All hands on desk. ;\nDelivery // I know where your house lives. ;\nSavings Questions // Watt. ;\nRubber Duck // Quacks me up. ;\nWater // Eau so fresh. ;\nBlocker // Show stopper. ;\nDelivery // Vantastic. ;\nOur Goals // Real keepers. ;\nWarehouse // Professional boxing. ;\nWaste Management // Bin there. ;\nCoffee Break // Livin la vida mocha. ;\nTools // Hammer time. ;\nPrinting // Inkredible. ;\nReviews // Written in the stars. ;\nCar Radios // Do the DAB. ;\nBarbecues // Grill power. ;\nBlenders // Works smoothie. ;\nComputer Cases // Keeping it together. ;\nDJ Controllers // Track record. ;\nFitbit // Futuwristic. ;\nApple // Not far from the tree. ;\nLawn Mowers // Thanks for shearing. ;\nHair Dryers // Blow me away. ;\nLaptop Sleeves // Zip it. ;\nLaptops // Love at first byte. ;\nHumidifiers // Mist opportunity. ;\nScreen Protectors // Stick around. ;\nSmartwatches // Hour favorites. ;\nLawn Scarifiers // Short cut."
human_message_prompt = HumanMessagePromptTemplate.from_template("Between the triple backticks ``` you will find examples of an object along with its corresponding Coolblue slogan. Make sure you create new slogans that fits the object, in the humorous style and format of the examples. Seperate them by '; ' The format of the examples is Object // Slogan and they are separated by ;\n\n```{}```\n\n. Now come up with three different slogans with a Coolblue wordplay for {}.".format(slogan_examples, object))
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

#LLM CHain
slogan_chain = LLMChain(llm=chat_model, prompt=chat_prompt, verbose = True)

if st.button('Start writing!'):
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
Made possible by Jesse Kuipers | jesse.kuipers@coolblue.nl | https://www.linkedin.com/in/jessekuipers/

Version: 2.0.0
""")
