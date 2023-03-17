#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = os.environ.get("LuisAppId", "e6eb0e67-2cf9-45aa-9ec5-d3f808012404")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "7117b3e146fa421094176f4424a80ece") #"662f82407f4043ed985858614d76d56e")
    # LUIS endpoint host name, ie "westus.api.cognitive.microsoft.com"
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "p10luis-authoring.cognitiveservices.azure.com") #"p10luis.cognitiveservices.azure.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", "62285427-6afc-4eff-9a56-5db4af84fdaf"
    )
