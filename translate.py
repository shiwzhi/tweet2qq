import requests
import xml.etree.ElementTree as ET
def translate(text, from_lang, to_lang):
	data = {'client_id': 'shiweizhi', 'client_secret': 'be0k+8yoBiAF/obSquKylPbnMvqVi41AE4YG7SbWpPk=', 'scope': 'http://api.microsofttranslator.com', 'grant_type': 'client_credentials'}
	r = requests.post('https://datamarket.accesscontrol.windows.net/v2/OAuth2-13', data=data)

	headers = {
		'Authorization': 'Bearer '+r.json()['access_token']
	}

	params = {
		'text': text,
		'from': from_lang,
		'to': to_lang
	}

	url = 'http://api.microsofttranslator.com/v2/Http.svc/Translate'
	run = requests.get(url, headers=headers, params=params)
	xml = ET.fromstring(run.text)
	return xml.text