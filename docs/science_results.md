# Model inventory

Version   | Approach    | Micro f1 | Description
--------- | ----------- | -------- | -------
2020.02.0 | tfidf-svm   | 0.63     | science_grants_tagged_title_synopsis.jsonl. only title and synopsis is used for text.
2020.02.1 | tfidf-svm   | 0.67     | science_grants_tagged_all.jsonl. additional to title and synopsis, lay summary and research question ("Qu.") is used
2020.02.2 | tfidf-svm   | 0.61     | science_granted_tagged_all.jsonl used for training and science_grants_tagged_title_synopsis.jsonl used for testing.
2020.03.0 | spacy-textclassifier | 0.57 | science_grants_tagged_title_synopsis.jsonl. 20 iterations.
2020.03.1 | classifier-chain-tfidf-svm | 0.65 | science_grants_tagged_title_synopsis.jsonl. classifier chain instead of binary relevance
2020.03.2 | labelpowerset-tfidf-svm | 0.45 | science_grants_tagged_title_synopsis.jsonl. label powerset instead of binary relevance
2020.03.3 | binaryrelevance-tfidf-knn | 0.63 | science_grants_tagged_title_synopsis.jsonl. knn instead of svm.
2020.03.4 | bert-svm | 0.62 | science_grants_tagged_title_synopsis.jsonl. bert embedding instead of tfidf.
2020.03.5 | scibert-svm | 0.64 | science_grants_tagged_title_synopsis.jsonl. scibert embedding instead of tfidf.
2020.04.0 | spacy-textclassifier | 0.61 | same as 2020.03.0 but with pretrained vectors on 10k mesh dataset
2020.04.1 | spacy-textclassifier | 0.59 | same as 2020.03.0 but with pretrained vectors on 100k mesh dataset
2020.04.2 | bilstm | 0.57 | same data as above trained with our bilstm architecture
2020.04.3 | cnn | 0.54 | same data as above trained with our cnn architecture
2020.05.0 | tfidf-svm | 0.66 | same as 2020.2.0 with min_df=5
2020.05.1 | tfidf-svm | 0.70 | same as 2020.5.0 with class_weight="balanced"
2020.05.2 | tfidf-svm | 0.71 | same as 2020.5.1 with ngram_range=(1,2)
2020.05.3 | bert | 0.58 | same data as 2020.2.0 but model is fine tuned bert.
2020.05.4 | scibert | 0.68 | same as 2020.05.3 but using scibert as pretrained bert
2020.05.5 | scibert | 0.71 | same as 2020.05.4 but learning rate 2e-5 and 10 epochs
2020.05.6 | doc2vec-svm | 0.57 | doc2vec instead of tfidf and sgd instead of svm
2020.05.7 | doc2vec-tfidf-svm | 0.68 | similar to 2020.05.0 with ngram_range=(1,2). performance without doc2vec (only tfidf) 0.67.
2020.05.8 | sent2vec-svm | 0.65 | same as 2020.05.6 but with sent2vec instead of doc2vec
2020.05.9 | sent2vec-tfidf-svm | 0.70 | same as 2020.05.7 but with sent2vec instead of doc2vec. performance without sent2vec (only tfidf) is 0.68
2020.06.0 | ensemble of tfidf and scibert | 0.73 | combines tfidf-svm-2020.05.2 and scibert-2020.05.5
2020.06.1 | ensemble of tfidf and scibert | 0.75 | same as 2020.06.0 with threshold 0.3
2020.06.2 | tfidf-adaboost | 0.63 | adaboost after tfidf
2020.06.3 | tfidf-gboost | 0.66 | same as 2020.06.2 but with gradient boosting instead
2020.10.0 | tfidf-svm | 0.72 | same as 2020.05.2 with train data including lay summary
2020.10.1 | tfidf-svm | 0.72 | same as 2020.05.2 with train data including lay summary and research question
2020.10.2 | tfidf-svm | 0.69 | same as 2020.05.2 with train data including lay summary but testing on title+synopsis
2020.10.3 | tfidf-svm | 0.69 | same as 2020.05.2 with train data including lay summary and research question but testing on title+synopsis
2020.10.4 | tfidf-svm | 0.52 | same as 2020.05.2 but testing on titles only
2020.10.5 | tfidf-svm | 0.67 | same as 2020.05.2 but test on title+lay summary
2020.10.6 | tfidf-svm | 0.54 | same as 2020.05.2 but test on title+research question
2020.10.7 | tfidf-svm | 0.46 | same as 2020.05.2 but train and test on title only
2020.10.8 | tfidf-svm | 0.48 | same as 2020.05.2 but train on title+synopsis+lay summary+research question and test on titles only
2020.10.9 | tfidf-svm | 0.66 | same as 2020.05.2 but train on title+synopsis+lay summary+research question and test on titles+summary
2020.10.10 | tfidf-svm | 0.52 | same as 2020.5.2 but train on title+synopsis+lay summary+research question and test on titles+question
2020.10.11 | tfidf-svm | 0.66 | same as 2020.5.2 but train and test on title+lay summary
2020.10.12 | tfidf-svm | 0.52 | same as 2020.5.2 but train and test on title+research question
2020.10.13 | tfidf-svm | 0.72 | same as 2020.5.2 but train on title+synopsis and test on title+synopsis+lay summary+research question
2020.10.14 | tfidf-svm | 0.72 | same as 2020.5.2 but train on title+synopsis and test on title+synopsis+lay summary
2020.10.15 | tfidf-svm | 0.71 | same as 2020.5.2 but train on title+synopsis and test on title+synopsis+research_question
2020.10.16 | tfidf+onehot_team | 0.71 | similar to 2020.5.2 but we add team as one hot variable to the features. as data get shuffled differently it seems as the performance stays the same but it actually increases 1% compared to removing the team variable
2020.10.17 | tfidf+onehot_scheme | 0.68 | similar to 2020.10.16 but this time we add scheme as one hot variable.
2021.03.0 | cnn | 0.58 | same as 2020.04.3 but with transformers tokenizer for encoder
2021.03.1 | tfidf-transformers-svm | 0.68 | same as 2020.05.2 but tokenizer is TransformersTokenizer

## 2020.02.0

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.14      0.25         7
                                          11: Parasites       1.00      0.72      0.84        29
                     12: Brain Cells Circuits & Systems       0.89      0.69      0.78        84
                           13: Sensory & Motor Function       1.00      0.59      0.74        27
                              14: Behaviour & Cognition       0.90      0.76      0.82        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.75      0.35      0.48        51
                          17: Health Services & Systems       0.67      0.24      0.35        17
                                       18: Surveillance       0.80      0.23      0.36        35
                 19: Maternal Child & Adolescent Health       0.92      0.52      0.67        21
                                 1: Genetics & Genomics       0.72      0.46      0.56        68
                             20: Nutrition & Metabolism       1.00      0.12      0.22        16
                                     21: Cardiovascular       0.80      0.40      0.53        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.92      0.49      0.64        47
                2: Gene Regulation and Genome Integrity       0.90      0.51      0.65        71
                        3: Protein Structure & Function       0.81      0.59      0.68        71
                                        4: Cell Biology       0.73      0.45      0.56        77
                               5: Developmental Biology       1.00      0.14      0.25        28
                                   6: Stem Cell Biology       1.00      0.36      0.53        11
                                          7: Immunology       0.95      0.74      0.83        72
                                            8: Bacteria       0.93      0.57      0.70        46
                                             9: Viruses       1.00      0.55      0.71        42

                                              micro avg       0.87      0.50      0.63       927
                                              macro avg       0.78      0.40      0.51       927
                                           weighted avg       0.83      0.50      0.61       927
                                            samples avg       0.74      0.54      0.59       927
```

## 2020.02.01

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.29      0.44         7
                                          11: Parasites       1.00      0.72      0.84        29
                     12: Brain Cells Circuits & Systems       0.91      0.75      0.82        84
                           13: Sensory & Motor Function       1.00      0.63      0.77        27
                              14: Behaviour & Cognition       0.94      0.76      0.84        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.81      0.41      0.55        51
                          17: Health Services & Systems       1.00      0.24      0.38        17
                                       18: Surveillance       0.77      0.29      0.42        35
                 19: Maternal Child & Adolescent Health       0.92      0.52      0.67        21
                                 1: Genetics & Genomics       0.79      0.54      0.64        68
                             20: Nutrition & Metabolism       1.00      0.25      0.40        16
                                     21: Cardiovascular       0.78      0.70      0.74        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.50      0.11      0.18         9
24: Data Science Computational & Mathematical Modelling       0.89      0.36      0.52        47
                2: Gene Regulation and Genome Integrity       0.95      0.56      0.71        71
                        3: Protein Structure & Function       0.86      0.68      0.76        71
                                        4: Cell Biology       0.66      0.51      0.57        77
                               5: Developmental Biology       0.67      0.14      0.24        28
                                   6: Stem Cell Biology       0.86      0.55      0.67        11
                                          7: Immunology       0.88      0.72      0.79        72
                                            8: Bacteria       0.94      0.65      0.77        46
                                             9: Viruses       1.00      0.62      0.76        42

                                              micro avg       0.87      0.54      0.67       927
                                              macro avg       0.80      0.46      0.56       927
                                           weighted avg       0.84      0.54      0.65       927
                                            samples avg       0.76      0.59      0.63       927
```

## 2020.02.02

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.14      0.25         7
                                          11: Parasites       1.00      0.66      0.79        29
                     12: Brain Cells Circuits & Systems       0.95      0.65      0.77        84
                           13: Sensory & Motor Function       1.00      0.52      0.68        27
                              14: Behaviour & Cognition       0.92      0.62      0.74        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.81      0.33      0.47        51
                          17: Health Services & Systems       0.80      0.24      0.36        17
                                       18: Surveillance       0.78      0.20      0.32        35
                 19: Maternal Child & Adolescent Health       0.91      0.48      0.62        21
                                 1: Genetics & Genomics       0.77      0.50      0.61        68
                             20: Nutrition & Metabolism       1.00      0.12      0.22        16
                                     21: Cardiovascular       0.67      0.20      0.31        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.94      0.32      0.48        47
                2: Gene Regulation and Genome Integrity       0.95      0.49      0.65        71
                        3: Protein Structure & Function       0.81      0.62      0.70        71
                                        4: Cell Biology       0.70      0.45      0.55        77
                               5: Developmental Biology       0.75      0.11      0.19        28
                                   6: Stem Cell Biology       1.00      0.27      0.43        11
                                          7: Immunology       0.94      0.71      0.81        72
                                            8: Bacteria       0.93      0.57      0.70        46
                                             9: Viruses       1.00      0.52      0.69        42

                                              micro avg       0.88      0.47      0.61       927
                                              macro avg       0.78      0.36      0.47       927
                                           weighted avg       0.84      0.47      0.59       927
                                            samples avg       0.71      0.51      0.56       927
