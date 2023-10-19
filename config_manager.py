import argparse
import requests
import io

from oauth2client.service_account import ServiceAccountCredentials
import json

import os

PROJECT_ID = "medica-test-customer"
CREDENTIALS = json.loads("{\"type\":\"service_account\",\"project_id\":\"medica-test-customer\",\"private_key_id\":\"5c3456c7940b1beb2d43b5f076a4316cc8fa7a8d\",\"private_key\":\"-----BEGINPRIVATEKEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDOrOiDVI2BiR5n\\n8wkmZDGF0wa4HBm38HTuSykubBpGGZKyStsd/2za+vLkUSKFKtuSwgEcDi++y3HW\\nVx0V5rTnx2qndQAT1IBngi10dNgu9GUpa8PzuqKZpiHiepmFQxa1EUQehxoY2pw9\\nD4AtMd8r/3AArELq8pJIuYwf/J731KGV6uKrxe3F8dNBsDsypthLK8aLz7YoQWJd\\n9KtLyEozrHzGXxHQNIe4rsyTAL59P+PKZatsmGQ3ojiwII9kFvs13QB69HWYkKkq\\ngWV7XTaoFXG/uY5SH9LK2xI4ruSDDxlynF2BMXWjlA5Jav38T6zuBPIiprXxIB71\\nihkkWirXAgMBAAECggEAXX5sxJRoWzP7VEzmU765hG99N6ZGoCYfz3iizYRLsnB5\\nIzynuP9GcB1b6ZsmgZVstQwcUmO8h5QjEDJiTvkJ11wnzE8qVM4ptCl4hJki/sLC\\nTKWahFRmoBk+dOS/NECwMgL4jNLTJHEogprTgh5wdcfdFADZWM2ZDVsan5G5HCT9\\nQKym8hkGnFAp8grGLrA7Ea+TRGZdq1oLrAY7mUEncCRj6gK0nZk6VcUqxDK7yUtD\\nobSVSwwXVyJMzNwa1NFQT0v2irErCrjCef5PLzQ8S2BaByYQCH0kw5rVfjl6H+Am\\nkLvDLKESZAoS6J2WFDYWbnlcMEl22/6AIZrY//2RWQKBgQDobqgwNijaBrOsg5S5\\nz8zvxyIoeFSheYCdhm158Ok13Iau7ksq/rwnuYxrZ/XG3viE31bp1n1W7TNdPakP\\nIR3/mO2AHEDb8NgFROkcd+lajWsHSjvTsYc0TAdMwULw8jrF4LM/GUZhKw+Ir8Nq\\nQErYSBgbgSbdIoVbd8coOH+qxQKBgQDjoauUkUNNXXQ9BNsc3OKdR8BijkFoTkkz\\nYsI3Qc5qq4My9t+K58RYgpjNmAmPVXopgLMCjw5l/KTcVcy0Yfzvwrg9PrHBL9Xi\\nkkUCIiwMHiYMIpy6FBzjDOSH6ojHzQM12XliK2cK/04WcgHgEa0PQdtNwvINI7Lh\\nQ3wGmK1I6wKBgFi9Lq9BbjVXS6+4iMasJGUDFPJ4hm8j0UvS7+cXaCItMKqGxeID\\nYViVSZwUE8y6gg1Qq4EZZ78RToPxr6LcFPTpsPsxTj3qZL8WQR2iVlBBH7SnzdGT\\nvLflsv/F5UXSZUf48tZLUwh0BTk9SZE+PJT4aWPO2kShEmMKhtm/QFa1AoGAFiqy\\nOL+EnE4TebW1WLQx5TsNgwtzVyL4geaGHzdrUHvvRNFBp5c2SaA+HRdHJwwd31jH\\nFeK0dj4KF+LLEm3QYdDGfEBUswljfLLdwX1uaKeu8NOWC5DV1050GsA+HabbPy00\\nYtjzKeD+y7TCdf2Cqs+w+XuYcqsdSk52D3ZiuY0CgYBo+X02b6Y47tLkAfJWA71c\\nu7odv7SEOVTovhbm3cq95fyf3BrTqBfttcWoBunJX5j9EoyP3TA7o4ruMGmgXnCO\\nY4DmCAube8N7Pc5NsbWRfes/jOU8ytypYN9k7qxFeXD9YxEpqiLHpm+AvFL+QX5i\\ntKPwrA+dwG3mWR8GpiU+PQ==\\n-----ENDPRIVATEKEY-----\\n\",\"client_email\":\"firebase-adminsdk-ens19@medica-test-customer.iam.gserviceaccount.com\",\"client_id\":\"117174656220392763369\",\"auth_uri\":\"https://accounts.google.com/o/oauth2/auth\",\"token_uri\":\"https://oauth2.googleapis.com/token\",\"auth_provider_x509_cert_url\":\"https://www.googleapis.com/oauth2/v1/certs\",\"client_x509_cert_url\":\"https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-ens19%40medica-test-customer.iam.gserviceaccount.com\",\"universe_domain\":\"googleapis.com\"}")
print(CREDENTIALS)

