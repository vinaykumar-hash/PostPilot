def ExtractTaskLlm(url: str, text: str) -> str:
    prompt = f'''This is a post from linkedin 'Author: nisha Shahnisha Shah• 3rd+3rd+
        URL:{url}
        Text: {text}
        , extract the info'''
    return prompt