"""
Wrapper for scispacy mesh tagger. SciSpacy implements mesh
tagging as a named entity recognition and linking step so
the class also transforms the problem to multi label classification
"""
from collections import defaultdict

from scispacy.linking import EntityLinker
from scispacy.abbreviation import AbbreviationDetector
from sklearn.metrics import f1_score
import scispacy
import spacy


class SciSpacyMeshTagger():
    def __init__(self, mesh_tags, threshold=2):
        """
        mesh_tags: list of mesh UI descriptros e.g. [D00001]
        """
        self.mesh_tags = mesh_tags
        self.threshold = threshold

    def fit(self, *_):
        nlp = spacy.load("en_core_sci_sm")
        abbreviation_resolver = AbbreviationDetector(nlp)
        nlp.add_pipe(abbreviation_resolver)
        linker = EntityLinker(resolve_abbreviations=True, name="mesh")
        nlp.add_pipe(linker)
        self.nlp = nlp

    def _get_tags(self, doc):
        mesh_ents = defaultdict(int)
        for ent in doc.ents:
            if ent._.kb_ents and ent._.kb_ents[0][0] in self.mesh_tags:
                mesh_ent = ent._.kb_ents[0]
                mesh_ent_ui = mesh_ent[0]
                mesh_ent_prob = mesh_ent[1]
                mesh_ents[mesh_ent_ui] += mesh_ent_prob
        # maybe we want to normalise the p as different lengths might have different number of entities
        tags = [t for t,p in sorted(mesh_ents.items(), key=lambda x: x[1], reverse=True) if p >= self.threshold]
        return tags

    def _binarize_tags(self, tags):
        Y = []
        for doc_tags in tags:
            Y.append([1 if t in doc_tags else 0 for t in self.mesh_tags])
        return Y

    def predict(self, X):
        docs = self.nlp.pipe(X)
        tags = [self._get_tags(doc) for doc in docs]
        return self._binarize_tags(tags)

    def score(self, X, Y):
        Y_pred = self.predict(X)
        return f1_score(Y, Y_pred, average='micro')

