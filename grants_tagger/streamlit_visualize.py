import pickle
import json

import streamlit as st
import pandas as pd

try:
    import shap

    SHAP_IMPORTED = True
except ImportError:
    print(
        "To get explanations for the predictions install shap "
        "with pip install git+https://github.com/nsorros/shap.git@dev"
    )
    SHAP_IMPORTED = False

#from grants_tagger.predict import predict_tags


DEFAULT_TEXT = "The cell is..."

threshold = st.sidebar.slider("Threshold", min_value=0.0, max_value=1.0, value=0.5)
text = st.text_area("Grant abstract", DEFAULT_TEXT, height=300)

models = {
    "disease_mesh_cnn-2021.03.1": {
        "model_path": "models/disease_mesh_cnn-2021.03.1/",
        "label_binarizer_path": "models/disease_mesh_label_binarizer.pkl",
        "approach": "mesh-cnn",
        "enabled": False
    },
    "tfidf-svm-2020.05.2": {
        "model_path": "models/tfidf-svm-2020.05.2.pkl",
        "label_binarizer_path": "models/label_binarizer.pkl",
        "approach": "tfidf-svm",
        "enabled": False
    },
    "scibert-2020.05.5": {
        "model_path": "models/scibert-2020.05.5/",
        "label_binarizer_path": "models/label_binarizer.pkl",
        "approach": "scibert",
        "enabled": False
    },
    "mesh-xlinear-2022.2.0": {
        "model_path": "models/xlinear-0.2.3/model",
        "full_report_path": "results/mesh_xlinear_full_report.json",
        "label_binarizer_path": "models/xlinear-0.2.3/label_binarizer-0.2.3.pkl",
        "approach": "mesh-xlinear",
        "enabled": True
    },
}

model_option = st.sidebar.selectbox(
    "Model",
    options=[model_name for model_name, params in models.items() if params["enabled"]]
)
full_report = {}
model = models[model_option]

if model.get("full_report_path"):
    with open(model["full_report"], "r") as f:
        full_report = json.load(f)

probabilities = st.sidebar.checkbox("Display probabilities")

if text == DEFAULT_TEXT:
    st.stop()

with st.spinner("Calculating tags..."):
    tags = predict_tags(
        [text],
        model["model_path"],
        model["label_binarizer_path"],
        model["approach"],
        probabilities=probabilities,
        threshold=threshold,
    )
    tags = tags[0]
st.success("Done!")

if probabilities:
    tag_probs = [
        {"Tag": tag, "Prob": prob} for tag, prob in tags.items() if prob > threshold
    ]
    st.table(pd.DataFrame(tag_probs))
    tags = [tag_prob["Tag"] for tag_prob in tag_probs]
else:
    for tag in tags:
        st.button(tag)

if SHAP_IMPORTED:
    from grants_tagger.models.mesh_cnn import MeshCNN

    if model["approach"] == "mesh-cnn":
        mesh_cnn = MeshCNN(threshold=threshold)
        mesh_cnn.load(model["model_path"])
        tokenizer = mesh_cnn.vectorizer.tokenizer

        with open(model["label_binarizer_path"], "rb") as f:
            label_binarizer = pickle.loads(f.read())

        with st.spinner("Calculating explanation..."):
            masker = shap.maskers.Text(tokenizer, mask_token="")
            explainer = shap.Explainer(
                mesh_cnn.predict_proba, masker, output_names=label_binarizer.classes_
            )
            shap_values = explainer([text])

        for tag in tags:
            st.write(tag)
            tag_index = list(label_binarizer.classes_).index(tag)

            html = shap.plots.text(shap_values[0, :, tag_index], display=False)
            st.components.v1.html(html, height=300, scrolling=True)


if full_report:
    pass  # Build the report 
