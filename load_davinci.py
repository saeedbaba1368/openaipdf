def load_davinci(question,temperature,max_tokens):
    from langchain.llms import  OpenAI
    llm= OpenAI(model_name="text-davinci-003",temperature=temperature,max_tokens=max_tokens)
    llm_question=llm(question)
    llm_token=llm.get_num_tokens(question)
    return llm_question,llm_token