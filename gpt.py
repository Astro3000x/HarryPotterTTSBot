import openai
def api(funcprompt : str):
    openai.api_key = "YOUR_API_KEY_HERE"

    model_engine = "text-davinci-003"
    prompt = funcprompt

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response
