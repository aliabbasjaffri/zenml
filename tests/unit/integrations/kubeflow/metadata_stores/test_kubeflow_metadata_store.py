#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

from zenml.enums import MetadataStoreFlavor, StackComponentType
from zenml.integrations.kubeflow.metadata_stores import KubeflowMetadataStore


def test_kubeflow_metadata_store_attributes():
    """Tests that the basic attributes of the kubeflow metadata store are set
    correctly."""
    metadata_store = KubeflowMetadataStore(name="")

    assert metadata_store.supports_local_execution is True
    assert metadata_store.supports_remote_execution is True
    assert metadata_store.type == StackComponentType.METADATA_STORE
    assert metadata_store.flavor == MetadataStoreFlavor.KUBEFLOW