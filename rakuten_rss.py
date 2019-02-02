"""楽天RSS用モジュール
"""
from lib.ddeclient import DDEClient


def rss(code, item):
	""" 楽天RSSから情報を取得
	Parameters
	----------
	code : str
		株価や先物のコード　例：東京電力の場合'9501.T'
	item :
	Returns
	-------
	str

	Examples
	----------

	>>>rss('9501.T' , '始値')
	'668.00'

	>>>rss('9501.T' , '現在値')
	'669.00'

	>>>rss('9501.T' , '銘柄名称')
	'東京電力ＨＤ'

	>>>rss('9501.T' , '現在値詳細時刻')
	'15:00:00'

	"""

	dde = DDEClient("rss", str(code))
	try:
		res = dde.request(item).decode('sjis').strip()
	except:
		print('fail: code@', code)
		res = 0
	finally:
		dde.__del__()
	return res


def rss_dict(code, *args):
	"""
	楽天RSSから辞書形式で情報を取り出す(複数の詳細情報問い合わせ可）

	Parameters
	----------
	code : str
	args : *str

	Returns
	-------
	dict

	Examples
	----------
	>>>rss_dict('9502.T', '始値','銘柄名称','現在値')
	{'始値': '1739.50', '現在値': '1661.50', '銘柄名称': '中部電力'}


	"""

	dde = DDEClient("rss", str(code))
	res = {}
	try:
		for item in args:
			res[item] = dde.request(item).decode('sjis').strip()
	except:
		print('fail: code@', code)
		res = {}
	finally:
		dde.__del__()
	return res


def fetch_open(code):
	""" 始値を返す（SQ計算用に関数切り出し,入力int）

	Parameters
	----------
	code : int
	Examples
	---------
	>>> fetch_open(9551)
	50050
	"""

	return float(rss(str(code) + '.T', '始値'))