```

## 2020.03.0

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       1.00      0.31      0.47        29
                     12: Brain Cells Circuits & Systems       0.80      0.79      0.80        84
                           13: Sensory & Motor Function       0.74      0.52      0.61        27
                              14: Behaviour & Cognition       0.88      0.62      0.73        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.62      0.55      0.58        51
                          17: Health Services & Systems       0.60      0.18      0.27        17
                                       18: Surveillance       1.00      0.09      0.16        35
                 19: Maternal Child & Adolescent Health       0.67      0.29      0.40        21
                                 1: Genetics & Genomics       0.71      0.54      0.62        68
                             20: Nutrition & Metabolism       0.60      0.19      0.29        16
                                     21: Cardiovascular       0.80      0.40      0.53        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.45      0.57      0.50        47
                2: Gene Regulation and Genome Integrity       0.69      0.58      0.63        71
                        3: Protein Structure & Function       0.83      0.49      0.62        71
                                        4: Cell Biology       0.58      0.44      0.50        77
                               5: Developmental Biology       1.00      0.07      0.13        28
                                   6: Stem Cell Biology       0.50      0.09      0.15        11
                                          7: Immunology       0.85      0.76      0.80        72
                                            8: Bacteria       0.92      0.50      0.65        46
                                             9: Viruses       1.00      0.31      0.47        42

                                              micro avg       0.72      0.47      0.57       927
                                              macro avg       0.64      0.35      0.41       927
                                           weighted avg       0.73      0.47      0.54       927
                                            samples avg       0.65      0.51      0.53       927

```

## 2020.03.1

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.14      0.25         7
                                          11: Parasites       1.00      0.72      0.84        29
                     12: Brain Cells Circuits & Systems       0.89      0.68      0.77        84
                           13: Sensory & Motor Function       1.00      0.63      0.77        27
                              14: Behaviour & Cognition       0.90      0.76      0.82        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.76      0.31      0.44        51
                          17: Health Services & Systems       0.67      0.24      0.35        17
                                       18: Surveillance       0.80      0.23      0.36        35
                 19: Maternal Child & Adolescent Health       0.92      0.52      0.67        21
                                 1: Genetics & Genomics       0.71      0.47      0.57        68
                             20: Nutrition & Metabolism       1.00      0.12      0.22        16
                                     21: Cardiovascular       0.80      0.40      0.53        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.92      0.47      0.62        47
                2: Gene Regulation and Genome Integrity       0.91      0.58      0.71        71
                        3: Protein Structure & Function       0.80      0.73      0.76        71
                                        4: Cell Biology       0.59      0.53      0.56        77
                               5: Developmental Biology       0.80      0.14      0.24        28
                                   6: Stem Cell Biology       1.00      0.45      0.62        11
                                          7: Immunology       0.87      0.81      0.83        72
                                            8: Bacteria       0.93      0.61      0.74        46
                                             9: Viruses       1.00      0.57      0.73        42

                                              micro avg       0.84      0.53      0.65       927
                                              macro avg       0.76      0.42      0.52       927
                                           weighted avg       0.81      0.53      0.62       927
                                            samples avg       0.76      0.58      0.62       927
```

## 2020.3.2

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       1.00      0.10      0.19        29
                     12: Brain Cells Circuits & Systems       0.77      0.65      0.71        84
                           13: Sensory & Motor Function       0.87      0.48      0.62        27
                              14: Behaviour & Cognition       0.70      0.67      0.68        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       1.00      0.02      0.04        51
                          17: Health Services & Systems       0.00      0.00      0.00        17
                                       18: Surveillance       0.00      0.00      0.00        35
                 19: Maternal Child & Adolescent Health       1.00      0.05      0.09        21
                                 1: Genetics & Genomics       0.62      0.50      0.55        68
                             20: Nutrition & Metabolism       0.00      0.00      0.00        16
                                     21: Cardiovascular       0.00      0.00      0.00        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       1.00      0.06      0.12        47
                2: Gene Regulation and Genome Integrity       0.88      0.42      0.57        71
                        3: Protein Structure & Function       0.45      0.77      0.57        71
                                        4: Cell Biology       0.34      0.75      0.47        77
                               5: Developmental Biology       0.00      0.00      0.00        28
                                   6: Stem Cell Biology       0.00      0.00      0.00        11
                                          7: Immunology       0.73      0.67      0.70        72
                                            8: Bacteria       1.00      0.07      0.12        46
                                             9: Viruses       1.00      0.14      0.25        42

                                              micro avg       0.57      0.38      0.45       927
                                              macro avg       0.47      0.22      0.24       927
                                           weighted avg       0.63      0.38      0.38       927
                                            samples avg       0.57      0.42      0.46       927
```

## 2020.03.3

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.14      0.25         7
                                          11: Parasites       1.00      0.72      0.84        29
                     12: Brain Cells Circuits & Systems       0.89      0.69      0.78        84
                           13: Sensory & Motor Function       1.00      0.59      0.74        27
                              14: Behaviour & Cognition       0.90      0.76      0.82        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.75      0.35      0.48        51
                          17: Health Services & Systems       0.67      0.24      0.35        17
                                       18: Surveillance       0.80      0.23      0.36        35
                 19: Maternal Child & Adolescent Health       0.92      0.52      0.67        21
                                 1: Genetics & Genomics       0.72      0.46      0.56        68
                             20: Nutrition & Metabolism       1.00      0.12      0.22        16
                                     21: Cardiovascular       0.80      0.40      0.53        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.92      0.49      0.64        47
                2: Gene Regulation and Genome Integrity       0.90      0.51      0.65        71
                        3: Protein Structure & Function       0.81      0.59      0.68        71
                                        4: Cell Biology       0.73      0.45      0.56        77
                               5: Developmental Biology       1.00      0.14      0.25        28
                                   6: Stem Cell Biology       1.00      0.36      0.53        11
                                          7: Immunology       0.95      0.74      0.83        72
                                            8: Bacteria       0.93      0.57      0.70        46
                                             9: Viruses       1.00      0.55      0.71        42

                                              micro avg       0.87      0.50      0.63       927
                                              macro avg       0.78      0.40      0.51       927
                                           weighted avg       0.83      0.50      0.61       927
                                            samples avg       0.74      0.54      0.59       927
```

## 2020.03.4

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.67      0.29      0.40         7
                                          11: Parasites       0.73      0.76      0.75        29
                     12: Brain Cells Circuits & Systems       0.76      0.76      0.76        84
                           13: Sensory & Motor Function       0.80      0.74      0.77        27
                              14: Behaviour & Cognition       0.82      0.88      0.85        58
                      15: Behavioural & Social Sciences       0.31      0.33      0.32        12
                                16: Health Intervention       0.61      0.55      0.58        51
                          17: Health Services & Systems       0.48      0.59      0.53        17
                                       18: Surveillance       0.50      0.54      0.52        35
                 19: Maternal Child & Adolescent Health       0.50      0.67      0.57        21
                                 1: Genetics & Genomics       0.60      0.63      0.61        68
                             20: Nutrition & Metabolism       0.45      0.31      0.37        16
                                     21: Cardiovascular       0.71      0.50      0.59        10
                              22: Experimental Medicine       0.11      0.11      0.11        18
                                    23: Medical Imaging       0.33      0.22      0.27         9
24: Data Science Computational & Mathematical Modelling       0.46      0.49      0.47        47
                2: Gene Regulation and Genome Integrity       0.58      0.61      0.59        71
                        3: Protein Structure & Function       0.74      0.70      0.72        71
                                        4: Cell Biology       0.54      0.58      0.56        77
                               5: Developmental Biology       0.50      0.68      0.58        28
                                   6: Stem Cell Biology       0.33      0.36      0.35        11
                                          7: Immunology       0.69      0.71      0.70        72
                                            8: Bacteria       0.61      0.67      0.64        46
                                             9: Viruses       0.78      0.69      0.73        42

                                              micro avg       0.61      0.63      0.62       927
                                              macro avg       0.57      0.56      0.56       927
                                           weighted avg       0.62      0.63      0.62       927
                                            samples avg       0.64      0.67      0.61       927
```

## 2020.03.5

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.75      0.43      0.55         7
                                          11: Parasites       0.79      0.93      0.86        29
                     12: Brain Cells Circuits & Systems       0.78      0.81      0.80        84
                           13: Sensory & Motor Function       0.78      0.67      0.72        27
                              14: Behaviour & Cognition       0.82      0.81      0.82        58
                      15: Behavioural & Social Sciences       0.31      0.33      0.32        12
                                16: Health Intervention       0.49      0.55      0.52        51
                          17: Health Services & Systems       0.35      0.41      0.38        17
                                       18: Surveillance       0.46      0.54      0.50        35
                 19: Maternal Child & Adolescent Health       0.58      0.67      0.62        21
                                 1: Genetics & Genomics       0.59      0.69      0.64        68
                             20: Nutrition & Metabolism       0.70      0.44      0.54        16
                                     21: Cardiovascular       0.57      0.40      0.47        10
                              22: Experimental Medicine       0.16      0.22      0.19        18
                                    23: Medical Imaging       0.75      0.33      0.46         9
24: Data Science Computational & Mathematical Modelling       0.57      0.55      0.56        47
                2: Gene Regulation and Genome Integrity       0.62      0.62      0.62        71
                        3: Protein Structure & Function       0.72      0.75      0.73        71
                                        4: Cell Biology       0.53      0.55      0.54        77
                               5: Developmental Biology       0.54      0.50      0.52        28
                                   6: Stem Cell Biology       0.47      0.64      0.54        11
                                          7: Immunology       0.73      0.76      0.75        72
                                            8: Bacteria       0.75      0.87      0.81        46
                                             9: Viruses       0.76      0.60      0.67        42

                                              micro avg       0.63      0.65      0.64       927
                                              macro avg       0.61      0.59      0.59       927
                                           weighted avg       0.64      0.65      0.64       927
                                            samples avg       0.67      0.70      0.64       927
```

## 2020.04.0

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.95      0.66      0.78        29
                     12: Brain Cells Circuits & Systems       0.86      0.71      0.78        84
                           13: Sensory & Motor Function       0.78      0.52      0.62        27
                              14: Behaviour & Cognition       0.87      0.69      0.77        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.80      0.47      0.59        51
                          17: Health Services & Systems       0.30      0.18      0.22        17
                                       18: Surveillance       0.54      0.40      0.46        35
                 19: Maternal Child & Adolescent Health       0.70      0.33      0.45        21
                                 1: Genetics & Genomics       0.60      0.76      0.68        68
                             20: Nutrition & Metabolism       0.67      0.12      0.21        16
                                     21: Cardiovascular       1.00      0.30      0.46        10
                              22: Experimental Medicine       0.11      0.06      0.07        18
                                    23: Medical Imaging       1.00      0.11      0.20         9
24: Data Science Computational & Mathematical Modelling       0.76      0.34      0.47        47
                2: Gene Regulation and Genome Integrity       0.83      0.49      0.62        71
                        3: Protein Structure & Function       0.73      0.69      0.71        71
                                        4: Cell Biology       0.45      0.64      0.52        77
                               5: Developmental Biology       0.70      0.25      0.37        28
                                   6: Stem Cell Biology       1.00      0.18      0.31        11
                                          7: Immunology       0.87      0.74      0.80        72
                                            8: Bacteria       0.74      0.43      0.55        46
                                             9: Viruses       0.88      0.50      0.64        42

                                              micro avg       0.71      0.53      0.61       927
                                              macro avg       0.67      0.40      0.47       927
                                           weighted avg       0.72      0.53      0.59       927
                                            samples avg       0.66      0.56      0.57       927
```

