import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def draft_email(purpose,tone,recepient):
    client= OpenAI(
        api_key=os.environ["OPENAI_API_KEY"]
    )
    #Prepare the Instruction
    instructions = """
    You are a professional email drafting assistant.
    Write clear, concise, grammatically correct emails.

    Rules:
    - Include a subject line and email body.
    - Follow the requested tone.
    - Do not invent dates, names, or facts.
    - Use placeholders when information is missing.
    - Return only the email draft.
    - Never send an email.
    """

    #Call the AI Model
    response=client.responses.create(
        model="gpt-4.1-mini",
        instructions=instructions,
        store=False,
        input=f"""
        EMAIL PURPOSE: {purpose}
        TONE: {tone}
        RECIPIENT: {recepient}
        """
    )
    return response.output_text