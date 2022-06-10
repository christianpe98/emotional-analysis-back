from joblib import load

from core.emotional_analysis.lexicon_approach.emotional_analysis_lexicon import EmotionalAnalysisLexicon
from core.emotional_analysis.lexicon_approach.lexicons.nrc_emotions_lexicon import NRCEmotionLexicon
from core.emotional_analysis.lexicon_approach.lexicons.nrc_hashtag_lexicon import NRCHashtagLexicon
from core.emotional_analysis.ml_approach.emotional_analysis_ml import EmotionalAnalysisML
from core.emotional_analysis.ml_approach.ml_model import MLModel
from core.emotional_analyzer import EmotionalAnalyzer


class EmotionalAnalyzerBuilder:

    analysis_approaches_options = [
        {"label":"APPROACH: Keyword - LEXICON: NRC Emotions","code":"LEXICON-NRC-EMOTIONS"},
        {"label":"APPROACH: Keyword - LEXICCON: NRC Hashtag","code":"LEXICON-NRC-HASHTAG"},
        {"label":"APPROACH: Machine Learning - MODEL: Decision Tree - TRAINING DATASET: CARER","code":"MODEL-DECISION-TREE__CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: Decision Tree - TRAINING DATASET: CARER 4 emotions",
         "code": "MODEL-DECISION-TREE__CARER-4"},
        {"label":"APPROACH: Machine Learning - MODEL: Random Forest - TRAINING DATASET: CARER","code":"MODEL-RANDOM-FOREST__CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: Random Forest - TRAINING DATASET: CARER 4 emotions",
         "code": "MODEL-RANDOM-FOREST__CARER-4"},
        {"label":"APPROACH: Machine Learning - MODEL: SVM SVC - TRAINING DATASET: CARER","code":"MODEL-SVM-SVC__CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: SVM SVC - TRAINING DATASET: CARER 4 emotions",
         "code": "MODEL-SVM-SVC__CARER-4"},
        {"label":"APPROACH: Machine Learning - MODEL: Neuronal Network - TRAINING DATASET: CARER","code":"MODEL-NEURONAL-NETWORK__CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: Neuronal Network - TRAINING DATASET: CARER 4 emotions",
         "code": "MODEL-NEURONAL-NETWORK__CARER-4"},
        {"label":"APPROACH: Machine Learning - MODEL: Bernoulli - TRAINING DATASET: CARER","code":"MODEL-BERNOULLI__CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: Bernoulli - TRAINING DATASET: CARER 4 emotions",
         "code": "MODEL-BERNOULLI__CARER-4"},
        {"label": "APPROACH: Machine Learning - MODEL: Decision Tree - TRAINING DATASET: ISEAR",
         "code": "MODEL-DECISION-TREE__ISEAR"},
        {"label": "APPROACH: Machine Learning - MODEL: Decision Tree - TRAINING DATASET: ISEAR 4 emotions",
         "code": "MODEL-DECISION-TREE__ISEAR-4"},
        {"label": "APPROACH: Machine Learning - MODEL: Random Forest - TRAINING DATASET: ISEAR",
         "code": "MODEL-RANDOM-FOREST__ISEAR"},
        {"label": "APPROACH: Machine Learning - MODEL: Random Forest - TRAINING DATASET: ISEAR 4 emotions",
         "code": "MODEL-RANDOM-FOREST__ISEAR-4"},
        {"label": "APPROACH: Machine Learning - MODEL: SVM SVC - TRAINING DATASET: ISEAR",
         "code": "MODEL-SVM-SVC__ISEAR"},
        {"label": "APPROACH: Machine Learning - MODEL: SVM SVC - TRAINING DATASET: ISEAR 4 emotions",
         "code": "MODEL-SVM-SVC__ISEAR-4"},
        {"label": "APPROACH: Machine Learning - MODEL: Neuronal Network - TRAINING DATASET: ISEAR",
         "code": "MODEL-NEURONAL-NETWORK__ISEAR"},
        {"label": "APPROACH: Machine Learning - MODEL: Neuronal Network - TRAINING DATASET: ISEAR 4 emotions",
         "code": "MODEL-NEURONAL-NETWORK__ISEAR-4"},
        {"label": "APPROACH: Machine Learning - MODEL: Bernoulli - TRAINING DATASET: ISEAR",
         "code": "MODEL-BERNOULLI__ISEAR"},
        {"label": "APPROACH: Machine Learning - MODEL: Bernoulli - TRAINING DATASET: ISEAR 4 emotions",
         "code": "MODEL-BERNOULLI__ISEAR-4"},

        {"label": "APPROACH: Machine Learning - MODEL: Decision Tree - TRAINING DATASET: ISEAR 4 emotions + CARER 4 emotions",
         "code": "MODEL-DECISION-TREE__ISEAR-CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: Random Forest - TRAINING DATASET: ISEAR 4 emotions + CARER 4 emotions",
         "code": "MODEL-RANDOM-FOREST__ISEAR-CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: SVM SVC - TRAINING DATASET: ISEAR 4 emotions + CARER 4 emotions",
         "code": "MODEL-SVM-SVC__ISEAR-CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: Neuronal Network - TRAINING DATASET: ISEAR 4 emotions + CARER 4 emotions",
         "code": "MODEL-NEURONAL-NETWORK__ISEAR-CARER"},
        {"label": "APPROACH: Machine Learning - MODEL: Bernoulli - TRAINING DATASET: ISEAR 4 emotions + CARER 4 emotions",
         "code": "MODEL-BERNOULLI__ISEAR-CARER"},
        ]


    @staticmethod
    def build_emotional_analyzer(analysis_code: str) -> EmotionalAnalyzer:
        base_path="models_raw/"
        base_path_carer=f"{base_path}carer/"
        base_path_carer_4=f"{base_path}carer_4/"
        base_path_isear=f"{base_path}isear/"
        base_path_isear_4=f"{base_path}isear_4/"
        base_path_isear_carer=f"{base_path}carer_4-isear_4/"

        if analysis_code == "LEXICON-NRC-EMOTIONS":
            return EmotionalAnalyzer(EmotionalAnalysisLexicon(NRCEmotionLexicon()))
        if analysis_code == "LEXICON-NRC-HASHTAG":
            return EmotionalAnalyzer(EmotionalAnalysisLexicon(NRCHashtagLexicon()))

        # DATASET CARER
        if analysis_code == "MODEL-DECISION-TREE__CARER":
            vectorizer = load(f"{base_path_carer}feature-extractor_carer_data.joblib")
            model = MLModel(f"{base_path_carer}model-decision-tree__carer_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-RANDOM-FOREST__CARER":
            vectorizer = load(f"{base_path_carer}feature-extractor_carer_data.joblib")
            model = MLModel(f"{base_path_carer}model-random-forest__carer_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-SVM-SVC__CARER":
            vectorizer = load(f"{base_path_carer}feature-extractor_carer_data.joblib")
            model = MLModel(f"{base_path_carer}model-svm-svc__carer_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-NEURONAL-NETWORK__CARER":
            vectorizer = load(f"{base_path_carer}feature-extractor_carer_data.joblib")
            model = MLModel(f"{base_path_carer}model-neuronal-network__carer_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-BERNOULLI__CARER":
            vectorizer = load(f"{base_path_carer}feature-extractor_carer_data.joblib")
            model = MLModel(f"{base_path_carer}model-bayes-bernoulli__carer_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))

        # DATASET CARER 4 EMOTIONS
        if analysis_code=="MODEL-DECISION-TREE__CARER-4":
            vectorizer = load(f"{base_path_carer_4}feature-extractor_carer_data_4_emotions.joblib")
            model = MLModel(f"{base_path_carer_4}model-decision-tree__carer_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-RANDOM-FOREST__CARER-4":
            vectorizer = load(f"{base_path_carer_4}feature-extractor_carer_data_4_emotions.joblib")
            model = MLModel(f"{base_path_carer_4}model-random-forest__carer_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-SVM-SVC__CARER-4":
            vectorizer = load(f"{base_path_carer_4}feature-extractor_carer_data_4_emotions.joblib")
            model = MLModel(f"{base_path_carer_4}model-svm-svc__carer_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-NEURONAL-NETWORK__CARER-4":
            vectorizer = load(f"{base_path_carer_4}feature-extractor_carer_data_4_emotions.joblib")
            model = MLModel(f"{base_path_carer_4}model-neuronal-network__carer_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-BERNOULLI__CARER-4":
            vectorizer = load(f"{base_path_carer_4}feature-extractor_carer_data_4_emotions.joblib")
            model = MLModel(f"{base_path_carer_4}model-bayes-bernoulli__carer_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))

        # DATASET ISEAR
        if analysis_code == "MODEL-DECISION-TREE__ISEAR":
            vectorizer = load(f"{base_path_isear}feature-extractor_isear_data_emotions.joblib")
            model = MLModel(f"{base_path_isear}model-decision-tree__isear_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-RANDOM-FOREST__ISEAR":
            vectorizer = load(f"{base_path_isear}feature-extractor_isear_data_emotions.joblib")
            model = MLModel(f"{base_path_isear}model-random-forest__isear_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-SVM-SVC__ISEAR":
            vectorizer = load(f"{base_path_isear}feature-extractor_isear_data_emotions.joblib")
            model = MLModel(f"{base_path_isear}model-svm-svc__isear_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-NEURONAL-NETWORK__ISEAR":
            vectorizer = load(f"{base_path_isear}feature-extractor_isear_data_emotions.joblib")
            model = MLModel(f"{base_path_isear}model-neuronal-network__isear_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code == "MODEL-BERNOULLI__ISEAR":
            vectorizer = load(f"{base_path_isear}feature-extractor_isear_data_emotions.joblib")
            model = MLModel(f"{base_path_isear}model-bayes-bernoulli__isear_data.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))

        # DATASET ISEAR 4 EMOTIONS
        if analysis_code=="MODEL-DECISION-TREE__ISEAR-4":
            vectorizer = load(f"{base_path_isear_4}feature-extractor_isear_data_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_4}model-decision-tree__isear_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-RANDOM-FOREST__ISEAR-4":
            vectorizer = load(f"{base_path_isear_4}feature-extractor_isear_data_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_4}model-random-forest__isear_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-SVM-SVC__ISEAR-4":
            vectorizer = load(f"{base_path_isear_4}feature-extractor_isear_data_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_4}model-svm-svc__isear_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-NEURONAL-NETWORK__ISEAR-4":
            vectorizer = load(f"{base_path_isear_4}feature-extractor_isear_data_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_4}model-neuronal-network__isear_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-BERNOULLI__ISEAR-4":
            vectorizer = load(f"{base_path_isear_4}feature-extractor_isear_data_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_4}model-bayes-bernoulli__isear_data_4_emotions.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))

        # DATASET ISEAR Y CARER 4 EMOCIONES
        if analysis_code=="MODEL-DECISION-TREE__ISEAR-CARER":
            vectorizer = load(f"{base_path_isear_carer}feature-extractor_carer-isear_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_carer}model-decision-tree__train-carer-isear_4_test-carer-isear_4.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-RANDOM-FOREST__ISEAR-CARER":
            vectorizer = load(f"{base_path_isear_carer}feature-extractor_carer-isear_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_carer}model-random-forest__train-carer-isear_4_test-carer-isear_4.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-SVM-SVC__ISEAR-CARER":
            vectorizer = load(f"{base_path_isear_carer}feature-extractor_carer-isear_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_carer}model-svm-svc__train-carer-isear_4_test-carer-isear_4.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-NEURONAL-NETWORK__ISEAR-CARER":
            vectorizer = load(f"{base_path_isear_carer}feature-extractor_carer-isear_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_carer}model-neuronal-network__train-carer-isear_4_test-carer-isear_4.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        if analysis_code=="MODEL-BERNOULLI__ISEAR-CARER":
            vectorizer = load(f"{base_path_isear_carer}feature-extractor_carer-isear_4_emotions.joblib")
            model = MLModel(f"{base_path_isear_carer}model-bayes-bernoulli__train-carer-isear_4_test-carer-isear_4.joblib")
            return EmotionalAnalyzer(EmotionalAnalysisML(model, vectorizer))
        raise KeyError(f"The code of the emotional analysis approach is not recognised:{analysis_code}")
