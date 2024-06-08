from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest


endpoint = "https://medical-jayadeva154.cognitiveservices.azure.com/"
key = "c7c09888fc3f436092218e8b26081185"

formUrl = "https://cdn.discordapp.com/attachments/1154658069234597920/1248876778232217735/WhatsApp-Image-2024-06-08-at-11.18.55-AM.pdf?ex=666542a2&is=6663f122&hm=62d378943078e38957ef21bc3e8b8e09c73e3d6bf0ad84c723d500ffbd564fa2&"
document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key))
    
poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-read", formUrl)
result = poller.result()

print ("Document contains content: ", result.content)