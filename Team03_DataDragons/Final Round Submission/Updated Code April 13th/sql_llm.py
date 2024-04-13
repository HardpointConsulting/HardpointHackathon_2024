from secret import secret_key

from langchain_google_genai import GoogleGenerativeAI
 
llm = GoogleGenerativeAI(model="models/text-bison-001",google_api_key=secret_key, temperature=0.2)

from langchain_community.utilities import SQLDatabase

def sql_to_llm(username, password, host, database, query):
    username = username
    localhost = host
    password = password
    port = 3306
    database = database
    db = SQLDatabase.from_uri(f"mysql+pymysql://{username}:{password}@{localhost}/{database}", sample_rows_in_table_info=3)

    from langchain_experimental.sql import SQLDatabaseChain

    db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
    result = db_chain(query)
    return {
        "query": result['query'], 
        "result": result['result']
    }
# res = sql_to_llm("root", "root", "localhost", "atliq_tshirts", "How many tshirts are there?")
# print(res["query"], res["result"])
