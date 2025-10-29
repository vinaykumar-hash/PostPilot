def ExtractTaskLlm(url: str, text: str) -> str:
    prompt = f'''This is a post from linkedin
        URL:{url}
        Text: {text}
        , extract the info'''
    return prompt