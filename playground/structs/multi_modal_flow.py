# This might not work in the beginning but it's a starting point
from swarms.structs import Flow, GPT4V

llm = GPT4V()

flow = Flow(
    max_loops="auto",
    llm=llm,
)

flow.run(
    task="Describe this image in a few sentences: ",
    img="https://unsplash.com/photos/0pIC5ByPpZY",
)