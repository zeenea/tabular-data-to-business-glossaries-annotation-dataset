from transformers import pipeline, AutoTokenizer
from huggingface_hub import login
import torch
import json
import pandas as pd

HF_TOKEN = "YOU HUGGINGFACE ACCESS TOKEN"


def align_columns_to_business_entities(list_columns, list_entities, llm):
    """Generate alignments between tabular columns and business entities using an LLM."""

    # prompt to generate alignments
    messages = [
        {
            "role": "user",
            "content": "In a json format {column:business-concept}, generate alignments between these tabular columns: ['vehicle', 'model', 'environment'] and the next business glossary items: " \
                       + """["Transportation,"Transportattion.Vehicle", "Transportation.Vehicle.Car", "Transportation.Vehicle.Car.Model", "Transportation.Environmental-Agency", "Transportation.Environmental-Agency.Environment", "Transportation.Environmental-Agency.Agency"]. """ \
                       + "Business concepts should contain the right path in the business glossary."
        },
        {
            "role": "assistant",
            "content": """{
                "vehicle": "Transportation.Vehicle",
                "model": "Transportation.Vehicle.Car.Model",
                "environment": "Transportation.Environmental-Agency"
                }"""

        },
        {
            "role": "user",
            "content": "In a json format {column-business-concept}, generate alignments between these tabular columns:" \
                       + f"{list_columns} and the next business glossary items: {list_entities}. " \
                       + "Business concepts should contain the right path in the business glossary."
        }
    ]
    generation_valid = False
    cpt = 0
    while not generation_valid:
        print(f"loop {cpt}")
        cpt += 1
        data = llm(messages)
        response = data[0]['generated_text'][-1]['content']

        try:
            # validate the json format
            response_json = json.loads(response)

            alignments = pd.DataFrame({'columns': response_json.keys(), 'business-entities': response_json.values()})

            # alignments are valid if the business entity appears in the business glossary
            alignments['valid'] = alignments['business-entities'].apply(lambda x: 1 if x in list_entities else 0)
            alignments.loc[alignments[alignments['valid'] == 0].index, 'business-entities'] = ""
            non_valid_rows = alignments[alignments['valid'] == 0]

            accuracy = (alignments.shape[0]-non_valid_rows.shape[0]) / alignments.shape[0]
            print(f"Accuracy of syntax-valid alignment generated {accuracy}")

            if accuracy > 0.5 or cpt == 10:
                # if the valid alignments are more than half of the total alignments, then the generation is complete
                generation_valid = True

        except Exception as error:
            print(f"An error occurred", type(error).__name__, "-", error)

        if cpt == 20:
            print("Json Error")
            return pd.DataFrame()

    return alignments


def generate_alignments(dataset_metadata, column_dataset_metadata, llm):
    """ Generate tabular column alignments for all datasets."""

    for idx, row in dataset_metadata.iterrows():
        dataset_name = row['dataset_name']
        theme = row['theme']

        print(f"Generate alignments for dataset: {idx}, {dataset_name}, with theme: {theme}")

        columns = column_dataset_metadata[column_dataset_metadata['dataset_name'] == dataset_name]['column_name'].values

        id_business_glossary = list(theme2tags.keys()).index(theme)
        if id_business_glossary < 10:
            id_business_glossary = "0" + str(id_business_glossary)

        business_glossary_path = f"business-glossaries/business_glossary_{id_business_glossary}_{theme}.csv"
        entities = pd.read_csv(business_glossary_path, index_col=0)

        list_entities = entities['code'].values

        alignments = align_columns_to_business_entities(columns, list_entities, llm)
        alignments.to_csv(f"SAVING_DIR/alignment_{idx}_{dataset_name}.csv")


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

    # Load dataset metadata dataframe
    column_dataset_metadata_path = "metadata/column_and_dataset_metadata.csv"
    column_dataset_metadata = pd.read_csv(column_dataset_metadata_path, index_col=0)
    dataset_metadata = column_dataset_metadata.drop_duplicates(subset=['dataset_name']).drop(['column_name'], axis=1)
    dataset_metadata = dataset_metadata.reset_index(drop=True)

    # Load theme_to_tags_metadata.json file
    with open("metadata/theme_to_tags_metadata.json", 'r') as f:
        theme2tags = json.load(f)

    # Generate alignments between tabular data and business entities
    generate_alignments(dataset_metadata, column_dataset_metadata, llm)
