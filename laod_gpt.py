def load_gpt(temperature,max_tokens,System_Message_content,Human_Message_content):

  from langchain.schema import(
      AIMessage,
      HumanMessage,
      SystemMessage
  )
  from langchain.chat_models import ChatOpenAI
  chat = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=temperature, max_tokens=max_tokens)
  messages = [
      SystemMessage(content=System_Message_content),
      HumanMessage(content=Human_Message_content)
  ]
  output = chat(messages)
  return(output.content)