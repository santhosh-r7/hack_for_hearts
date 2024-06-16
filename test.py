from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest


endpoint = ""
key = ""

formUrl = ""
document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key))
    
poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-read", formUrl)
result = poller.result()

print ("Document contains content: ", result.content)
