from kedro.pipeline import node, Pipeline
from kedro.io import MemoryDataSet, DataCatalog, data_catalog
from kedro.runner import SequentialRunner


def add_filler(n=10):
    print('-'*n)


# Create the first node
def return_greeting():
    return "Hello"

return_greeting_node = node(func=return_greeting, inputs=None, outputs="salutation")

# Create the second node
def get_name():
    return input("Enter your name: ")

get_name_node = node(get_name, inputs=None, outputs="name")

# Create the third node
def greet(salutation, name):
    return f"{salutation} {name}!"

greet_node = node(greet, inputs=['salutation', 'name'], outputs="greeting")

# Create the pipeline
pipeline = Pipeline(nodes=[return_greeting_node, get_name_node, greet_node])

# Create the data catalog
data_catalog = DataCatalog({'salutation': MemoryDataSet(), 'name': MemoryDataSet()})

# Create the runner
runner = SequentialRunner()


if __name__ == '__main__':
    output = runner.run(pipeline, data_catalog)
    add_filler(); print()
    print('Kedro pipeline output')
    add_filler(); print()
    print(output)
    print()