## 2020.04.1

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.78      0.62      0.69        29
                     12: Brain Cells Circuits & Systems       0.84      0.74      0.78        84
                           13: Sensory & Motor Function       0.85      0.63      0.72        27
                              14: Behaviour & Cognition       0.88      0.48      0.62        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.71      0.43      0.54        51
                          17: Health Services & Systems       0.33      0.12      0.17        17
                                       18: Surveillance       0.41      0.20      0.27        35
                 19: Maternal Child & Adolescent Health       0.62      0.24      0.34        21
                                 1: Genetics & Genomics       0.56      0.68      0.61        68
                             20: Nutrition & Metabolism       1.00      0.06      0.12        16
                                     21: Cardiovascular       1.00      0.50      0.67        10
                              22: Experimental Medicine       0.09      0.11      0.10        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.46      0.53      0.50        47
                2: Gene Regulation and Genome Integrity       0.72      0.54      0.61        71
                        3: Protein Structure & Function       0.75      0.56      0.65        71
                                        4: Cell Biology       0.52      0.71      0.60        77
                               5: Developmental Biology       0.57      0.29      0.38        28
                                   6: Stem Cell Biology       0.58      0.64      0.61        11
                                          7: Immunology       0.67      0.86      0.76        72
                                            8: Bacteria       0.81      0.54      0.65        46
                                             9: Viruses       0.95      0.45      0.61        42

                                              micro avg       0.65      0.53      0.59       927
                                              macro avg       0.59      0.41      0.46       927
                                           weighted avg       0.66      0.53      0.57       927
                                            samples avg       0.64      0.58      0.57       927
```

## 2020.4.2

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.92      0.83      0.87        29
                     12: Brain Cells Circuits & Systems       0.91      0.70      0.79        84
                           13: Sensory & Motor Function       0.71      0.37      0.49        27
                              14: Behaviour & Cognition       0.74      0.69      0.71        58
                      15: Behavioural & Social Sciences       0.50      0.17      0.25        12
                                16: Health Intervention       0.54      0.25      0.35        51
                          17: Health Services & Systems       0.25      0.12      0.16        17
                                       18: Surveillance       0.45      0.29      0.35        35
                 19: Maternal Child & Adolescent Health       0.54      0.33      0.41        21
                                 1: Genetics & Genomics       0.68      0.41      0.51        68
                             20: Nutrition & Metabolism       0.33      0.06      0.11        16
                                     21: Cardiovascular       1.00      0.30      0.46        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.54      0.45      0.49        47
                2: Gene Regulation and Genome Integrity       0.69      0.52      0.59        71
                        3: Protein Structure & Function       0.71      0.49      0.58        71
                                        4: Cell Biology       0.64      0.51      0.57        77
                               5: Developmental Biology       0.75      0.21      0.33        28
                                   6: Stem Cell Biology       0.88      0.64      0.74        11
                                          7: Immunology       0.85      0.62      0.72        72
                                            8: Bacteria       0.80      0.72      0.76        46
                                             9: Viruses       0.88      0.36      0.51        42

                                              micro avg       0.72      0.47      0.57       927
                                              macro avg       0.60      0.38      0.45       927
                                           weighted avg       0.68      0.47      0.55       927
                                            samples avg       0.61      0.51      0.52       927
```

## 2020.04.3

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.81      0.76      0.79        29
                     12: Brain Cells Circuits & Systems       0.92      0.64      0.76        84
                           13: Sensory & Motor Function       0.71      0.37      0.49        27
                              14: Behaviour & Cognition       0.67      0.52      0.58        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.61      0.37      0.46        51
                          17: Health Services & Systems       0.50      0.18      0.26        17
                                       18: Surveillance       0.44      0.23      0.30        35
                 19: Maternal Child & Adolescent Health       0.00      0.00      0.00        21
                                 1: Genetics & Genomics       0.62      0.56      0.59        68
                             20: Nutrition & Metabolism       1.00      0.12      0.22        16
                                     21: Cardiovascular       0.00      0.00      0.00        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.41      0.15      0.22        47
                2: Gene Regulation and Genome Integrity       0.73      0.62      0.67        71
                        3: Protein Structure & Function       0.79      0.63      0.70        71
                                        4: Cell Biology       0.52      0.52      0.52        77
                               5: Developmental Biology       0.62      0.29      0.39        28
                                   6: Stem Cell Biology       0.50      0.27      0.35        11
                                          7: Immunology       0.80      0.68      0.74        72
                                            8: Bacteria       0.81      0.28      0.42        46
                                             9: Viruses       0.54      0.45      0.49        42

                                              micro avg       0.68      0.45      0.54       927
                                              macro avg       0.50      0.32      0.37       927
                                           weighted avg       0.63      0.45      0.51       927
                                            samples avg       0.62      0.48      0.51       927
```

## 2020.05.0

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.14      0.25         7
                                          11: Parasites       1.00      0.72      0.84        29
                     12: Brain Cells Circuits & Systems       0.91      0.71      0.80        84
                           13: Sensory & Motor Function       1.00      0.70      0.83        27
                              14: Behaviour & Cognition       0.89      0.72      0.80        58
                      15: Behavioural & Social Sciences       1.00      0.08      0.15        12
                                16: Health Intervention       0.79      0.45      0.58        51
                          17: Health Services & Systems       0.57      0.24      0.33        17
                                       18: Surveillance       0.79      0.31      0.45        35
                 19: Maternal Child & Adolescent Health       0.86      0.57      0.69        21
                                 1: Genetics & Genomics       0.72      0.46      0.56        68
                             20: Nutrition & Metabolism       1.00      0.12      0.22        16
                                     21: Cardiovascular       0.86      0.60      0.71        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.85      0.47      0.60        47
                2: Gene Regulation and Genome Integrity       0.93      0.56      0.70        71
                        3: Protein Structure & Function       0.79      0.63      0.70        71
                                        4: Cell Biology       0.72      0.51      0.60        77
                               5: Developmental Biology       0.83      0.18      0.29        28
                                   6: Stem Cell Biology       0.83      0.45      0.59        11
                                          7: Immunology       0.90      0.74      0.81        72
                                            8: Bacteria       0.93      0.57      0.70        46
                                             9: Viruses       1.00      0.64      0.78        42

                                              micro avg       0.86      0.53      0.66       927
                                              macro avg       0.80      0.44      0.54       927
                                           weighted avg       0.83      0.53      0.64       927
                                            samples avg       0.75      0.57      0.62       927
```

## 2020.05.1

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       0.95      0.72      0.82        29
                     12: Brain Cells Circuits & Systems       0.89      0.80      0.84        84
                           13: Sensory & Motor Function       0.84      0.78      0.81        27
                              14: Behaviour & Cognition       0.78      0.81      0.80        58
                      15: Behavioural & Social Sciences       0.40      0.50      0.44        12
                                16: Health Intervention       0.60      0.61      0.60        51
                          17: Health Services & Systems       0.56      0.53      0.55        17
                                       18: Surveillance       0.67      0.74      0.70        35
                 19: Maternal Child & Adolescent Health       0.72      0.62      0.67        21
                                 1: Genetics & Genomics       0.70      0.72      0.71        68
                             20: Nutrition & Metabolism       0.75      0.38      0.50        16
                                     21: Cardiovascular       0.75      0.60      0.67        10
                              22: Experimental Medicine       0.23      0.17      0.19        18
                                    23: Medical Imaging       0.33      0.11      0.17         9
24: Data Science Computational & Mathematical Modelling       0.54      0.57      0.56        47
                2: Gene Regulation and Genome Integrity       0.75      0.70      0.72        71
                        3: Protein Structure & Function       0.71      0.79      0.75        71
                                        4: Cell Biology       0.56      0.64      0.60        77
                               5: Developmental Biology       0.88      0.25      0.39        28
                                   6: Stem Cell Biology       0.82      0.82      0.82        11
                                          7: Immunology       0.82      0.83      0.83        72
                                            8: Bacteria       0.83      0.63      0.72        46
                                             9: Viruses       0.97      0.81      0.88        42

                                              micro avg       0.72      0.68      0.70       927
                                              macro avg       0.71      0.61      0.64       927
                                           weighted avg       0.73      0.68      0.70       927
                                            samples avg       0.73      0.71      0.68       927
```

## 2020.05.2

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.43      0.60         7
                                          11: Parasites       0.95      0.72      0.82        29
                     12: Brain Cells Circuits & Systems       0.89      0.81      0.85        84
                           13: Sensory & Motor Function       0.91      0.78      0.84        27
                              14: Behaviour & Cognition       0.79      0.84      0.82        58
                      15: Behavioural & Social Sciences       0.40      0.50      0.44        12
                                16: Health Intervention       0.61      0.59      0.60        51
                          17: Health Services & Systems       0.56      0.53      0.55        17
                                       18: Surveillance       0.66      0.71      0.68        35
                 19: Maternal Child & Adolescent Health       0.68      0.62      0.65        21
                                 1: Genetics & Genomics       0.73      0.72      0.73        68
                             20: Nutrition & Metabolism       0.88      0.44      0.58        16
                                     21: Cardiovascular       0.75      0.60      0.67        10
                              22: Experimental Medicine       0.22      0.11      0.15        18
                                    23: Medical Imaging       0.33      0.11      0.17         9
24: Data Science Computational & Mathematical Modelling       0.56      0.60      0.58        47
                2: Gene Regulation and Genome Integrity       0.76      0.68      0.72        71
                        3: Protein Structure & Function       0.69      0.77      0.73        71
                                        4: Cell Biology       0.57      0.69      0.62        77
                               5: Developmental Biology       1.00      0.29      0.44        28
                                   6: Stem Cell Biology       0.82      0.82      0.82        11
                                          7: Immunology       0.87      0.83      0.85        72
                                            8: Bacteria       0.85      0.63      0.72        46
                                             9: Viruses       0.97      0.81      0.88        42

                                              micro avg       0.74      0.68      0.71       927
                                              macro avg       0.73      0.61      0.65       927
                                           weighted avg       0.75      0.68      0.70       927
                                            samples avg       0.73      0.72      0.69       927
```

