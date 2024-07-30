import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate


class GoogleAI:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def model(self, temperature: float = 0.7, max_output_tokens: int = None):
        llm = GoogleGenerativeAI(
            model="models/gemini-1.5-flash",
            google_api_key=self.api_key,
            temperature=temperature,
            max_output_tokens=max_output_tokens,
        )
        return llm

    def load_message(self, word: str):
        llm_loading = self.model(temperature=0.2, max_output_tokens=100)
        prompt_loading = PromptTemplate(
            input_variables=["word"],
            template="""Generate a short message to enthusiastically say a word sounds cool and you need some time to think about it.
            ###
            word: serendipity
            output: Wow, 'serendipity' sounds so cool! Give me a moment to let my thoughts wander through its magic. I'll be back with something amazing in just a bit!
            ###
            word: {word}
            output:
            """,
        )
        chain_loading = prompt_loading | llm_loading
        loading = chain_loading.invoke(word)

        return loading

    def poem(self, word: str):
        llm_poem = self.model(max_output_tokens=600)
        prompt_poem = PromptTemplate(
            input_variables=["word"],
            template=""" Write a poem that beautifully incorporates a word. The poem should be evocative, capturing the essence and imagery 
                        associated with the word, and should be at least 12 lines long. give it a title.
                        ###
                        word: serendipity.
                        poem :  In a meadow filled with sunlight's grace,
                                Where wildflowers sway in a gentle dance,
                                Serendipity finds its place,
                                A moment seized by purest chance.

                                A breeze that whispers through the trees,
                                A laugh that echoes on the breeze,
                                In the unexpected, hearts find ease,
                                In serendipity's sweet reprise.

                                Like stars that guide the lost at night,
                                Or rainbows after storms subside,
                                Serendipity brings delight,
                                A joyous spark we can't confide.
                        ###
                        word: {word}
                        title:
                        poem: 
                        """,
        )
        chain_poem = prompt_poem | llm_poem
        poem = chain_poem.invoke(word)

        lines = poem.strip().split("\n")
        tittle = lines[0].replace("## ", "")
        poem = "\n".join(lines[1:]).strip()

        return tittle, poem

