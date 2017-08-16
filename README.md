
Firefox F-Droid repo (inofficial)
=================================

Add this URL to F-Droid: `https://rfc2822.gitlab.io/fdroid-firefox/fdroid/`

![Repo URL QRcode](public/repo-qrcode.png)


How does it work?
=================

A daily [scheduled pipeline](https://docs.gitlab.com/ce/user/project/pipelines/schedules.html)
downloads the Firefox package from mozilla.org and then updates the F-Droid repository. All
required things are run by Gitlab CI. This repository contains the complete source code.

The private key for signing the repository is kept private, but it's only used for
this purpose. The APKs are still signed by Mozilla.