## 2020.05.3

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.93      0.48      0.64        29
                     12: Brain Cells Circuits & Systems       0.88      0.70      0.78        84
                           13: Sensory & Motor Function       1.00      0.30      0.46        27
                              14: Behaviour & Cognition       0.90      0.66      0.76        58
                      15: Behavioural & Social Sciences       0.00      0.00      0.00        12
                                16: Health Intervention       0.74      0.27      0.40        51
                          17: Health Services & Systems       0.25      0.06      0.10        17
                                       18: Surveillance       0.69      0.26      0.37        35
                 19: Maternal Child & Adolescent Health       1.00      0.38      0.55        21
                                 1: Genetics & Genomics       0.76      0.43      0.55        68
                             20: Nutrition & Metabolism       1.00      0.06      0.12        16
                                     21: Cardiovascular       1.00      0.10      0.18        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.00      0.00      0.00         9
24: Data Science Computational & Mathematical Modelling       0.65      0.36      0.47        47
                2: Gene Regulation and Genome Integrity       0.88      0.61      0.72        71
                        3: Protein Structure & Function       0.81      0.62      0.70        71
                                        4: Cell Biology       0.81      0.38      0.51        77
                               5: Developmental Biology       1.00      0.14      0.25        28
                                   6: Stem Cell Biology       1.00      0.09      0.17        11
                                          7: Immunology       0.84      0.72      0.78        72
                                            8: Bacteria       0.96      0.54      0.69        46
                                             9: Viruses       1.00      0.38      0.55        42

                                              micro avg       0.84      0.45      0.58       927
                                              macro avg       0.71      0.31      0.41       927
                                           weighted avg       0.80      0.45      0.55       927
                                            samples avg       0.72      0.49      0.55       927
```

## 2020.05.4

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.91      0.72      0.81        29
                     12: Brain Cells Circuits & Systems       0.91      0.76      0.83        84
                           13: Sensory & Motor Function       1.00      0.63      0.77        27
                              14: Behaviour & Cognition       0.89      0.81      0.85        58
                      15: Behavioural & Social Sciences       0.40      0.17      0.24        12
                                16: Health Intervention       0.74      0.63      0.68        51
                          17: Health Services & Systems       0.75      0.18      0.29        17
                                       18: Surveillance       0.57      0.46      0.51        35
                 19: Maternal Child & Adolescent Health       0.69      0.52      0.59        21
                                 1: Genetics & Genomics       0.79      0.60      0.68        68
                             20: Nutrition & Metabolism       1.00      0.19      0.32        16
                                     21: Cardiovascular       0.78      0.70      0.74        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.75      0.33      0.46         9
24: Data Science Computational & Mathematical Modelling       0.67      0.43      0.52        47
                2: Gene Regulation and Genome Integrity       0.92      0.48      0.63        71
                        3: Protein Structure & Function       0.77      0.69      0.73        71
                                        4: Cell Biology       0.76      0.51      0.61        77
                               5: Developmental Biology       1.00      0.25      0.40        28
                                   6: Stem Cell Biology       0.00      0.00      0.00        11
                                          7: Immunology       0.94      0.82      0.87        72
                                            8: Bacteria       0.93      0.59      0.72        46
                                             9: Viruses       1.00      0.62      0.76        42

                                              micro avg       0.83      0.57      0.68       927
                                              macro avg       0.72      0.46      0.54       927
                                           weighted avg       0.80      0.57      0.65       927
                                            samples avg       0.81      0.62      0.67       927
```

## 2020.05.5

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       0.96      0.79      0.87        29
                     12: Brain Cells Circuits & Systems       0.88      0.81      0.84        84
                           13: Sensory & Motor Function       0.90      0.70      0.79        27
                              14: Behaviour & Cognition       0.97      0.62      0.76        58
                      15: Behavioural & Social Sciences       0.50      0.25      0.33        12
                                16: Health Intervention       0.77      0.47      0.59        51
                          17: Health Services & Systems       0.44      0.24      0.31        17
                                       18: Surveillance       0.91      0.29      0.43        35
                 19: Maternal Child & Adolescent Health       0.79      0.52      0.63        21
                                 1: Genetics & Genomics       0.76      0.81      0.79        68
                             20: Nutrition & Metabolism       0.88      0.44      0.58        16
                                     21: Cardiovascular       0.82      0.90      0.86        10
                              22: Experimental Medicine       0.29      0.11      0.16        18
                                    23: Medical Imaging       1.00      0.22      0.36         9
24: Data Science Computational & Mathematical Modelling       0.84      0.34      0.48        47
                2: Gene Regulation and Genome Integrity       0.81      0.72      0.76        71
                        3: Protein Structure & Function       0.88      0.65      0.75        71
                                        4: Cell Biology       0.71      0.62      0.66        77
                               5: Developmental Biology       1.00      0.32      0.49        28
                                   6: Stem Cell Biology       1.00      0.55      0.71        11
                                          7: Immunology       0.96      0.74      0.83        72
                                            8: Bacteria       0.93      0.85      0.89        46
                                             9: Viruses       0.94      0.69      0.79        42

                                              micro avg       0.85      0.62      0.71       927
                                              macro avg       0.83      0.55      0.64       927
                                           weighted avg       0.85      0.62      0.70       927
                                            samples avg       0.82      0.67      0.70       927
```

## 2020.05.6

```
                                                         precision    recall  f1-score   support
                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.85      0.38      0.52        29
                     12: Brain Cells Circuits & Systems       0.79      0.76      0.78        84
                           13: Sensory & Motor Function       0.43      0.74      0.54        27
                              14: Behaviour & Cognition       0.72      0.57      0.63        58
                      15: Behavioural & Social Sciences       0.24      0.42      0.30        12
                                16: Health Intervention       0.47      0.82      0.60        51
                          17: Health Services & Systems       0.22      0.76      0.34        17
                                       18: Surveillance       0.38      0.23      0.29        35
                 19: Maternal Child & Adolescent Health       0.69      0.43      0.53        21
                                 1: Genetics & Genomics       0.54      0.74      0.62        68
                             20: Nutrition & Metabolism       0.50      0.38      0.43        16
                                     21: Cardiovascular       0.50      0.20      0.29        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.60      0.67      0.63         9
24: Data Science Computational & Mathematical Modelling       0.75      0.13      0.22        47
                2: Gene Regulation and Genome Integrity       0.65      0.52      0.58        71
                        3: Protein Structure & Function       0.71      0.55      0.62        71
                                        4: Cell Biology       0.49      0.64      0.55        77
                               5: Developmental Biology       0.67      0.29      0.40        28
                                   6: Stem Cell Biology       0.23      0.27      0.25        11
                                          7: Immunology       0.77      0.78      0.77        72
                                            8: Bacteria       0.65      0.67      0.66        46
                                             9: Viruses       0.73      0.64      0.68        42

                                              micro avg       0.57      0.57      0.57       927
                                              macro avg       0.52      0.48      0.47       927
                                           weighted avg       0.61      0.57      0.56       927
                                            samples avg       0.60      0.60      0.56       927

```

## 2020.05.7

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.14      0.25         7
                                          11: Parasites       0.84      0.72      0.78        29
                     12: Brain Cells Circuits & Systems       0.83      0.82      0.83        84
                           13: Sensory & Motor Function       0.72      0.78      0.75        27
                              14: Behaviour & Cognition       0.81      0.81      0.81        58
                      15: Behavioural & Social Sciences       0.21      0.25      0.23        12
                                16: Health Intervention       0.67      0.55      0.60        51
                          17: Health Services & Systems       0.41      0.53      0.46        17
                                       18: Surveillance       0.60      0.51      0.55        35
                 19: Maternal Child & Adolescent Health       0.69      0.52      0.59        21
                                 1: Genetics & Genomics       0.61      0.72      0.66        68
                             20: Nutrition & Metabolism       0.86      0.38      0.52        16
                                     21: Cardiovascular       0.71      0.50      0.59        10
                              22: Experimental Medicine       0.17      0.06      0.08        18
                                    23: Medical Imaging       0.20      0.11      0.14         9
24: Data Science Computational & Mathematical Modelling       0.78      0.53      0.63        47
                2: Gene Regulation and Genome Integrity       0.85      0.63      0.73        71
                        3: Protein Structure & Function       0.69      0.66      0.68        71
                                        4: Cell Biology       0.61      0.49      0.55        77
                               5: Developmental Biology       0.80      0.43      0.56        28
                                   6: Stem Cell Biology       0.86      0.55      0.67        11
                                          7: Immunology       0.86      0.83      0.85        72
                                            8: Bacteria       0.90      0.57      0.69        46
                                             9: Viruses       0.83      0.83      0.83        42

                                              micro avg       0.73      0.63      0.68       927
                                              macro avg       0.69      0.54      0.58       927
                                           weighted avg       0.73      0.63      0.67       927
                                            samples avg       0.73      0.67      0.66       927
```

## 2020.05.8

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.29      0.44         7
                                          11: Parasites       0.81      0.86      0.83        29
                     12: Brain Cells Circuits & Systems       0.79      0.81      0.80        84
                           13: Sensory & Motor Function       0.81      0.78      0.79        27
                              14: Behaviour & Cognition       0.77      0.84      0.80        58
                      15: Behavioural & Social Sciences       0.38      0.25      0.30        12
                                16: Health Intervention       0.68      0.49      0.57        51
                          17: Health Services & Systems       0.43      0.71      0.53        17
                                       18: Surveillance       0.50      0.77      0.61        35
                 19: Maternal Child & Adolescent Health       0.55      0.57      0.56        21
                                 1: Genetics & Genomics       0.63      0.71      0.67        68
                             20: Nutrition & Metabolism       0.64      0.56      0.60        16
                                     21: Cardiovascular       0.57      0.40      0.47        10
                              22: Experimental Medicine       0.19      0.22      0.21        18
                                    23: Medical Imaging       0.40      0.22      0.29         9
24: Data Science Computational & Mathematical Modelling       0.50      0.53      0.52        47
                2: Gene Regulation and Genome Integrity       0.63      0.61      0.62        71
                        3: Protein Structure & Function       0.68      0.72      0.70        71
                                        4: Cell Biology       0.50      0.57      0.53        77
                               5: Developmental Biology       0.70      0.68      0.69        28
                                   6: Stem Cell Biology       0.62      0.45      0.53        11
                                          7: Immunology       0.73      0.71      0.72        72
                                            8: Bacteria       0.86      0.65      0.74        46
                                             9: Viruses       0.76      0.67      0.71        42

                                              micro avg       0.65      0.65      0.65       927
                                              macro avg       0.63      0.59      0.59       927
                                           weighted avg       0.66      0.65      0.65       927
                                            samples avg       0.68      0.69      0.65       927
