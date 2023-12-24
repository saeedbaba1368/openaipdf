def prompet_template(input_v,temperature):
    from langchain import PromptTemplate
    from langchain.llms import OpenAI
    template = '''You are Anna, an AI bot specialized in booking reservations and customer support..
    Please recommend the 10 best book that {z} recomend .just number book with auther name not more explaination.'''
    prompt = PromptTemplate(
            input_variables=["z"],
            template=template
        )
    llm = OpenAI(model_name='text-davinci-003', temperature=temperature)
    x=prompt.format(z=input_v)
    return x,llm(x)