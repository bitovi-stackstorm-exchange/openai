import sys
import json

from st2common.runners.base_action import Action
from st2client.client import Client
from st2client.models import KeyValuePair

import openai


class CompletionAction(Action):
    def __init__(self, config):
        super(CompletionAction, self).__init__(config=config)
        self.client = Client(base_url="http://localhost")

        self.api_key = self.client.keys.get_by_name(
            name="openai_apikey", decrypt=True
        ).value
        # self.api_key = self.config.get("api_key", None)

        openai.api_key = self.api_key

    def run(
        self,
        prompt,
        n,
        size
    ):
        response = openai.Image.create(
            model=model,
            prompt=prompt,
            n=int(n),
            size=size
        )

        return {"response": response}
