from joblib import load


class MLModel:
    def __init__(self, filename_model):
        self.model = load(filename_model)

    def predict(self, text_vectorized) -> [str]:
        return self.model.predict(text_vectorized).tolist()
