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
"""Step that allows you to send messages to Slack and wait for a response."""

from zenml.alerter.alerter_utils import get_active_alerter
from zenml.integrations.slack.alerters.slack_alerter import (
    SlackAlerter,
    SlackAlerterConfig,
)
from zenml.steps import StepContext, step


@step
def slack_alerter_ask_step(
    config: SlackAlerterConfig, context: StepContext, message: str
) -> bool:
    """Posts a message to the Slack alerter component and waits for approval.

    This can be useful, e.g. to easily get a human in the loop before
    deploying models.

    Args:
        config: Runtime configuration for the Slack alerter.
        context: StepContext of the ZenML repository.
        message: Initial message to be posted.

    Returns:
        True if a user approved the operation, else False.

    Raises:
        RuntimeError: If currently active alerter is not a `SlackAlerter`.
    """
    alerter = get_active_alerter(context)
    if not isinstance(alerter, SlackAlerter):
        # TODO: potential duplicate code for other components
        # -> generalize to `check_component_flavor()` utility function?
        raise RuntimeError(
            "Step `slack_alerter_ask_step` requires an alerter component of "
            "flavor `slack`, but the currently active alerter is of type "
            f"{type(alerter)}, which is not a subclass of `SlackAlerter`."
        )
    return alerter.ask(message, config)