BASE_URL = "https://firebaseremoteconfig.googleapis.com"
REMOTE_CONFIG_ENDPOINT = "v1/projects/" + PROJECT_ID + "/remoteConfig"
REMOTE_CONFIG_URL = BASE_URL + "/" + REMOTE_CONFIG_ENDPOINT
SCOPES = ["https://www.googleapis.com/auth/firebase.remoteconfig"]

# [START retrieve_access_token]
def _get_access_token():
    """Retrieve a valid access token that can be used to authorize requests.
    :return: Access token.
    """
    credentials = ServiceAccountCredentials.from_json_keyfile_dict(CREDENTIALS, SCOPES)
    access_token_info = credentials.get_access_token()
    return access_token_info.access_token


# [END retrieve_access_token]


def _get(save=False):
    """Retrieve the current Firebase Remote Config template from server.
    Retrieve the current Firebase Remote Config template from server and store it
    locally.
    """






    headers = {"Authorization": "Bearer " + _get_access_token()}
    resp = requests.get(REMOTE_CONFIG_URL, headers=headers)

    if save != False and resp.status_code == 200:
        with io.open("config.json", "wb") as f:
            f.write(resp.text.encode("utf-8"))

        print("Retrieved template has been written to config.json")
    return resp.headers["ETag"]


def _listVersions():
    """Print the last 5 Remote Config version's metadata."""
    headers = {"Authorization": "Bearer " + _get_access_token()}
    resp = requests.get(REMOTE_CONFIG_URL + ":listVersions?pageSize=5", headers=headers)

    if resp.status_code == 200:
        print("Versions:")
        print(resp.text)
    else:
        print("Request to print template versions failed.")
        print(resp.text)


def _rollback(version):
    """Roll back to an available version of Firebase Remote Config template.
    :param version: The version of the template to roll back to.
    """
    headers = {"Authorization": "Bearer " + _get_access_token()}

    json = {"version_number": version}
    resp = requests.post(REMOTE_CONFIG_URL + ":rollback", headers=headers, json=json)

    if resp.status_code == 200:
        print("Rolled back to version: " + version)
        print(resp.text)
        print("ETag from server: {}".format(resp.headers["ETag"]))
    else:
        print("Request to roll back to version " + version + " failed.")
        print(resp.text)


def _publish():
    """Publish local template to Firebase server.
    Args:
      etag: ETag for safe (avoid race conditions) template updates.
          * can be used to force template replacement.
    """
    etag = _get()
    with open("remoteconfig.template.json", "r", encoding="utf-8") as f:
        content = f.read()
    headers = {
        "Authorization": "Bearer " + _get_access_token(),
        "Content-Type": "application/json; UTF-8",
        "If-Match": etag,
    }
    resp = requests.put(
        REMOTE_CONFIG_URL, data=content.encode("utf-8"), headers=headers
    )
    if resp.status_code == 200:
        print("Template has been published.")
        print("ETag from server: {}".format(resp.headers["ETag"]))
    else:
        print("Unable to publish template.")
        print(resp.text)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--action")
    parser.add_argument("--etag")
    parser.add_argument("--version")
    args = parser.parse_args()

    if args.action and args.action == "get":
        _get()
    elif args.action and args.action == "publish":
        _publish()
    elif args.action and args.action == "versions":
        _listVersions()
    elif args.action and args.action == "rollback" and args.version:
        _rollback(args.version)
    else:
        print(
            """Invalid command. Please use one of the following commands:
python configure.py --action=get
python configure.py --action=publish
python configure.py --action=versions
python configure.py --action=rollback --version=<TEMPLATE_VERSION_NUMBER>"""
        )


if __name__ == "__main__":
    main()