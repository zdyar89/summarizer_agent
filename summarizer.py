# This file contains the HuggingFace Pipeline object implementation

import logging
import transformers
import pipeline

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


class HuggingFacePipeline(self):
    """
    Implementation of HuggingFace LLM Pipeline
    """

    def __init__(self, pipeline_task: str, model: str = "facebook/bart-large-cnn") -> None:
        """
        Initializes a new HuggingFace pipeline object.

        Args:
            pipeline_task ('str'): The pipeline task to be performed.
            model ('str'): The HuggingFace LLM to use.

        Returns:
            None
        """
        self.pipeline_task = pipeline_task
        self.model = model
