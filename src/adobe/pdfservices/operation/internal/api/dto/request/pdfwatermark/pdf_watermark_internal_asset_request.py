# Copyright 2024 Adobe
# All Rights Reserved.
#
# NOTICE:  All information contained herein is, and remains
# the property of Adobe and its suppliers, if any. The intellectual
# and technical concepts contained herein are proprietary to Adobe
# and its suppliers and are protected by all applicable intellectual
# property laws, including trade secret and copyright laws.
# Dissemination of this information or reproduction of this material
# is strictly forbidden unless prior written permission is obtained
# from Adobe.

import json
from abc import ABC
from typing import List

from adobe.pdfservices.operation.config.notifier.notifier_config import NotifierConfig
from adobe.pdfservices.operation.internal.api.dto.request.pdf_services_api.pdf_services_api_request import \
    PDFServicesAPIRequest
from adobe.pdfservices.operation.internal.util.json_hint_encoder import JSONHintEncoder
from adobe.pdfservices.operation.pdfjobs.params.pdf_watermark.pdf_watermark_params import PDFWatermarkParams


class PDFWatermarkInternalAssetRequest(PDFServicesAPIRequest, ABC):
    json_hint = {
        'input_document_asset_id': 'inputDocumentAssetID',
        'watermark_document_asset_id': 'watermarkDocumentAssetID',
        'page_ranges': 'pageRanges',
        'appearance': 'appearance',
        'notify_config_list': 'notifiers'
    }

    def __init__(self, input_document_asset_id: str, watermark_document_asset_id : str, pdf_watermark_params: PDFWatermarkParams,
                 notify_config_list: List[NotifierConfig] = None):
        super().__init__()
        self.input_document_asset_id = input_document_asset_id
        self.watermark_document_asset_id = watermark_document_asset_id
        if pdf_watermark_params is not None:
            if pdf_watermark_params.get_page_ranges() is not None:
                self.page_ranges = pdf_watermark_params.get_page_ranges().ranges
            self.appearance = pdf_watermark_params.get_watermark_appearance()
        self.notify_config_list = notify_config_list

    def to_json(self):
        return json.dumps(self, cls=JSONHintEncoder, indent=1, sort_keys=True)
