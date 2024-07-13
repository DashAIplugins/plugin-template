from DashAI.back.core.schema_fields import BaseSchema, schema_field


class PluginSchema(BaseSchema):
    epochs: schema_field(
        type_field(), # Choose between different types_fields e.g. int_field, string_field, etc
        placeholder=, # Placeholde to display in UI
        description=(
            "Field description"
        ),
    )  # type: ignore


class PluginClass(PluginParentClass):

    SCHEMA = PluginSchema

    def __init__(
            self, 
            # add here the params specified in the schema
            **kwargs
        ):
        super().__init__(**kwargs)
        self.model = None

    def fit(self, x: datasets.Dataset, y: datasets.Dataset) -> None:
        pass
        # This method should train the model and put it in self.model class variable

    def predict(self, x: datasets.Dataset) -> list:
        pass
        # This method must return a list of the predicted probabilities of each class for each input in x

    def save(self, filename: str) -> None:
        """Save the model in the specified path."""
        pass

    @staticmethod
    def load(filename: str) -> None:
        """Load the model of the specified path."""
        pass
