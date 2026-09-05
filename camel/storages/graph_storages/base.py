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

from abc import ABC, abstractmethod
from typing import Any


class BaseGraphStorage(ABC):
    r"""An abstract base class for graph storage systems."""

    @property
    @abstractmethod
    def get_client(self) -> Any:
        r"""Get the underlying graph storage client."""

    @property
    @abstractmethod
    def get_schema(self) -> str:
        r"""Get the schema of the graph storage"""

    @property
    @abstractmethod
    def get_structured_schema(self) -> dict[str, Any]:
        r"""Get the structured schema of the graph storage"""

    @abstractmethod
    def refresh_schema(self) -> None:
        r"""Refreshes the graph schema information."""

    @abstractmethod
    def add_triplet(self, subj: str, obj: str, rel: str) -> None:
        r"""Adds a relationship (triplet) between two entities in the database.

        Args:
            subj (str): The identifier for the subject entity.
            obj (str): The identifier for the object entity.
            rel (str): The relationship between the subject and object.
        """

    @abstractmethod
    def delete_triplet(self, subj: str, obj: str, rel: str) -> None:
        r"""Deletes a specific triplet from the graph, comprising a subject,
        object and relationship.

        Args:
            subj (str): The identifier for the subject entity.
            obj (str): The identifier for the object entity.
            rel (str): The relationship between the subject and object.
        """

    @abstractmethod
    def query(
        self, query: str, params: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:
        r"""Query the graph store with statement and parameters.

        Args:
            query (str): The query to be executed.
            params (Optional[Dict[str, Any]]): A dictionary of parameters to
                be used in the query. Defaults to `None`.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each
                dictionary represents a row of results from the query.
        """
