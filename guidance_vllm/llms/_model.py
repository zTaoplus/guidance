from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from vllm import SamplingParams
    from vllm.outputs import RequestOutput


import logging

import os
import torch
from transformers import AutoConfig, AutoTokenizer


import requests
from loguru import logger

endpoint = os.getenv("VLLM_ENDPOINT_URL", "http://127.0.0.1:8080")


class VllmServiceModel:
    def __init__(self, model_name_or_path: str) -> None:
        self.config = AutoConfig.from_pretrained(model_name_or_path)
        # self.model = LLM(model=model_name_or_path)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    def generate(self, request_dict: dict, **kwargs):
        logger.debug(f"request dic:{request_dict}")
        ret = requests.post(endpoint + "/generate", json=request_dict).json()
        logger.debug(f"vllm svc return json:{ret}")
        return ret


class VllmModel:
    def __init__(self, model_name_or_path: str) -> None:
        from vllm import LLM
        self.config = AutoConfig.from_pretrained(model_name_or_path)
        self.model = LLM(model=model_name_or_path)
        self.tokenizer = self.model.get_tokenizer()

    def generate(
        self,
        prompt_token_ids: list[list[int]],
        sampling_params: "SamplingParams",
        **kwargs,
    ):
        logging.debug(f"input token ids: {prompt_token_ids}")
        outputs: "RequestOutput" = self.model.generate(
            prompt_token_ids=prompt_token_ids,
            sampling_params=sampling_params,
            use_tqdm=False,
        )

        output_token_ids: list = outputs[0].outputs[0].token_ids

        logging.debug(f"output token ids: {output_token_ids}")

        return torch.as_tensor([prompt_token_ids[0] + output_token_ids])
