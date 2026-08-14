# Main entry point for the AI Code Assistant application. 
# This script handles user input, initializes the OpenAI client, 
# and generates content based on the provided prompt.

import argparse
import json
import os

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from functions.call_function import available_functions



def main():
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str, help="User prompt for LLM")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY environment variable not set.")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt}
    ]

    if args.verbose:
        print(f"User prompt: {args.user_prompt}\n")

    generate_content(client, messages, args.verbose)



def generate_content(client: OpenAI, messages: list, verbose: bool = False) -> None:
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    if not response.usage:
        raise RuntimeError("Error: API response appears to be malformed.")

    if verbose:
        print(
            f"Prompt tokens: {response.usage.prompt_tokens}\n"
            f"\nResponse tokens: {response.usage.completion_tokens}\n"
        )

    message = response.choices[0].message
    if not message.tool_calls:
        print("Response:")
        print(message.content)
        return

    for tool_call in message.tool_calls:
        if tool_call.type != "function":
            continue
        function_args = json.loads(tool_call.function.arguments or "{}")
        print(f"Calling function: {tool_call.function.name}({function_args})")


if __name__ == "__main__":
    main()