```

## 2020.05.9

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.29      0.44         7
                                          11: Parasites       0.92      0.76      0.83        29
                     12: Brain Cells Circuits & Systems       0.88      0.82      0.85        84
                           13: Sensory & Motor Function       0.90      0.67      0.77        27
                              14: Behaviour & Cognition       0.81      0.83      0.82        58
                      15: Behavioural & Social Sciences       0.30      0.25      0.27        12
                                16: Health Intervention       0.77      0.53      0.63        51
                          17: Health Services & Systems       0.55      0.35      0.43        17
                                       18: Surveillance       0.67      0.69      0.68        35
                 19: Maternal Child & Adolescent Health       0.67      0.57      0.62        21
                                 1: Genetics & Genomics       0.76      0.65      0.70        68
                             20: Nutrition & Metabolism       0.80      0.50      0.62        16
                                     21: Cardiovascular       0.75      0.60      0.67        10
                              22: Experimental Medicine       0.33      0.33      0.33        18
                                    23: Medical Imaging       0.50      0.33      0.40         9
24: Data Science Computational & Mathematical Modelling       0.81      0.53      0.64        47
                2: Gene Regulation and Genome Integrity       0.85      0.63      0.73        71
                        3: Protein Structure & Function       0.78      0.69      0.73        71
                                        4: Cell Biology       0.62      0.51      0.56        77
                               5: Developmental Biology       0.71      0.54      0.61        28
                                   6: Stem Cell Biology       0.69      0.82      0.75        11
                                          7: Immunology       0.82      0.83      0.83        72
                                            8: Bacteria       0.85      0.72      0.78        46
                                             9: Viruses       0.88      0.83      0.85        42

                                              micro avg       0.77      0.66      0.71       927
                                              macro avg       0.73      0.59      0.65       927
                                           weighted avg       0.77      0.66      0.70       927
                                            samples avg       0.77      0.69      0.69       927
```

## 2020.06.0

```
precision    recall  f1-score   support

           0       1.00      0.71      0.83         7
           1       0.96      0.79      0.87        29
           2       0.89      0.81      0.85        84
           3       0.95      0.74      0.83        27
           4       0.92      0.76      0.83        58
           5       0.43      0.25      0.32        12
           6       0.78      0.55      0.64        51
           7       0.62      0.29      0.40        17
           8       0.92      0.31      0.47        35
           9       0.81      0.62      0.70        21
          10       0.76      0.76      0.76        68
          11       1.00      0.50      0.67        16
          12       0.82      0.90      0.86        10
          13       0.50      0.06      0.10        18
          14       0.75      0.33      0.46         9
          15       0.78      0.38      0.51        47
          16       0.83      0.70      0.76        71
          17       0.82      0.69      0.75        71
          18       0.69      0.61      0.65        77
          19       1.00      0.36      0.53        28
          20       0.80      0.73      0.76        11
          21       0.95      0.78      0.85        72
          22       0.90      0.76      0.82        46
          23       0.94      0.81      0.87        42

   micro avg       0.84      0.65      0.73       927
   macro avg       0.83      0.59      0.67       927
weighted avg       0.84      0.65      0.72       927
 samples avg       0.82      0.69      0.71       927
```

## 2020.06.1

```
precision    recall  f1-score   support

           0       1.00      0.86      0.92         7
           1       0.92      0.83      0.87        29
           2       0.85      0.86      0.85        84
           3       0.81      0.78      0.79        27
           4       0.81      0.86      0.83        58
           5       0.42      0.42      0.42        12
           6       0.67      0.73      0.70        51
           7       0.50      0.65      0.56        17
           8       0.69      0.71      0.70        35
           9       0.61      0.67      0.64        21
          10       0.69      0.87      0.77        68
          11       0.67      0.62      0.65        16
          12       0.75      0.90      0.82        10
          13       0.33      0.17      0.22        18
          14       0.60      0.33      0.43         9
          15       0.64      0.62      0.63        47
          16       0.75      0.77      0.76        71
          17       0.75      0.80      0.78        71
          18       0.60      0.77      0.67        77
          19       0.92      0.43      0.59        28
          20       0.85      1.00      0.92        11
          21       0.87      0.85      0.86        72
          22       0.83      0.85      0.84        46
          23       0.88      0.88      0.88        42

   micro avg       0.74      0.76      0.75       927
   macro avg       0.73      0.72      0.71       927
weighted avg       0.75      0.76      0.75       927
 samples avg       0.77      0.80      0.75       927
```

## 2020.06.2

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       0.83      0.83      0.83        29
                     12: Brain Cells Circuits & Systems       0.90      0.68      0.78        84
                           13: Sensory & Motor Function       0.68      0.48      0.57        27
                              14: Behaviour & Cognition       0.73      0.66      0.69        58
                      15: Behavioural & Social Sciences       0.45      0.42      0.43        12
                                16: Health Intervention       0.60      0.47      0.53        51
                          17: Health Services & Systems       0.44      0.47      0.46        17
                                       18: Surveillance       0.50      0.51      0.51        35
                 19: Maternal Child & Adolescent Health       0.50      0.43      0.46        21
                                 1: Genetics & Genomics       0.73      0.68      0.70        68
                             20: Nutrition & Metabolism       0.36      0.25      0.30        16
                                     21: Cardiovascular       0.70      0.70      0.70        10
                              22: Experimental Medicine       0.25      0.11      0.15        18
                                    23: Medical Imaging       0.67      0.22      0.33         9
24: Data Science Computational & Mathematical Modelling       0.62      0.38      0.47        47
                2: Gene Regulation and Genome Integrity       0.77      0.56      0.65        71
                        3: Protein Structure & Function       0.80      0.61      0.69        71
                                        4: Cell Biology       0.55      0.47      0.50        77
                               5: Developmental Biology       0.78      0.25      0.38        28
                                   6: Stem Cell Biology       0.78      0.64      0.70        11
                                          7: Immunology       0.77      0.67      0.72        72
                                            8: Bacteria       0.85      0.63      0.72        46
                                             9: Viruses       0.88      0.71      0.79        42

                                              micro avg       0.71      0.56      0.62       927
                                              macro avg       0.67      0.52      0.57       927
                                           weighted avg       0.71      0.56      0.62       927
                                            samples avg       0.68      0.58      0.59       927
```

## 2020.06.3

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.71      0.83         7
                                          11: Parasites       0.92      0.79      0.85        29
                     12: Brain Cells Circuits & Systems       0.89      0.81      0.85        84
                           13: Sensory & Motor Function       0.76      0.59      0.67        27
                              14: Behaviour & Cognition       0.88      0.66      0.75        58
                      15: Behavioural & Social Sciences       0.38      0.25      0.30        12
                                16: Health Intervention       0.67      0.39      0.49        51
                          17: Health Services & Systems       0.50      0.35      0.41        17
                                       18: Surveillance       0.79      0.43      0.56        35
                 19: Maternal Child & Adolescent Health       0.69      0.52      0.59        21
                                 1: Genetics & Genomics       0.79      0.56      0.66        68
                             20: Nutrition & Metabolism       0.44      0.44      0.44        16
                                     21: Cardiovascular       0.70      0.70      0.70        10
                              22: Experimental Medicine       0.13      0.11      0.12        18
                                    23: Medical Imaging       0.33      0.11      0.17         9
24: Data Science Computational & Mathematical Modelling       0.75      0.51      0.61        47
                2: Gene Regulation and Genome Integrity       0.80      0.55      0.65        71
                        3: Protein Structure & Function       0.85      0.70      0.77        71
                                        4: Cell Biology       0.67      0.38      0.48        77
                               5: Developmental Biology       0.73      0.29      0.41        28
                                   6: Stem Cell Biology       0.78      0.64      0.70        11
                                          7: Immunology       0.84      0.68      0.75        72
                                            8: Bacteria       0.82      0.59      0.68        46
                                             9: Viruses       0.93      0.67      0.78        42

                                              micro avg       0.78      0.56      0.65       927
                                              macro avg       0.71      0.52      0.59       927
                                           weighted avg       0.77      0.56      0.64       927
                                            samples avg       0.73      0.59      0.62       927
```

## 2020.10.0

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.71      0.83         7
                                          11: Parasites       1.00      0.72      0.84        29
                     12: Brain Cells Circuits & Systems       0.91      0.82      0.86        84
                           13: Sensory & Motor Function       0.81      0.78      0.79        27
                              14: Behaviour & Cognition       0.84      0.88      0.86        58
                      15: Behavioural & Social Sciences       0.36      0.42      0.38        12
                                16: Health Intervention       0.66      0.65      0.65        51
                          17: Health Services & Systems       0.56      0.59      0.57        17
                                       18: Surveillance       0.64      0.71      0.68        35
                 19: Maternal Child & Adolescent Health       0.72      0.62      0.67        21
                                 1: Genetics & Genomics       0.71      0.71      0.71        68
                             20: Nutrition & Metabolism       0.75      0.38      0.50        16
                                     21: Cardiovascular       0.73      0.80      0.76        10
                              22: Experimental Medicine       0.18      0.11      0.14        18
                                    23: Medical Imaging       0.50      0.22      0.31         9
24: Data Science Computational & Mathematical Modelling       0.59      0.57      0.58        47
                2: Gene Regulation and Genome Integrity       0.82      0.66      0.73        71
                        3: Protein Structure & Function       0.78      0.76      0.77        71
                                        4: Cell Biology       0.55      0.71      0.62        77
                               5: Developmental Biology       0.81      0.46      0.59        28
                                   6: Stem Cell Biology       0.75      0.82      0.78        11
                                          7: Immunology       0.85      0.83      0.84        72
                                            8: Bacteria       0.92      0.72      0.80        46
                                             9: Viruses       0.97      0.71      0.82        42

                                              micro avg       0.75      0.70      0.72       927
                                              macro avg       0.72      0.64      0.67       927
                                           weighted avg       0.76      0.70      0.72       927
                                            samples avg       0.75      0.73      0.71       927
```

## 2020.10.1

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.71      0.83         7
                                          11: Parasites       1.00      0.72      0.84        29
                     12: Brain Cells Circuits & Systems       0.91      0.83      0.87        84
                           13: Sensory & Motor Function       0.81      0.78      0.79        27
                              14: Behaviour & Cognition       0.82      0.86      0.84        58
                      15: Behavioural & Social Sciences       0.38      0.42      0.40        12
                                16: Health Intervention       0.65      0.63      0.64        51
                          17: Health Services & Systems       0.53      0.53      0.53        17
                                       18: Surveillance       0.65      0.69      0.67        35
                 19: Maternal Child & Adolescent Health       0.76      0.62      0.68        21
                                 1: Genetics & Genomics       0.66      0.69      0.68        68
                             20: Nutrition & Metabolism       0.62      0.31      0.42        16
                                     21: Cardiovascular       0.75      0.90      0.82        10
                              22: Experimental Medicine       0.20      0.11      0.14        18
                                    23: Medical Imaging       0.50      0.22      0.31         9
24: Data Science Computational & Mathematical Modelling       0.60      0.55      0.58        47
                2: Gene Regulation and Genome Integrity       0.81      0.68      0.74        71
                        3: Protein Structure & Function       0.77      0.76      0.77        71
                                        4: Cell Biology       0.58      0.74      0.65        77
                               5: Developmental Biology       0.80      0.43      0.56        28
                                   6: Stem Cell Biology       0.73      0.73      0.73        11
                                          7: Immunology       0.86      0.82      0.84        72
                                            8: Bacteria       0.94      0.70      0.80        46
                                             9: Viruses       0.97      0.71      0.82        42

                                              micro avg       0.75      0.69      0.72       927
                                              macro avg       0.72      0.63      0.66       927
                                           weighted avg       0.75      0.69      0.71       927
                                            samples avg       0.75      0.73      0.70       927
```

