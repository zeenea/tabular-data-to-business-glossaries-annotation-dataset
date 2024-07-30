# tabular-data-to-business-glossaries-annotation-dataset
A dataset of tabular data from [data.gov](https://data.gov/) annotated to business glossaries using LLMs.

# Dataset Description
Following a collaboration between [Zeenea](https://zeenea.com/fr/) and [LIP6](https://www.lip6.fr/) through an industrial thesis project on **Smart Metadata Management Systems**,
we encountered a number of data-related challenges.
Through this project, we took the initiative to build a relevant dataset for tabular data alignment with business glossaries.

This repository contains tabular data (datasets and columns) collected from [data.gov](https://data.gov/) , various business glossaries, and alignments between tabular data and business glossary entities.

We choose [data.gov](https://data.gov/) for the following reasons:
* Easy-to-use API
* A vast amount of public and open source data
* Tabular Datasets are annotated with _themes_ and a _list of tags_ 
* Tabular Columns have meaningful names 

The table bellow describe the main content of this repository:

| Content Description  |                                                        |
|----------------------|--------------------------------------------------------|
| data/                | Collection of tables in csv files                      |
| metadata/            | Metadata about Datasets, Columns, Themes and Tags      |
| business-glossaries/ | Collection of business-glossaries in csv files         |
| alignments/          | Column and Dataset alignments with business-glossaries |

We used Large Language Models LLMs to assist the dataset construction as described bellow.

# Dataset Construction

We collected 226 Datasets (Tables) from [data.gov](https://data.gov/) using their API, 
by searching for datasets related to "**Transport**" field (The choice of the field was arbitrary).



### LLM-Generated Business Glossaries


### LLM-Generated Alignments



# Statistics on Datasets and Columns, Business Glossaries and Alignments
<table>
<tr><th>1. Dataset and Column statistics  </th> <th>2. Business Glossary statistics  </th><th>3. Alignments statistics</th></tr>
<tr><td>

|                                       |      |
|---------------------------------------|------|
| Number of datasets                    | 226  |
| Number of columns                     | 5232 |
| Maximum number of columns per dataset | 381  |
| Minimum number of columns per dataset | 2    |
| Mean number of columns per dataset    | 23   |
| Maximum number of rows per dataset    | 100  |
| Minimum number of row per dataset     | 4    |
| Mean number of rows per dataset       | 62   |

</td><td>

|                                                |     |
|------------------------------------------------|-----|
| Number of Business Glossaries                  | 34  |
| Maximum number of business entity per glossary | 26  |
| Minimum number of business entity per glossary | 4   |
| Mean number of business entity per glossary    | 14  |
| Maximum number of levels per glossary          | 9   |
| Minimum number of levels per glossary          | 2   |
| Mean number of levels per glossary             | 4   |

</td><td>

|                            |        |
|----------------------------|--------|
| Number of aligned columns  | **1017**   |
| Rate of aligned columns    | **19.02%** |
| Number of aligned datasets | **226**    |
| Rate of aligned datasets   | **100%**   |

</td></tr> </table>



# License
tabular-data-to-business-glossaries-annotation-dataset © 2024 by Zeenea is licensed under CC BY-NC-SA 4.0.
To view a copy of this license, visit https://creativecommons.org/licenses/by-nc-sa/4.0/ or go to [LICENCE.md](https://github.com/AKNOUCHEanis/tabular-data-to-business-glossaries-annotation-dataset/blob/main/LICENSE.md).

Certain datasets utilized in this project are governed by specific licenses as detailed in [metadata/column_and_dataset_metadata.csv](https://github.com/AKNOUCHEanis/tabular-data-to-business-glossaries-annotation-dataset/blob/main/metadata/column_and_dataset_metadata.csv).  
The corresponding licenses are provided in [data.gov](https://data.gov/) for each dataset. 

The dataset licenses used in this project are:
* http://opendatacommons.org/licenses/odbl/1.0/
* https://creativecommons.org/licenses/by/4.0/
* https://www.usa.gov/government-works
* http://creativecommons.org/licenses/by/4.0/legalcode
* https://louisville-metro-opendata-lojic.hub.arcgis.com/pages/terms-of-use-and-license
* http://creativecommons.org/licenses/by-sa/4.0/legalcode
* http://creativecommons.org/publicdomain/zero/1.0/legalcode
* http://www.usa.gov/publicdomain/label/1.0/
* http://opendefinition.org/licenses/odc-odbl/
* https://creativecommons.org/licenses/by/4.0
* http://opendatacommons.org/licenses/pddl/1.0/
* https://logis.loudoun.gov/loudoun/disclaimer.html
* https://creativecommons.org/licenses/by-nc-nd/4.0
