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
            name="openapi_apikey", decrypt=True
        ).value
        # self.api_key = self.config.get("api_key", None)

        openai.api_key = self.api_key
        print("api key:")
        print(self.api_key[:10])

    def run(
        self,
        prompt,
        model,
        max_tokens,
        temperature,
        top_p,
        frequency_penalty,
        presence_penalty,
        stop,
    ):
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            stop=stop,
        )
        return {"response": response}
