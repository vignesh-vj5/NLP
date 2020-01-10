# NLP
Natural Language Processing is a discipline that focuses on the interaction between data-science and human language, and is scaling to lots of industries in the modern era. 


If you have Python ready on your PC and prefers to skip the description, just install the requirements.txt by running the command : `pip install -r requirements.txt`



##Prerequisites to make this work.
1. Install Python on your PC.
      - I suggest you to install Anaconda Navigator on your PC since we will dive-in later to wire-up neural network models             where-as working with jupyter notebook for evaluating the network-model performance will be like bread-and-butter from         my point of view. Also there won't be any dependency issues which might feel annoying when trying to mess with the             codes.
2. Open up the terminal and hit the following:
      
      * `pip install spacy`
                * Spacy is one of the popular NLP libraries used to handle various text analysis tasks such as tokenization,    sentiment analysis,named entity recognition,text summarization,etc.
                In-order to utilize the above mentioned tasks, we should download a language model, here we use english `en_core_web_sm`. Head-over to the terminal and run  `python -m spacy download en`.
                
      * `pip install textblob`
                We utilize textblob to analyze the sentiment from the input that we type-in.  
                
      * `pip install streamlit`
                * Streamlit is an open-source Python library that makes it easy to build beautiful apps for machine learning.
                  Once you install just locate to the project directory and run `streamlit <<filename.py>>` via terminal. Local URL and Network URL will be generated. Copy either of the address and run it via your desired browser.

      * **N.B.** For composing the streamlit script, I employed Sublime Text for editing convenience. You can use your favourite one. Also Usage of Anaconda Navigator ensures that you don't face any dependency crashes since installations that you make via pip will be in the conda environment. To make sure you are on the conda environment just look-out for **(base)** in the terminal before the username. If it is not there, hit `conda activate` if you are using Anaconda prompt.
