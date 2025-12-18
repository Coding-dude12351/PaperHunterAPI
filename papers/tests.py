from django.test import TestCase
from unittest.mock import patch, MagicMock
from django.http import StreamingHttpResponse

from .utils.download_papers import download_file_from_supabase_url


class DownloadPapersTests(TestCase):
	@patch('papers.utils.download_papers.supabase')
	@patch('papers.utils.download_papers.requests.get')
	def test_public_url_generates_signed_url_and_streams(self, mock_get, mock_supabase):
		# Mock supabase signed url response
		mock_supabase.storage.from_.return_value.create_signed_url.return_value = {'signedURL': 'https://signed.example/test.pdf?token=abc'}

		# Mock requests.get
		mock_resp = MagicMock()
		mock_resp.status_code = 200
		mock_resp.headers = {'content-type': 'application/pdf', 'content-length': '3'}
		mock_resp.iter_content.return_value = [b'abc']
		mock_get.return_value = mock_resp

		file_url = 'https://example.supabase.co/storage/v1/object/public/papers/test.pdf'
		response = download_file_from_supabase_url(file_url)

		self.assertIsInstance(response, StreamingHttpResponse)
		self.assertEqual(response['Content-Disposition'], 'attachment; filename="test.pdf"')

	@patch('papers.utils.download_papers.requests.get')
	def test_direct_url_streams_without_supabase(self, mock_get):
		mock_resp = MagicMock()
		mock_resp.status_code = 200
		mock_resp.headers = {'content-type': 'application/pdf'}
		mock_resp.iter_content.return_value = [b'xyz']
		mock_get.return_value = mock_resp

		file_url = 'https://cdn.example.com/files/myfile.pdf'
		response = download_file_from_supabase_url(file_url, download_name='download.pdf')

		self.assertIsInstance(response, StreamingHttpResponse)
		self.assertEqual(response['Content-Disposition'], 'attachment; filename="download.pdf"')
