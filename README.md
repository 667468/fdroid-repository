

Firefox F-Droid repo (inofficial)
=================================

Add this URL to F-Droid:  
https://rfc2822.gitlab.io/fdroid-firefox/fdroid/repo?fingerprint=8F992BBBA0340EFE6299C7A410B36D9C8889114CA6C58013C3587CDA411B4AED

[![Repo URL QRcode](public/repo-qrcode.png)](https://rfc2822.gitlab.io/fdroid-firefox/fdroid/repo?fingerprint=8F992BBBA0340EFE6299C7A410B36D9C8889114CA6C58013C3587CDA411B4AED)

All code/work of this repository is put to public domain. This repository
is not affiliated to, nor has it been authorized, sponsored or
otherwise approved by Mozilla.

Discussion: https://forum.f-droid.org/t/separate-non-free-firefox-repo/944


How does it work?
=================

The F-Droid repository is hosted using [Gitlab pages](https://about.gitlab.com/2016/04/07/gitlab-pages-setup/).

A daily [scheduled pipeline](https://docs.gitlab.com/ce/user/project/pipelines/schedules.html)
downloads the Firefox package from mozilla.org and then updates the F-Droid repository (which lives
on gitlab.com pages). All required things are run by Gitlab CI. This repository contains the complete source code.

The private key for signing the repository is kept private, but it's only used for
this purpose. The APKs are still signed by Mozilla.


Donations
=========

If you want to donate, please [donate to Mozilla](https://donate.mozilla.org) instead!

