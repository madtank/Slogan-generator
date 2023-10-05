#Importing dependencies
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

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.langchain.plus"
os.environ["LANGCHAIN_API_KEY"] = os.environ.get("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "solgan-generator"

apikey = os.getenv('OPENAI_API_KEY')

st.sidebar.success('Select a page above!')

#App framework
st.title('Coolblue slogan generator📝')

st.markdown(""" Welkom bij de Coolblue slogan generator! Hier maak je slogans in de Coolblue stijl voor praktisch alles wat los en vast zit. Probeer, genereer en fascineer 🤠 """ )
object = st.text_input(' **Vul hier het object in waar je een slogan voor wilt** ')

#Chatmodel

chat_model= ChatOpenAI(temperature=0.7, model="gpt-4")

#Prompt template

system_message_prompt = SystemMessagePromptTemplate.from_template("Jij bent een creatieve slogan schrijver van Coolblue. Coolblue gebruikt woordgrappen om objecten of dingen grappig te beschrijven in een slogan. Je gebruikt de humor van Coolblue om andere te helpen met het maken van slogans")
slogan_examples = "cashback // boemeranggeld. ;\ninruilen // wisseltruc. ;\npre-order // dibs. ;\naward // blikvanger. ;\nbevestiging // voelt goed. ;\nbluetooth speakers // meeslepende muziek. ;\nfietscomputers // spaakgebrek ;\nstormparaplu // onweer-staanbaar. ;\ntuinslangen // geen geëmmer. ;\nbetaalwijze // aangekaart. ;\npersoonlijke chat // niet bot. ;\nlaadbak // ik klep even helemaal dicht. ;\nbier // drankjewel. ;\ngrasmaaiers // thuiskapper. ;\nintern geheugen // zit geramd. ;\nijsmachines // moet je hoorn. ;\nairpods // zet de toon. ;\nbarbecues // geef maar een grill. ;\nblenders // drankjes van 't huis. ;\ndrones // in de wolken. ;\nbaardtrimmers // anti-blotebillengezicht. ;\nprinters // druk druk druk. ;\nbouwradio's // openluchtconcert. ;\nbouwstofzuigers // kort van stof. ;\nbridges // langeafstandsrelatie. ;\nbroodbakmachines // deeglijk brood in huis. ;\nbroodroosters // daar toasten we op. ;\nbruiswatermachines // eau zo lekker. ;\nbuiktrainer // blokjesdenken. ;\nbureaus // werkelijk. ;\nfitbit // per seconde wijzer. ;\nflightsticks // krijg er hoogte van. ;\nflosapparaten // wij helpen je kiezen. ;\nfoamrollers // spierritueel. ;\nföhns // gebakken lucht. ;\nfoodprocessors // koekjes rapsen. ;\nfonduesets // om voor te smelten. ;\nfornuizen // kook van jou. ;\nfotografie // een goede klik. ;\nfotografie // neem een kiekje. ;\nfriteuses // bitterballenbubbelbad. ;\nfriteuses // vet gezellig thuis. ;\ngames // alles onder controller. ;\ngrasmaaiers // kortpittige grasmat. ;\ngrastrimmers // alleen de puntjes graag. ;\nhaakse slijpers // meeslijpend. ;\nhaardrogers // ook voor hem. ;\nhakmolens // gabberfeestje."
human_message_prompt = HumanMessagePromptTemplate.from_template("Tussen de triple backticks ``` vind je voorbeelden een object met bijbehorend van Coolblue slogan. Zorg ervoor dat je de nieuwe slogan creëert die past bij het object en in de humoristische stijl is van de voorbeelden. Het format van de voorbeelden is Object // Slogan en worden gescheiden door ;\n\n```{}```\n\n Bedenk nu drie verschillende slogans met Coolblue woordgrap voor {}".format(slogan_examples, object))
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

#LLM CHain

slogan_chain = LLMChain(llm=chat_model, prompt=chat_prompt, verbose = True)

# Show stuff on the screen when there is a prompt 
if st.button('Begin te schrijven!'):
    try:
        if object:
            response = slogan_chain.run({"object": object})
            st.write(response)
    except Exception as e:
        st.error(f"an error occurred:{e}")

st.markdown("""
---
Mede mogelijk gemaakt door Jesse Kuipers | jesse.kuipers@coolblue.nl | https://www.linkedin.com/in/jessekuipers/

Version: 2.0.0
""")