## 2020.10.2

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       1.00      0.69      0.82        29
                     12: Brain Cells Circuits & Systems       0.90      0.76      0.83        84
                           13: Sensory & Motor Function       0.87      0.74      0.80        27
                              14: Behaviour & Cognition       0.81      0.76      0.79        58
                      15: Behavioural & Social Sciences       0.31      0.33      0.32        12
                                16: Health Intervention       0.67      0.61      0.64        51
                          17: Health Services & Systems       0.50      0.47      0.48        17
                                       18: Surveillance       0.62      0.60      0.61        35
                 19: Maternal Child & Adolescent Health       0.67      0.57      0.62        21
                                 1: Genetics & Genomics       0.69      0.68      0.68        68
                             20: Nutrition & Metabolism       0.78      0.44      0.56        16
                                     21: Cardiovascular       0.83      0.50      0.62        10
                              22: Experimental Medicine       0.25      0.11      0.15        18
                                    23: Medical Imaging       0.50      0.11      0.18         9
24: Data Science Computational & Mathematical Modelling       0.62      0.60      0.61        47
                2: Gene Regulation and Genome Integrity       0.79      0.63      0.70        71
                        3: Protein Structure & Function       0.74      0.76      0.75        71
                                        4: Cell Biology       0.60      0.68      0.64        77
                               5: Developmental Biology       0.89      0.29      0.43        28
                                   6: Stem Cell Biology       0.90      0.82      0.86        11
                                          7: Immunology       0.87      0.75      0.81        72
                                            8: Bacteria       0.93      0.61      0.74        46
                                             9: Viruses       0.97      0.74      0.84        42

                                              micro avg       0.75      0.65      0.69       927
                                              macro avg       0.74      0.58      0.63       927
                                           weighted avg       0.76      0.65      0.69       927
                                            samples avg       0.73      0.68      0.67       927
```

## 2020.10.3

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       1.00      0.69      0.82        29
                     12: Brain Cells Circuits & Systems       0.93      0.79      0.85        84
                           13: Sensory & Motor Function       0.83      0.70      0.76        27
                              14: Behaviour & Cognition       0.80      0.76      0.78        58
                      15: Behavioural & Social Sciences       0.33      0.33      0.33        12
                                16: Health Intervention       0.68      0.63      0.65        51
                          17: Health Services & Systems       0.47      0.41      0.44        17
                                       18: Surveillance       0.64      0.60      0.62        35
                 19: Maternal Child & Adolescent Health       0.71      0.57      0.63        21
                                 1: Genetics & Genomics       0.69      0.69      0.69        68
                             20: Nutrition & Metabolism       0.70      0.44      0.54        16
                                     21: Cardiovascular       0.80      0.40      0.53        10
                              22: Experimental Medicine       0.29      0.11      0.16        18
                                    23: Medical Imaging       0.50      0.11      0.18         9
24: Data Science Computational & Mathematical Modelling       0.61      0.53      0.57        47
                2: Gene Regulation and Genome Integrity       0.76      0.62      0.68        71
                        3: Protein Structure & Function       0.73      0.77      0.75        71
                                        4: Cell Biology       0.59      0.66      0.62        77
                               5: Developmental Biology       0.89      0.29      0.43        28
                                   6: Stem Cell Biology       0.89      0.73      0.80        11
                                          7: Immunology       0.88      0.78      0.82        72
                                            8: Bacteria       0.93      0.59      0.72        46
                                             9: Viruses       0.97      0.74      0.84        42

                                              micro avg       0.75      0.64      0.69       927
                                              macro avg       0.73      0.56      0.62       927
                                           weighted avg       0.76      0.64      0.69       927
                                            samples avg       0.73      0.68      0.67       927
```

## 2020.10.4

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.29      0.44         7
                                          11: Parasites       1.00      0.59      0.74        29
                     12: Brain Cells Circuits & Systems       0.85      0.55      0.67        84
                           13: Sensory & Motor Function       0.80      0.44      0.57        27
                              14: Behaviour & Cognition       0.84      0.55      0.67        58
                      15: Behavioural & Social Sciences       0.38      0.25      0.30        12
                                16: Health Intervention       0.77      0.45      0.57        51
                          17: Health Services & Systems       0.44      0.24      0.31        17
                                       18: Surveillance       0.56      0.26      0.35        35
                 19: Maternal Child & Adolescent Health       0.91      0.48      0.62        21
                                 1: Genetics & Genomics       0.81      0.37      0.51        68
                             20: Nutrition & Metabolism       0.80      0.25      0.38        16
                                     21: Cardiovascular       0.75      0.30      0.43        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       1.00      0.11      0.20         9
24: Data Science Computational & Mathematical Modelling       0.58      0.15      0.24        47
                2: Gene Regulation and Genome Integrity       0.84      0.38      0.52        71
                        3: Protein Structure & Function       0.69      0.49      0.57        71
                                        4: Cell Biology       0.42      0.35      0.38        77
                               5: Developmental Biology       0.67      0.21      0.32        28
                                   6: Stem Cell Biology       1.00      0.18      0.31        11
                                          7: Immunology       0.83      0.49      0.61        72
                                            8: Bacteria       0.85      0.50      0.63        46
                                             9: Viruses       0.95      0.48      0.63        42

                                              micro avg       0.74      0.40      0.52       927
                                              macro avg       0.74      0.35      0.46       927
                                           weighted avg       0.74      0.40      0.51       927
                                            samples avg       0.60      0.43      0.47       927
```

## 2020.10.5

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       0.96      0.79      0.87        29
                     12: Brain Cells Circuits & Systems       0.91      0.76      0.83        84
                           13: Sensory & Motor Function       0.78      0.67      0.72        27
                              14: Behaviour & Cognition       0.81      0.81      0.81        58
                      15: Behavioural & Social Sciences       0.50      0.42      0.45        12
                                16: Health Intervention       0.72      0.57      0.64        51
                          17: Health Services & Systems       0.62      0.47      0.53        17
                                       18: Surveillance       0.64      0.60      0.62        35
                 19: Maternal Child & Adolescent Health       0.76      0.62      0.68        21
                                 1: Genetics & Genomics       0.70      0.57      0.63        68
                             20: Nutrition & Metabolism       0.71      0.31      0.43        16
                                     21: Cardiovascular       0.73      0.80      0.76        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.50      0.11      0.18         9
24: Data Science Computational & Mathematical Modelling       0.45      0.43      0.44        47
                2: Gene Regulation and Genome Integrity       0.84      0.59      0.69        71
                        3: Protein Structure & Function       0.79      0.63      0.70        71
                                        4: Cell Biology       0.52      0.64      0.57        77
                               5: Developmental Biology       0.69      0.32      0.44        28
                                   6: Stem Cell Biology       0.86      0.55      0.67        11
                                          7: Immunology       0.83      0.76      0.80        72
                                            8: Bacteria       0.90      0.61      0.73        46
                                             9: Viruses       0.96      0.62      0.75        42

                                              micro avg       0.74      0.61      0.67       927
                                              macro avg       0.72      0.55      0.61       927
                                           weighted avg       0.74      0.61      0.66       927
                                            samples avg       0.71      0.64      0.64       927
```

## 2020.10.6

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.29      0.44         7
                                          11: Parasites       1.00      0.55      0.71        29
                     12: Brain Cells Circuits & Systems       0.93      0.62      0.74        84
                           13: Sensory & Motor Function       0.71      0.37      0.49        27
                              14: Behaviour & Cognition       0.76      0.53      0.63        58
                      15: Behavioural & Social Sciences       0.38      0.25      0.30        12
                                16: Health Intervention       0.77      0.45      0.57        51
                          17: Health Services & Systems       0.44      0.24      0.31        17
                                       18: Surveillance       0.53      0.26      0.35        35
                 19: Maternal Child & Adolescent Health       0.88      0.33      0.48        21
                                 1: Genetics & Genomics       0.76      0.46      0.57        68
                             20: Nutrition & Metabolism       0.80      0.25      0.38        16
                                     21: Cardiovascular       0.80      0.40      0.53        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       1.00      0.11      0.20         9
24: Data Science Computational & Mathematical Modelling       0.28      0.53      0.37        47
                2: Gene Regulation and Genome Integrity       0.79      0.42      0.55        71
                        3: Protein Structure & Function       0.67      0.55      0.60        71
                                        4: Cell Biology       0.51      0.40      0.45        77
                               5: Developmental Biology       0.67      0.21      0.32        28
                                   6: Stem Cell Biology       0.50      0.27      0.35        11
                                          7: Immunology       0.84      0.60      0.70        72
                                            8: Bacteria       0.81      0.46      0.58        46
                                             9: Viruses       0.95      0.45      0.61        42

                                              micro avg       0.68      0.45      0.54       927
                                              macro avg       0.70      0.38      0.47       927
                                           weighted avg       0.72      0.45      0.54       927
                                            samples avg       0.58      0.49      0.49       927
```

## 2020.10.7

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.11      0.14      0.12         7
                                          11: Parasites       0.45      0.69      0.55        29
                     12: Brain Cells Circuits & Systems       0.52      0.71      0.60        84
                           13: Sensory & Motor Function       0.29      0.56      0.38        27
                              14: Behaviour & Cognition       0.53      0.69      0.60        58
                      15: Behavioural & Social Sciences       0.18      0.50      0.27        12
                                16: Health Intervention       0.33      0.53      0.40        51
                          17: Health Services & Systems       0.15      0.29      0.20        17
                                       18: Surveillance       0.28      0.66      0.39        35
                 19: Maternal Child & Adolescent Health       0.30      0.43      0.35        21
                                 1: Genetics & Genomics       0.43      0.68      0.53        68
                             20: Nutrition & Metabolism       0.18      0.19      0.18        16
                                     21: Cardiovascular       0.15      0.40      0.22        10
                              22: Experimental Medicine       0.07      0.17      0.10        18
                                    23: Medical Imaging       0.29      0.22      0.25         9
24: Data Science Computational & Mathematical Modelling       0.18      0.38      0.24        47
                2: Gene Regulation and Genome Integrity       0.42      0.54      0.47        71
                        3: Protein Structure & Function       0.45      0.76      0.56        71
                                        4: Cell Biology       0.43      0.68      0.53        77
                               5: Developmental Biology       0.25      0.46      0.32        28
                                   6: Stem Cell Biology       0.23      0.45      0.30        11
                                          7: Immunology       0.47      0.71      0.56        72
                                            8: Bacteria       0.39      0.67      0.49        46
                                             9: Viruses       0.55      0.67      0.60        42

                                              micro avg       0.37      0.60      0.46       927
                                              macro avg       0.32      0.51      0.38       927
                                           weighted avg       0.39      0.60      0.47       927
                                            samples avg       0.40      0.62      0.46       927
```

