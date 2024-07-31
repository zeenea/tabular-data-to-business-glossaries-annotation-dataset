from transformers import pipeline, AutoTokenizer
from huggingface_hub import login
import torch
import json
import pandas as pd

HF_TOKEN = "YOUR HUGGINGFACE ACCESS TOKEN"


def generate_business_glossary(theme, list_of_tags, llm):
    """Generates a business glossary using a theme and a list of tags with an LLM."""
    messages = [
        {
            "role": "user",
            "content": "Generate in a json format, a hierarchical business glossary in the theme of Transportation, by creating concepts with descriptions linked together, using this list of tags: ['car', 'bolt', 'chevrolet', 'vehicle', 'green-report'].\
            The business glossary should contain business concepts with descriptions, instances and subclasses if needed.",
        },
        {
            "role": "assistant",
            "content": """{ 'Transportation': {
                                    'Vehicle': {
                                      'description': 'Any device capable of moving, and can be used for transportation.',
                                      'subclasses': {
                                        'Car': {
                                          'description': 'A road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor.',
                                          'instances': ['bolt', 'chevrolet']
                                        }
                                      }
                                    },
                                    'Environmental-Agency': {
                                                            'description': 'Organization focused on environmental impacts.',
                                                            'instances': ['green-report']
                                                            }
          },
      }"""
        },
        {
            "role": "user",
            "content": f"Generate in a json format, a hierarchical business glossary in the theme of {theme}, by creating concepts with descriptions linked together, using this list of tags: {list_of_tags}. \
                        The business glossary should contain business concepts with descriptions, instances and subclasses if needed."
        }
    ]

    valid_json = False
    cpt = 0

    while not valid_json:
        print(f"Iteration number: {cpt}")
        data = llm(messages)
        response = data[0]['generated_text'][-1]['content']
        print(response)

        try:
            glossary = json.loads(response)
            valid_json = True

        except Exception as error:
            print(f"An error occurred", type(error).__name__, "-", error)
            cpt += 1

    return glossary


def extract_info(data, parent_key='', node_type='Concept'):
    """Recursive function to Extract metadata in a json file"""
    records = []

    for key, value in data.items():
        code = parent_key+"."+key
        concept_name = key
        description = value.get('description', '')
        instances = value.get('instances', [])

        nb_subclasses = len(value.get('subclasses', {}))

        nb_properties = len(value.get('properties', {}))
        if nb_properties > 0:
            properties = list(value.get('properties').keys())
        else:
            properties = []

        records.append({
            'code': code[1:],
            'name': concept_name,
            'type': node_type,
            'description': description,
            'instances': instances,
            'sub_class_of': parent_key[1:],
            'properties': properties
        })

        if nb_subclasses > 0:
            records.extend(extract_info(value.get('subclasses'), parent_key=code, node_type='Concept'))

        if nb_properties > 0:
            records.extend(extract_info(value.get('properties'), parent_key=code, node_type='Property'))

    return records


if __name__ == "__main__":

    login(token=HF_TOKEN)

    if torch.cuda.is_available():
        # GPU available
        device = torch.device("cuda")
    else:
        # GPU not available, using CPU
        device = torch.device("cpu")

    # Load LLM
    model_name = "mistralai/Mistral-7B-Instruct-v0.3"
    llm = pipeline("text-generation", model=model_name, device=device, max_new_tokens=1024)

    # Load theme_to_tags_metadata.json file
    with open("metadata/theme_to_tags_metadata.json", "r") as f:
        theme2tags = json.load(f)

    for theme in theme2tags.keys():
        print(f"Generate business glossary for: {theme}")

        list_tags = theme2tags[theme]
        business_glossary = generate_business_glossary(theme, list_tags, llm)

        records = extract_info(business_glossary, "")
        glossary = pd.DataFrame(records, columns=['code', 'name', 'description', 'instances', 'sub_class_of'])

        idx_theme = list(theme2tags.keys()).index(theme)
        glossary.to_csv(f"SAVING-DIR/business_glossary_{idx_theme}_{theme}.csv")
