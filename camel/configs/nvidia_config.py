# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========= Copyright 2023-2024 @ CAMEL-AI.org. All Rights Reserved. =========
from __future__ import annotations

from pydantic import Field

from camel.configs.base_config import BaseConfig
from camel.types import NotGiven


class NvidiaConfig(BaseConfig):
    r"""Configuration class for NVIDIA API models.

    This class defines the configuration parameters for NVIDIA's language
    models, including temperature, sampling parameters, and response format
    settings.

    Args:
        stream (bool, optional): Whether to stream the response.
            (default: :obj:`None`)
        temperature (float, optional): Controls randomness in the response.
            Higher values make output more random, lower values make it more
            deterministic. Range: [0.0, 2.0]. (default: :obj:`None`)
        top_p (float, optional): Controls diversity via nucleus sampling.
            Range: [0.0, 1.0]. (default: :obj:`None`)
        presence_penalty (float, optional): Penalizes new tokens based on
            whether they appear in the text so far. Range: [-2.0, 2.0].
            (default: :obj:`None`)
        frequency_penalty (float, optional): Penalizes new tokens based on
            their frequency in the text so far. Range: [-2.0, 2.0].
            (default: :obj:`None`)
        max_tokens (Union[int, NotGiven], optional): Maximum number of tokens
            to generate. If not provided, model will use its default maximum.
            (default: :obj:`None`)
        seed (Optional[int], optional): Random seed for deterministic sampling.
            (default: :obj:`None`)
        tools (Optional[List[Dict]], optional): List of tools available to the
            model. This includes tools such as a text editor, a calculator, or
            a search engine. (default: :obj:`None`)
        tool_choice (Optional[str], optional): Tool choice configuration.
            (default: :obj:`None`)
        stop (Optional[List[str]], optional): List of stop sequences.
            (default: :obj:`None`)
    """

    stream: bool | None = Field(default=None)
    temperature: float | None = Field(default=None)
    top_p: float | None = Field(default=None)
    presence_penalty: float | None = Field(default=None)
    frequency_penalty: float | None = Field(default=None)
    max_tokens: int | NotGiven | None = Field(default=None)
    seed: int | None = Field(default=None)
    tool_choice: str | None = Field(default=None)
    stop: list[str] | None = Field(default=None)


NVIDIA_API_PARAMS = {param for param in NvidiaConfig.model_fields.keys()}