## 2020.10.8

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.29      0.44         7
                                          11: Parasites       1.00      0.48      0.65        29
                     12: Brain Cells Circuits & Systems       0.82      0.49      0.61        84
                           13: Sensory & Motor Function       0.83      0.37      0.51        27
                              14: Behaviour & Cognition       0.82      0.40      0.53        58
                      15: Behavioural & Social Sciences       0.29      0.17      0.21        12
                                16: Health Intervention       0.73      0.37      0.49        51
                          17: Health Services & Systems       0.33      0.18      0.23        17
                                       18: Surveillance       0.62      0.29      0.39        35
                 19: Maternal Child & Adolescent Health       1.00      0.57      0.73        21
                                 1: Genetics & Genomics       0.76      0.37      0.50        68
                             20: Nutrition & Metabolism       0.80      0.25      0.38        16
                                     21: Cardiovascular       0.67      0.20      0.31        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       1.00      0.11      0.20         9
24: Data Science Computational & Mathematical Modelling       0.50      0.11      0.18        47
                2: Gene Regulation and Genome Integrity       0.85      0.31      0.45        71
                        3: Protein Structure & Function       0.72      0.48      0.58        71
                                        4: Cell Biology       0.47      0.38      0.42        77
                               5: Developmental Biology       1.00      0.14      0.25        28
                                   6: Stem Cell Biology       0.75      0.27      0.40        11
                                          7: Immunology       0.93      0.38      0.53        72
                                            8: Bacteria       0.86      0.41      0.56        46
                                             9: Viruses       0.90      0.43      0.58        42

                                              micro avg       0.74      0.35      0.48       927
                                              macro avg       0.74      0.31      0.42       927
                                           weighted avg       0.75      0.35      0.47       927
                                            samples avg       0.56      0.38      0.43       927
```

## 2020.10.9

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       0.96      0.79      0.87        29
                     12: Brain Cells Circuits & Systems       0.93      0.80      0.86        84
                           13: Sensory & Motor Function       0.83      0.56      0.67        27
                              14: Behaviour & Cognition       0.82      0.78      0.80        58
                      15: Behavioural & Social Sciences       0.36      0.33      0.35        12
                                16: Health Intervention       0.72      0.55      0.62        51
                          17: Health Services & Systems       0.40      0.35      0.38        17
                                       18: Surveillance       0.62      0.46      0.52        35
                 19: Maternal Child & Adolescent Health       0.83      0.71      0.77        21
                                 1: Genetics & Genomics       0.78      0.57      0.66        68
                             20: Nutrition & Metabolism       0.86      0.38      0.52        16
                                     21: Cardiovascular       0.70      0.70      0.70        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.50      0.11      0.18         9
24: Data Science Computational & Mathematical Modelling       0.50      0.26      0.34        47
                2: Gene Regulation and Genome Integrity       0.83      0.55      0.66        71
                        3: Protein Structure & Function       0.77      0.62      0.69        71
                                        4: Cell Biology       0.51      0.60      0.55        77
                               5: Developmental Biology       0.85      0.39      0.54        28
                                   6: Stem Cell Biology       0.88      0.64      0.74        11
                                          7: Immunology       0.84      0.71      0.77        72
                                            8: Bacteria       0.90      0.61      0.73        46
                                             9: Viruses       0.96      0.62      0.75        42

                                              micro avg       0.75      0.58      0.66       927
                                              macro avg       0.72      0.53      0.60       927
                                           weighted avg       0.76      0.58      0.65       927
                                            samples avg       0.70      0.62      0.62       927
```

## 2020.10.10

```
                                                        precision    recall  f1-score   support

                                              10: Fungi       1.00      0.29      0.44         7
                                          11: Parasites       1.00      0.52      0.68        29
                     12: Brain Cells Circuits & Systems       0.90      0.56      0.69        84
                           13: Sensory & Motor Function       0.77      0.37      0.50        27
                              14: Behaviour & Cognition       0.76      0.43      0.55        58
                      15: Behavioural & Social Sciences       0.17      0.08      0.11        12
                                16: Health Intervention       0.81      0.33      0.47        51
                          17: Health Services & Systems       0.33      0.18      0.23        17
                                       18: Surveillance       0.67      0.29      0.40        35
                 19: Maternal Child & Adolescent Health       0.92      0.57      0.71        21
                                 1: Genetics & Genomics       0.76      0.46      0.57        68
                             20: Nutrition & Metabolism       0.75      0.19      0.30        16
                                     21: Cardiovascular       0.67      0.20      0.31        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       1.00      0.11      0.20         9
24: Data Science Computational & Mathematical Modelling       0.41      0.19      0.26        47
                2: Gene Regulation and Genome Integrity       0.85      0.41      0.55        71
                        3: Protein Structure & Function       0.70      0.54      0.61        71
                                        4: Cell Biology       0.50      0.35      0.41        77
                               5: Developmental Biology       0.83      0.18      0.29        28
                                   6: Stem Cell Biology       0.50      0.27      0.35        11
                                          7: Immunology       0.93      0.51      0.66        72
                                            8: Bacteria       0.83      0.41      0.55        46
                                             9: Viruses       1.00      0.48      0.65        42

                                              micro avg       0.75      0.39      0.52       927
                                              macro avg       0.71      0.33      0.44       927
                                           weighted avg       0.75      0.39      0.51       927
                                            samples avg       0.58      0.43      0.46       927
```

## 2020.10.11

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       0.88      0.76      0.81        29
                     12: Brain Cells Circuits & Systems       0.85      0.83      0.84        84
                           13: Sensory & Motor Function       0.79      0.70      0.75        27
                              14: Behaviour & Cognition       0.82      0.78      0.80        58
                      15: Behavioural & Social Sciences       0.23      0.25      0.24        12
                                16: Health Intervention       0.64      0.57      0.60        51
                          17: Health Services & Systems       0.40      0.35      0.38        17
                                       18: Surveillance       0.47      0.60      0.52        35
                 19: Maternal Child & Adolescent Health       0.75      0.71      0.73        21
                                 1: Genetics & Genomics       0.60      0.74      0.66        68
                             20: Nutrition & Metabolism       0.75      0.38      0.50        16
                                     21: Cardiovascular       0.75      0.60      0.67        10
                              22: Experimental Medicine       0.00      0.00      0.00        18
                                    23: Medical Imaging       0.33      0.11      0.17         9
24: Data Science Computational & Mathematical Modelling       0.42      0.47      0.44        47
                2: Gene Regulation and Genome Integrity       0.80      0.72      0.76        71
                        3: Protein Structure & Function       0.70      0.70      0.70        71
                                        4: Cell Biology       0.53      0.70      0.60        77
                               5: Developmental Biology       0.76      0.46      0.58        28
                                   6: Stem Cell Biology       0.80      0.73      0.76        11
                                          7: Immunology       0.76      0.75      0.76        72
                                            8: Bacteria       0.85      0.63      0.72        46
                                             9: Viruses       0.96      0.60      0.74        42

                                              micro avg       0.67      0.65      0.66       927
                                              macro avg       0.66      0.57      0.60       927
                                           weighted avg       0.69      0.65      0.66       927
                                            samples avg       0.68      0.68      0.64       927
```

## 2020.10.12

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         7
                                          11: Parasites       0.63      0.66      0.64        29
                     12: Brain Cells Circuits & Systems       0.68      0.71      0.70        84
                           13: Sensory & Motor Function       0.41      0.59      0.48        27
                              14: Behaviour & Cognition       0.66      0.64      0.65        58
                      15: Behavioural & Social Sciences       0.29      0.42      0.34        12
                                16: Health Intervention       0.50      0.63      0.56        51
                          17: Health Services & Systems       0.21      0.29      0.24        17
                                       18: Surveillance       0.35      0.54      0.42        35
                 19: Maternal Child & Adolescent Health       0.40      0.48      0.43        21
                                 1: Genetics & Genomics       0.54      0.71      0.61        68
                             20: Nutrition & Metabolism       0.38      0.31      0.34        16
                                     21: Cardiovascular       0.56      0.50      0.53        10
                              22: Experimental Medicine       0.03      0.06      0.04        18
                                    23: Medical Imaging       0.38      0.33      0.35         9
24: Data Science Computational & Mathematical Modelling       0.22      0.38      0.28        47
                2: Gene Regulation and Genome Integrity       0.55      0.55      0.55        71
                        3: Protein Structure & Function       0.46      0.58      0.51        71
                                        4: Cell Biology       0.45      0.70      0.55        77
                               5: Developmental Biology       0.45      0.46      0.46        28
                                   6: Stem Cell Biology       0.50      0.36      0.42        11
                                          7: Immunology       0.63      0.65      0.64        72
                                            8: Bacteria       0.54      0.67      0.60        46
                                             9: Viruses       0.62      0.60      0.61        42

                                              micro avg       0.48      0.58      0.52       927
                                              macro avg       0.44      0.49      0.46       927
                                           weighted avg       0.50      0.58      0.53       927
                                            samples avg       0.51      0.60      0.52       927
```

## 2020.10.13

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.71      0.83         7
                                          11: Parasites       0.88      0.76      0.81        29
                     12: Brain Cells Circuits & Systems       0.90      0.82      0.86        84
                           13: Sensory & Motor Function       0.78      0.78      0.78        27
                              14: Behaviour & Cognition       0.81      0.90      0.85        58
                      15: Behavioural & Social Sciences       0.47      0.58      0.52        12
                                16: Health Intervention       0.69      0.67      0.68        51
                          17: Health Services & Systems       0.60      0.53      0.56        17
                                       18: Surveillance       0.56      0.80      0.66        35
                 19: Maternal Child & Adolescent Health       0.67      0.67      0.67        21
                                 1: Genetics & Genomics       0.68      0.75      0.71        68
                             20: Nutrition & Metabolism       0.88      0.44      0.58        16
                                     21: Cardiovascular       0.75      0.90      0.82        10
                              22: Experimental Medicine       0.15      0.11      0.13        18
                                    23: Medical Imaging       0.67      0.22      0.33         9
24: Data Science Computational & Mathematical Modelling       0.51      0.62      0.56        47
                2: Gene Regulation and Genome Integrity       0.78      0.73      0.75        71
                        3: Protein Structure & Function       0.75      0.77      0.76        71
                                        4: Cell Biology       0.55      0.75      0.63        77
                               5: Developmental Biology       0.79      0.39      0.52        28
                                   6: Stem Cell Biology       0.73      0.73      0.73        11
                                          7: Immunology       0.83      0.86      0.84        72
                                            8: Bacteria       0.87      0.72      0.79        46
                                             9: Viruses       0.95      0.83      0.89        42

                                              micro avg       0.72      0.73      0.72       927
                                              macro avg       0.72      0.67      0.68       927
                                           weighted avg       0.73      0.73      0.72       927
                                            samples avg       0.73      0.76      0.71       927
