def load_env():
    
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv(), override=True)
    os.environ.get("PINECONE_API_KEY")
    os.environ.get("OPENAI_API_KEY")
    os.environ.get("PINECONE_ENV")
    os.environ.get("HUGGINGFACEHUB_API_TOKEN")
    return True