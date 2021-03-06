from sklearn.pipeline import Pipeline

from hyp_param_optim.models_dict import FORECAST_ALGO


class Model():
    def __init__(self, pipeline):
        steps = self.create_steps(pipeline)
        # self.model = Pipeline(steps=steps)
        self.model = steps[0][1]

    def created_model(self):
        return self.model

    def create_steps(self, pipeline):
        steps = list()
        for model_name in pipeline:
            # add features from pipeline
            if model_name in FORECAST_ALGO.keys():
                step = self._make_step(model_name)
                steps.append(step)

            else:
                # if method not found
                steps.append([model_name, None])
        return steps


    def _make_step(self, model_name):
        if isinstance(FORECAST_ALGO[model_name], type):
            step = [model_name, FORECAST_ALGO[model_name]()]
        else:
            # if already initialized
            step = [model_name, FORECAST_ALGO[model_name]]
        return step
