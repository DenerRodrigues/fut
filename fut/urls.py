import requests

from .exceptions import FutError

# config
rc = requests.get('https://www.easports.com/fifa/ultimate-team/web-app/config/config.json').json()
auth_url = rc['authURL']
pin_url = rc['pinURL']  # TODO: urls in dict?
client_id = rc['eadpClientId']
release_type = rc['releaseType']
fun_captcha_public_key = rc['funCaptchaPublicKey']


# remote config - should be refresh every x seconds
rc = requests.get('https://www.easports.com/fifa/ultimate-team/web-app/content/20C1B296-B15C-4F72-AF0F-882F187EC2C9/2020/fut/config/companion/remoteConfig.json').json()

if rc['pin'] != {"b": True, "bf": 500, "bs": 10, "e": True, "r": 3, "rf": 300}:
    print('>>> WARNING: ping variables changed: %s' % rc['pin'])

if rc['futweb_maintenance']:
    raise FutError('Futweb maintenance, please retry in few minutes.')

itemsPerPage = dict()
itemsPerPage = rc['itemsPerPage']
# nasty hack but it's better than parsing big js file
itemsPerPage['transferMarket'] += 1
itemsPerPage['club'] = 91  # ea, please don't troll us :-)

# TODO: read sku's from https://utas.mob.v1.fut.ea.com/ut/shards/v2

# TODO: card info url not found yet
card_info_url = 'https://www.easports.com/fifa/ultimate-team/web-app/content/20C1B296-B15C-4F72-AF0F-882F187EC2C9/{year}/fut/items/web/'  # TODO: get hash from somewhere, dynamic year
# TODO: could be nice to add locals on startup
messages_url = 'https://www.easports.com/fifa/ultimate-team/web-app/loc/en_US.json'  # TODO: needs to base64 decoded.
