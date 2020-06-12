#!/usr/bin/env python3

import json
import re
import requests
import subprocess

def main():
  with open("apks.json") as file:
    apks = json.load(file)
  for apk in apks:
    ver = ""
    forceFileName = False
    ignore = False
    if "version" in apk:
      verObj = apk["version"]
      if "json" in verObj:
        ver = get_version_json(verObj["url"], verObj["json"])
      elif "regex" in verObj:
        ver = get_version_regex(verObj["url"], verObj["regex"])
    print("Downloading " + apk["name"] + " " + ver)
    if "forceFileName" in apk:
      forceFileName = apk["forceFileName"]
    if "ignoreErrors" in apk:
      ignore = apk["ignoreErrors"]
    if "architectures" in apk:
      for arch in apk["architectures"]:
        download(apk["baseUrl"].format(arch=arch, ver=ver, ver_stripped=ver.lstrip("v"), ver_splitted=ver.split(".")), forceFileName, ignore)
    else:
      download(apk["baseUrl"].format(ver=ver, ver_stripped=ver.lstrip("v"), ver_splitted=ver.split(".")), forceFileName, ignore)

def download(download_url, forceFileName, ignore):
  if forceFileName:
    retcode = subprocess.call(["wget", "--progress=dot:mega", "-N", "-P", "fdroid/repo", "-O", forceFileName, download_url])
  elif download_url.endswith(".apk"):
    retcode = subprocess.call(["wget", "--progress=dot:mega", "-N", "-P", "fdroid/repo", download_url])
  else:
    retcode = subprocess.call(["wget", "--progress=dot:mega", "-nc", "--content-disposition", "-P", "fdroid/repo", download_url])
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
