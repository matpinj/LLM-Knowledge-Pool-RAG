# This script needs a llama-parse key setup in the keys.py script to run.
from llama_parse import LlamaParse
import os
from config import *

# Parser parameters
parser = LlamaParse(
    api_key="lm-studio", 
    result_type="markdown",  # "markdown" or "text"
    num_workers=4,
    # verbose=True,
    language="en",
)

for document in os.listdir("knowledge_pool"):
    #Iterate through the pdfs
    if document.endswith(".pdf"):
        filepath = os.path.join("knowledge_pool", document)

        # Parse the pdf
        pdf = parser.load_data(filepath)
        # text = pdf[0].text

        # Save to a txt file
        output_filename = os.path.splitext(document)[0]
        output_path = os.path.join("knowledge_pool", f"{output_filename}.txt")
        with open(output_path, 'w', encoding='utf-8') as f:
            for stuff in pdf:
                f.write(stuff.text)
            
        print(f"Finished parsing {document}")

    # juntar todos os documentos a que dei parse num só txt
    
print("Finished parsing all documents")