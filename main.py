import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
def main():
    parser=argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt",type=str,help="User prompt")
    parser.add_argument("--verbose",action="store_true",help="Enable verbose output")
    args=parser.parse_args()

    user_prompt=args.user_prompt

    load_dotenv()
    api_key=os.environ.get("GEMINI_API_KEY")

    if api_key==None:
        raise RuntimeError("Please paste your gemini api key in the .env file")

    messages=[
        types.Content(
            role="user",
            parts=[
                types.Part(text=user_prompt)
            ]
        )
    ]

    client=genai.Client(api_key=api_key)

    response=client.models.generate_content(
        model="gemini-3-flash-preview",contents=messages
    )
    if response.usage_metadata==None:
        raise RuntimeError

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Response:\n",response.text)

if __name__ == "__main__":
    main()
