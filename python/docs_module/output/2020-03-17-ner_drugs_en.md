---
layout: model
title: Ner DL Model Drugs
author: John Snow Labs
name: ner_drugs
class: NerDLModel
language: en
repository: clinical/models
date: 17/03/2020
tags: [clinical,ner]
article_header:
   type: cover
use_language_switcher: "Python-Scala-Java"
---

{:.h2_title}
## Description 
Pretrained named entity recognition deep learning model for Drugs.

 {:.h2_title}
## Predicted Entities
DrugChem (Drug and Chemicals) 

{:.btn-box}
<button class="button button-orange" disabled>Live Demo</button><br/>[Open in Colab](https://colab.research.google.com/github/JohnSnowLabs/spark-nlp-workshop/blob/master/tutorials/Certification_Trainings/Healthcare/1.Clinical_Named_Entity_Recognition_Model.ipynb){:.button.button-orange.button-orange-trans.co.button-icon}<br/>[Download](https://s3.amazonaws.com/auxdata.johnsnowlabs.com/clinical/models/ner_drugs_en_2.4.4_2.4_1584452534235.zip){:.button.button-orange.button-orange-trans.arr.button-icon}<br/>

## How to use 
<div class="tabs-box" markdown="1">

{% include programmingLanguageSelectScalaPython.html %}

```python

```

```scala

```
</div>

{:.h2_title}
## Results
```bash

```

{:.model-param}
## Model Information

{:.table-model}
|-------------------------|-------------------------------|
| Model Name              | ner_drugs                     |
| Model Class             | NerDLModel                    |
| Spark Compatibility     | 2.4.4                         |
| Spark NLP Compatibility | 2.4                           |
| License                 | Licensed                      |
| Edition                 | Healthcare                    |
| Input Labels            |                               |
| Output Labels           | DrugChem (Drug and Chemicals) |
| Language                | en                            |
| Dimension               |                               |
| Case Sensitive          | 0.0                           |
| Upstream Dependencies   | embeddings_clinical           |




{:.h2_title}
## Data Source

Trained on i2b2_med7 + FDA with `embeddings_clinical`.

