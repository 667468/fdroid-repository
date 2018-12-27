import json
import os
import re
import requests
import subprocess

def main():
  with open("apks.json") as file:
    apks = json.load(file)
  os.chdir("fdroid/repo")
  for apk in apks:
    ver = ""
    ignore = False
    if "version" in apk:
      verObj = apk["version"]
      if "json" in verObj:
        ver = get_version_json(verObj["url"], verObj["json"])
      elif "regex" in verObj:
        ver = get_version_regex(verObj["url"], verObj["regex"])
    if "ignoreErrors" in apk:
      ignore = apk["ignoreErrors"]
    if "architectures" in apk:
      for arch in apk["architectures"]:
        download(apk["baseUrl"].format(arch=arch, ver=ver), ignore)
    else:
      download(apk["baseUrl"].format(ver=ver), ignore)

def download(download_url, ignore):
  if download_url.endswith(".apk"):
    retcode = subprocess.call(["wget", "-N", download_url])
  else:
    retcode = subprocess.call(["wget", "-nc", "--content-disposition", download_url])
  if not ignore and retcode != 0:
    raise Exception("Failed downloading " + download_url)

def get_version_regex(url, query):
  request = requests.get(url)
  regex = re.search(query, request.text)
  return regex.group(1)

def get_version_json(url, query):
  request = requests.get(url)
  version = request.json()
  if not isinstance(query, list):
    return version[query]
  for query_part in query:
    version = version[query_part]
  return version

if __name__ == "__main__":
  main()