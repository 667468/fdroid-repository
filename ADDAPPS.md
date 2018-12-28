# How to add new apps

## Step 1

Add a new metadata file in `fdroid/metadata`  
Use existing files as a reference or take a look here: [F-Droid Metadata Reference](https://f-droid.org/en/docs/Build_Metadata_Reference/)

## Step 2

Add new download information in [apks.json](../blob/master/apks.json):

```json
{
  "baseUrl": "https://example.org/download/App-{ver}-{arch}.apk",
  "architectures": ["arm", "x86"],
  "version": {
    "url": "https://example.org/versions.json",
    "json": [0, "version"]
  },
  "ignoreErrors": false
}
```

Everything except `baseUrl` is optional.  
`{ver}` and `{arch}` will get automatically replaced with the corresponding version and all architectures.  
Note that you can use a single `regex` string instead of `json` to query the version.