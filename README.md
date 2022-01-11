Unofficial F-Droid repo for various apps
========================================

Currently included (alphabetically):

* Firefox (may sometimes be a release candidate)
* Firefox Beta
* Firefox Focus / Firefox Klar
* Kiwix
* Signal
* Wire

Add this URL to F-Droid:
https://rfc2822.gitlab.io/fdroid-firefox/fdroid/repo?fingerprint=8F992BBBA0340EFE6299C7A410B36D9C8889114CA6C58013C3587CDA411B4AED

[![Repo URL QRcode](fdroid/public/repo-qrcode.png)](https://rfc2822.gitlab.io/fdroid-firefox/fdroid/repo?fingerprint=8F992BBBA0340EFE6299C7A410B36D9C8889114CA6C58013C3587CDA411B4AED)

For some apps, this repo may include APKs of more than one architecture that is compatible with your device, and all of them will appear in the "Versions" list in the F-Droid client.
To show the architecture of each APK, enable "Expert mode" in the F-Droid settings.

All code and other work in this repository is in the public domain, i.e. licensed as such.<br />
**Both, this Gitlab repository and this unofficial F-Droid repository
are not affiliated to, nor have been authorized, sponsored or otherwise approved by the app developers.**

You can see what's inside the repo here: https://rfc2822.gitlab.io/fdroid-firefox/fdroid/repo/index.xml

It was first created to serve the Firefox APKs, hence the name, which will be changed as soon as a solution
to redirecting from the current repo URL is found.


How does it work?
=================

This unofficial F-Droid repository is hosted using [Gitlab pages](https://about.gitlab.com/2016/04/07/gitlab-pages-setup/).
A daily [scheduled pipeline](https://docs.gitlab.com/ce/user/project/pipelines/schedules.html)
downloads the APKs directly from the app developers and then updates this F-Droid repository (which lives
on Gitlab pages).<br />
All necessary actions are performed by [Gitlab CI/CD](https://about.gitlab.com/features/gitlab-ci-cd/).
This Gitlab repository contains the complete source code to configure Gitlab CI/CD and this F-Droid repository.

The private key for signing this unofficial F-Droid repository is kept private, but only used for exactly this purpose.
To generate your own key run:
```
keytool -genkey -v -keystore my.keystore -alias repokey -keyalg RSA -keysize 2048 -validity 10000 -storepass passw0rd1
```

Get base64 representation (ASCII only characters) of the certificate:
```
base64 my.keystore
```
Then paste it into to the gitlab variables.

**The APKs are unaltered and hence still signed by the app developers.**

How to include new apps?
========================

Click [here](ADDAPPS.md) to see how to add a new app to this repo.

Please note that the repo has to be kept small because there's a 1 GB limit on Gitlab pages.
If you need specific apps, you can fork this repo and maintain your own one.

See [LICENSE.md](LICENSE) for license info. Please sign your commit
(git -s) to accept the license.


Donations
=========

If you want to donate, please donate to the respective app developers instead!

