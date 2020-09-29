"""
Evaluate MeSH model on grants annotated with MeSH

The script works on an Excel file that contains 
columns that follow the pattern below
Disease MeSH#TAG_INDEX (ANNOTATOR)
"""
from argparse import ArgumentParser
from pathlib import Path
import pickle

from sklearn.metrics import classification_report
import pandas as pd


def get_tags(data, annotator):
    tag_columns = [col for col in data.columns if annotator in col]
    tags = []
    for _, row in data.iterrows():
        row_tags = [tag for tag in row[tag_columns] if not pd.isnull(tag)]
        tags.append(row_tags)
    return tags

def evaluate_mesh_on_grants(data_path, label_binarizer_path):
    data = pd.read_excel(data_path)

    with open(label_binarizer_path, "rb") as f:
        label_binarizer = pickle.loads(f.read())

    gold_tags = get_tags(data, "KW")
    model_tags = get_tags(data, "NS")
    Y = label_binarizer.transform(gold_tags)
    Y_pred = label_binarizer.transform(model_tags)
#    print(classification_report(Y, Y_pred, target_names=label_binarizer.classes_))

    unique_tags = len(set([t for tags in gold_tags for t in tags]))
    all_tags = len(label_binarizer.classes_)
    print(f"Gold dataset contains examples from {unique_tags} tags out of {all_tags}")

if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('--data_path', type=Path, help="path to validation data")
    argparser.add_argument('--label_binarizer_path', type=Path, help="path to disease label binarizer")
    args = argparser.parse_args()

    evaluate_mesh_on_grants(args.data_path, args.label_binarizer_path)
