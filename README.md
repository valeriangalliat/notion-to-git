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

Go on [Notion](https://www.notion.so/), in **settings & members** >
**settings**. Open the developer tools in the **network** tab. In
Notion, click **export all workspace content** and run the export with
the settings you want.

In the network tab, you'll see a request to `enqueueTask`. In the
request payload you'll find a `spaceId` property. In the request
**cookies** you'll find `token_v2` and `file_token`.

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
      }
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