```

## 2020.10.14

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.57      0.73         7
                                          11: Parasites       0.88      0.76      0.81        29
                     12: Brain Cells Circuits & Systems       0.88      0.82      0.85        84
                           13: Sensory & Motor Function       0.78      0.78      0.78        27
                              14: Behaviour & Cognition       0.80      0.91      0.85        58
                      15: Behavioural & Social Sciences       0.50      0.67      0.57        12
                                16: Health Intervention       0.67      0.67      0.67        51
                          17: Health Services & Systems       0.60      0.53      0.56        17
                                       18: Surveillance       0.56      0.77      0.65        35
                 19: Maternal Child & Adolescent Health       0.67      0.67      0.67        21
                                 1: Genetics & Genomics       0.69      0.74      0.71        68
                             20: Nutrition & Metabolism       0.78      0.44      0.56        16
                                     21: Cardiovascular       0.75      0.90      0.82        10
                              22: Experimental Medicine       0.15      0.11      0.13        18
                                    23: Medical Imaging       0.67      0.22      0.33         9
24: Data Science Computational & Mathematical Modelling       0.56      0.62      0.59        47
                2: Gene Regulation and Genome Integrity       0.78      0.70      0.74        71
                        3: Protein Structure & Function       0.74      0.77      0.76        71
                                        4: Cell Biology       0.54      0.74      0.62        77
                               5: Developmental Biology       0.79      0.39      0.52        28
                                   6: Stem Cell Biology       0.73      0.73      0.73        11
                                          7: Immunology       0.84      0.86      0.85        72
                                            8: Bacteria       0.87      0.72      0.79        46
                                             9: Viruses       0.97      0.83      0.90        42

                                              micro avg       0.72      0.72      0.72       927
                                              macro avg       0.72      0.66      0.67       927
                                           weighted avg       0.73      0.72      0.72       927
                                            samples avg       0.73      0.76      0.71       927
```

## 2020.10.15

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.43      0.60         7
                                          11: Parasites       0.95      0.72      0.82        29
                     12: Brain Cells Circuits & Systems       0.91      0.82      0.86        84
                           13: Sensory & Motor Function       0.88      0.78      0.82        27
                              14: Behaviour & Cognition       0.80      0.84      0.82        58
                      15: Behavioural & Social Sciences       0.40      0.50      0.44        12
                                16: Health Intervention       0.61      0.59      0.60        51
                          17: Health Services & Systems       0.56      0.53      0.55        17
                                       18: Surveillance       0.62      0.71      0.67        35
                 19: Maternal Child & Adolescent Health       0.68      0.62      0.65        21
                                 1: Genetics & Genomics       0.71      0.71      0.71        68
                             20: Nutrition & Metabolism       0.78      0.44      0.56        16
                                     21: Cardiovascular       0.88      0.70      0.78        10
                              22: Experimental Medicine       0.25      0.11      0.15        18
                                    23: Medical Imaging       0.33      0.11      0.17         9
24: Data Science Computational & Mathematical Modelling       0.56      0.64      0.59        47
                2: Gene Regulation and Genome Integrity       0.76      0.72      0.74        71
                        3: Protein Structure & Function       0.70      0.77      0.73        71
                                        4: Cell Biology       0.59      0.69      0.63        77
                               5: Developmental Biology       0.82      0.32      0.46        28
                                   6: Stem Cell Biology       0.82      0.82      0.82        11
                                          7: Immunology       0.86      0.82      0.84        72
                                            8: Bacteria       0.88      0.65      0.75        46
                                             9: Viruses       0.94      0.81      0.87        42

                                              micro avg       0.74      0.69      0.71       927
                                              macro avg       0.72      0.62      0.65       927
                                           weighted avg       0.74      0.69      0.71       927
                                            samples avg       0.74      0.72      0.69       927
```

## 2020.10.16

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.20      0.33         5
                                          11: Parasites       0.90      0.75      0.82        24
                     12: Brain Cells Circuits & Systems       0.84      0.84      0.84        74
                           13: Sensory & Motor Function       0.86      0.69      0.77        26
                              14: Behaviour & Cognition       0.70      0.82      0.76        51
                      15: Behavioural & Social Sciences       0.48      0.52      0.50        21
                                16: Health Intervention       0.67      0.69      0.68        54
                          17: Health Services & Systems       0.93      0.78      0.85        32
                                       18: Surveillance       0.49      0.82      0.62        34
                 19: Maternal Child & Adolescent Health       0.83      0.63      0.72        30
                                 1: Genetics & Genomics       0.61      0.56      0.58        61
                             20: Nutrition & Metabolism       0.64      0.47      0.54        15
                                     21: Cardiovascular       0.86      0.38      0.52        16
                              22: Experimental Medicine       0.20      0.14      0.17        21
                                    23: Medical Imaging       0.50      0.33      0.40         6
24: Data Science Computational & Mathematical Modelling       0.54      0.68      0.60        38
                2: Gene Regulation and Genome Integrity       0.78      0.70      0.74        71
                        3: Protein Structure & Function       0.82      0.80      0.81        81
                                        4: Cell Biology       0.61      0.76      0.67        79
                               5: Developmental Biology       0.70      0.77      0.73        30
                                   6: Stem Cell Biology       0.89      0.53      0.67        15
                                          7: Immunology       0.75      0.82      0.78        72
                                            8: Bacteria       0.89      0.63      0.74        49
                                             9: Viruses       0.86      0.71      0.78        45

                                              micro avg       0.71      0.70      0.71       950
                                              macro avg       0.72      0.63      0.65       950
                                           weighted avg       0.73      0.70      0.71       950
                                            samples avg       0.74      0.74      0.71       950
```

## 2020.10.17

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       1.00      0.20      0.33         5
                                          11: Parasites       0.74      0.71      0.72        24
                     12: Brain Cells Circuits & Systems       0.86      0.80      0.83        74
                           13: Sensory & Motor Function       0.87      0.50      0.63        26
                              14: Behaviour & Cognition       0.74      0.78      0.76        51
                      15: Behavioural & Social Sciences       0.44      0.38      0.41        21
                                16: Health Intervention       0.70      0.65      0.67        54
                          17: Health Services & Systems       0.67      0.69      0.68        32
                                       18: Surveillance       0.60      0.62      0.61        34
                 19: Maternal Child & Adolescent Health       0.68      0.57      0.62        30
                                 1: Genetics & Genomics       0.56      0.56      0.56        61
                             20: Nutrition & Metabolism       0.67      0.40      0.50        15
                                     21: Cardiovascular       1.00      0.38      0.55        16
                              22: Experimental Medicine       0.27      0.14      0.19        21
                                    23: Medical Imaging       0.50      0.33      0.40         6
24: Data Science Computational & Mathematical Modelling       0.62      0.61      0.61        38
                2: Gene Regulation and Genome Integrity       0.79      0.68      0.73        71
                        3: Protein Structure & Function       0.82      0.78      0.80        81
                                        4: Cell Biology       0.62      0.77      0.69        79
                               5: Developmental Biology       0.89      0.57      0.69        30
                                   6: Stem Cell Biology       0.86      0.40      0.55        15
                                          7: Immunology       0.81      0.75      0.78        72
                                            8: Bacteria       0.93      0.57      0.71        49
                                             9: Viruses       0.82      0.71      0.76        45

                                              micro avg       0.72      0.65      0.68       950
                                              macro avg       0.73      0.56      0.62       950
                                           weighted avg       0.74      0.65      0.68       950
                                            samples avg       0.74      0.69      0.67       950
```

## 2021.03.0

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         5
                                          11: Parasites       0.75      0.88      0.81        24
                     12: Brain Cells Circuits & Systems       0.87      0.80      0.83        74
                           13: Sensory & Motor Function       0.75      0.58      0.65        26
                              14: Behaviour & Cognition       0.62      0.78      0.70        51
                      15: Behavioural & Social Sciences       0.33      0.10      0.15        21
                                16: Health Intervention       0.74      0.43      0.54        54
                          17: Health Services & Systems       1.00      0.03      0.06        32
                                       18: Surveillance       0.42      0.53      0.47        34
                 19: Maternal Child & Adolescent Health       1.00      0.13      0.24        30
                                 1: Genetics & Genomics       0.53      0.54      0.54        61
                             20: Nutrition & Metabolism       1.00      0.13      0.24        15
                                     21: Cardiovascular       0.00      0.00      0.00        16
                              22: Experimental Medicine       0.00      0.00      0.00        21
                                    23: Medical Imaging       0.00      0.00      0.00         6
24: Data Science Computational & Mathematical Modelling       0.48      0.29      0.36        38
                2: Gene Regulation and Genome Integrity       0.90      0.52      0.66        71
                        3: Protein Structure & Function       0.88      0.60      0.72        81
                                        4: Cell Biology       0.59      0.52      0.55        79
                               5: Developmental Biology       0.67      0.27      0.38        30
                                   6: Stem Cell Biology       0.67      0.27      0.38        15
                                          7: Immunology       0.78      0.64      0.70        72
                                            8: Bacteria       0.85      0.47      0.61        49
                                             9: Viruses       0.88      0.51      0.65        45

                                              micro avg       0.71      0.48      0.58       950
                                              macro avg       0.61      0.38      0.43       950
                                           weighted avg       0.71      0.48      0.54       950
                                            samples avg       0.67      0.53      0.55       950
```

## 2021.03.1

```
                                                         precision    recall  f1-score   support

                                              10: Fungi       0.00      0.00      0.00         5
                                          11: Parasites       0.89      0.67      0.76        24
                     12: Brain Cells Circuits & Systems       0.91      0.82      0.87        74
                           13: Sensory & Motor Function       0.88      0.54      0.67        26
                              14: Behaviour & Cognition       0.69      0.71      0.70        51
                      15: Behavioural & Social Sciences       0.47      0.33      0.39        21
                                16: Health Intervention       0.71      0.63      0.67        54
                          17: Health Services & Systems       0.96      0.69      0.80        32
                                       18: Surveillance       0.59      0.65      0.62        34
                 19: Maternal Child & Adolescent Health       0.80      0.53      0.64        30
                                 1: Genetics & Genomics       0.61      0.54      0.57        61
                             20: Nutrition & Metabolism       0.70      0.47      0.56        15
                                     21: Cardiovascular       1.00      0.25      0.40        16
                              22: Experimental Medicine       0.20      0.05      0.08        21
                                    23: Medical Imaging       0.50      0.33      0.40         6
24: Data Science Computational & Mathematical Modelling       0.59      0.61      0.60        38
                2: Gene Regulation and Genome Integrity       0.76      0.68      0.72        71
                        3: Protein Structure & Function       0.78      0.75      0.77        81
                                        4: Cell Biology       0.62      0.70      0.66        79
                               5: Developmental Biology       0.86      0.60      0.71        30
                                   6: Stem Cell Biology       1.00      0.33      0.50        15
                                          7: Immunology       0.84      0.68      0.75        72
                                            8: Bacteria       0.91      0.59      0.72        49
                                             9: Viruses       0.89      0.71      0.79        45

                                              micro avg       0.75      0.63      0.68       950
                                              macro avg       0.71      0.54      0.60       950
                                           weighted avg       0.75      0.63      0.67       950
                                            samples avg       0.73      0.67      0.66       950
```
