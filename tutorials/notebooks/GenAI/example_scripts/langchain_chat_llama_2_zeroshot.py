from langchain.retrievers import PubMedRetriever
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
#from langchain import SagemakerEndpoint
from langchain.llms.sagemaker_endpoint import LLMContentHandler
import sys
import json
import os
from langchain.llms import SagemakerEndpoint


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

MAX_HISTORY_LENGTH = 1

def build_chain():
  region = os.environ["AWS_REGION"]
  #kendra_index_id = os.environ["KENDRA_INDEX_ID"]
  endpoint_name = os.environ["LLAMA_2_ENDPOINT"]

  class ContentHandler(LLMContentHandler):
      content_type = "application/json"
      accepts = "application/json"

      def transform_input(self, prompt: str, model_kwargs: dict) -> bytes:
          input_str = json.dumps({"inputs": 
                                  [[
                                    #{"role": "system", "content": ""},
                                    {"role": "user", "content": prompt},
                                  ]],
                                  **model_kwargs
                                  })
          #print(input_str)
          
          return input_str.encode('utf-8')
      
      def transform_output(self, output: bytes) -> str:
          response_json = json.loads(output.read().decode("utf-8"))
          
          return response_json[0]['generation']['content']

  content_handler = ContentHandler()

  llm=SagemakerEndpoint(
          endpoint_name=endpoint_name, 
          region_name=region, 
          model_kwargs={"parameters": {"max_new_tokens": 1000, "top_p": 0.9,"temperature":0.6}},
          endpoint_kwargs={"CustomAttributes":"accept_eula=true"},
          content_handler=content_handler,
      )
      
  #retriever = AmazonKendraRetriever(index_id=kendra_index_id,region_name=region)
  retriever= PubMedRetriever()
    
  prompt_template = """
  Ignore everything before.
  
  Instruction:
  I want you to act as a research paper summarizer. I will provide you with a research paper on a specific topic in English, and you will create a summary. The summary should be concise and should accurately and objectively communicate the takeaway of the paper. You should not include any personal opinions or interpretations in your summary, but rather focus on objectively presenting the information from the paper. Your summary should be written in your own words and ensure that your summary is clear, concise, and accurately reflects the content of the original paper.
  
  First, provide a concise summary then provide the sources.
  
  {question} Answer "don't know" if not present in the document. 
  {context}
  Solution:"""
  PROMPT = PromptTemplate(
      template=prompt_template, input_variables=["context", "question"],
  )

  condense_qa_template = """
  Chat History:
  {chat_history}
  Here is a new question for you: {question}
  Standalone question:"""
  standalone_question_prompt = PromptTemplate.from_template(condense_qa_template)

  qa = ConversationalRetrievalChain.from_llm(
        llm=llm, 
        retriever=retriever, 
        condense_question_prompt=standalone_question_prompt, 
        return_source_documents=True, 
        combine_docs_chain_kwargs={"prompt":PROMPT},
        )
  return qa

def run_chain(chain, prompt: str, history=[]):
   print(prompt)
   return chain({"question": prompt, "chat_history": history})

if __name__ == "__main__":
  chat_history = []
  qa = build_chain()
  print(bcolors.OKBLUE + "Hello! How can I help you?" + bcolors.ENDC)
  print(bcolors.OKCYAN + "Ask a question, start a New search: or CTRL-D to exit." + bcolors.ENDC)
  print(">", end=" ", flush=True)
  for query in sys.stdin:
    if (query.strip().lower().startswith("new search:")):
      query = query.strip().lower().replace("new search:","")
      chat_history = []
    elif (len(chat_history) == MAX_HISTORY_LENGTH):
      chat_history.pop(0)
    result = run_chain(qa, query, chat_history)
    chat_history.append((query, result["answer"]))
    print(bcolors.OKGREEN + result['answer'] + bcolors.ENDC)
    print(bcolors.ENDC)
    print(bcolors.OKCYAN + "Ask a question, start a New search: or CTRL-D to exit." + bcolors.ENDC)
    print(">", end=" ", flush=True)
  print(bcolors.OKBLUE + "Bye" + bcolors.ENDC)
