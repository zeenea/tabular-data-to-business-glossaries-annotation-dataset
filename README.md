# tabular-data-to-business-glossaries-annotation-dataset
A dataset of tabular data (tables and columns) from data.gov (USA) annotated to business glossaries using LLMs.

# Dataset Description
In this project we collected datasets from [data.gov](https://data.gov/) using their API,
by searching for datasets related to "Transport" field (The choice of the field was arbitrary).

We choose [data.gov](https://data.gov/) for the following reasons:
* Easy-to-use API
* A vast amount of public and open source data
* Tabular Datasets are annotated with _themes_ and a _list of tags_ 
* Tabular Columns have meaningful names 

--- describe the content, files ....


We conducted this project to build a relevant dataset for tabular data alignment with business glossaries.
We used Large Language Models LLMs to assist the dataset construction as described bellow.

# Dataset Construction

LLM used : 
### LLM-Generated Business Glossaries


### LLM-Generated Alignments


# Statistics on Datasets, Columns, Business Glossaries and Alignments
<table>
<tr><th>Dataset and Column statistics  </th> <th>Business Glossary statistics  </th><th>Alignments statistics</th></tr>
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
tabular-data-to-business-glossaries-annotation-dataset © 2024 is licensed under CC BY-NC-SA 4.0.
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
