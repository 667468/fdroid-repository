Unofficial F-Droid repo for various apps
========================================

Currently included (alphabetically):

* Abrowser
* Brave
* Firefox, Firefox Beta, Firefox Nightly
* Firefox Preview
* Firefox Focus / Firefox Klar
* Firefox Lockwise
* Kiwix
* Signal
* Spotify
* Wire

Add this URL to F-Droid:
https://rfc2822.gitlab.io/fdroid-firefox/fdroid/repo?fingerprint=8F992BBBA0340EFE6299C7A410B36D9C8889114CA6C58013C3587CDA411B4AED

[![Repo URL QRcode](fdroid/public/repo-qrcode.png)](https://rfc2822.gitlab.io/fdroid-firefox/fdroid/repo?fingerprint=8F992BBBA0340EFE6299C7A410B36D9C8889114CA6C58013C3587CDA411B4AED)

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

The private key for signing this unofficial F-Droid repository is kept private, but only used for exactly this purpose.<br />
The APKs are unaltered and hence still signed by the app developers.

How to include new apps?
========================

Click [here](ADDAPPS.md) to see how to add a new app to this repo.


Donations
=========

If you want to donate, please donate to the respective developers instead!
