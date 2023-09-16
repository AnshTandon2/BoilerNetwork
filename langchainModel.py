from langchain import OpenAI, SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
import sqlite3
from config import *

conn = sqlite3.connect("opportunityDatabase.db")
cursor = conn.cursor()

#defining LLM
llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name='gpt-3.5-turbo')

#defining database
pg_uri = "sqlite:///opportunityDatabase.db"
db = SQLDatabase.from_uri(pg_uri)

#prompt
PROMPT = """ 
Write a descriptive email to a researcher about why you as an individual would be interested in working with them and learning from their experience. Explain why you think their project is interesting in the context of the problem description and your own background.
"""

db_chain = SQLDatabaseChain(llm=llm, database=db, verbose=True, top_k=3)

#specialized query
question = "write an email about why you would like to work with this professor"

# use db_chain.run(question) instead if you don't have a prompt
db_chain.run(PROMPT.format(question=question))