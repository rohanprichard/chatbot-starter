import os


def get_prompt(prompt_name: str):
    with open(os.path.join(os.path.dirname(__file__), f"prompts/{prompt_name}.txt"), "r") as file:
        prompt = file.read()
        return prompt
