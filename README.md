# Notion to Git

> Backs up a Notion workspace to a Git repository.

## Dependencies

```sh
apt install unzip jq
brew install jq
```

## Usage

Clone this repository.

```sh
git clone https://github.com/valeriangalliat/notion-to-git
cd notion-to-git
```

Go on [Notion](https://www.notion.so/), in **Settings & members > Settings**.
Open the developer tools in the **Network** tab. In Notion, click
**Export all workspace content** and run the export with the settings
you want.

In the network tab, you'll see a request to `enqueueTask`. In the
request payload you'll find a `spaceId` property. In the request
**cookies** you'll find `token_v2` and `file_token`.

If you don't find the `file_token`, check the **Storage** or
**Application** tab for more cookies!

With those 3 variables, create a `.env` file like so:

```sh
API_TOKEN='{{ token_v2 }}'
FILE_TOKEN='{{ file_token }}'
TASK='{
  "task": {
    "eventName": "exportSpace",
    "request": {
      "spaceId": "{{ spaceId }}",
      "exportOptions": {
        "exportType": "markdown",
        "timeZone": "America/Toronto",
        "locale": "en"
      },
      "shouldExportComments": false
    }
  }
}'
```

Create an empty Git repo in a `notion` subdirectory.

```sh
mkdir notion
git -C notion init
```

Then run the following commands:


```sh
# Generate and download your Notion archive
./export

# Validate and extract the archive
./extract

# Commit the newly extracted export to the Git repo
./commit
```

Feel free to add the remote of your choice to that Git repository and
push it after those steps.

## Refreshing the tokens

If you need to refresh the tokens, go on Notion in your browser, and in
the developer tools, go to the **Storage** or **Application** tab and
list the cookies directly there.

Check for `token_v2` and `file_token` and put them respectively in the
`.env` file in `API_TOKEN` and `FILE_TOKEN`.

It seems to matter that the token is _not_ URL encoded, e.g. `API_TOKEN`
starts with `v02:user_token_or_cookies:` and not
`v02%3Auser_token_or_cookies%3A`, and `FILE_TOEN` starts with `1:` and
not `1%3A`.

## Debug mode

If it doesn't work, you can try debug mode to inspect the full responses
from the Notion API:

```sh
DEBUG=1 ./export
```
