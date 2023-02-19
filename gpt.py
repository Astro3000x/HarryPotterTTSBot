import openai
def api(funcprompt : str):
    f = open("apikey.txt", "r")

    openai.api_key = f.read()

    model_engine = "text-davinci-003"
    prompt = funcprompt

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response
