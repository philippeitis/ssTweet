[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

#### About
ssTweet is a twitter bot which would upload the screenshot of every tweet in a thread to Google Photos.

#### Setting Up the project
After cloning the repo, you should create a new virtual env and install all dependencies from `requirements.txt` then create access_tokens from `twitter_developers` + access_tokens from `google_developers` and add them to two seperate files called `config.py` and `gphotos_keys.json` respectively. This is how both the files should look like:
1. `config.py`
    ```
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_KEY = ""
    ACCESS_SECRET = ""
    ```
2. `gphotos_keys.json`
    ```
    {
    "installed":
        {
            "client_id":"",
            "client_secret":"",
            "auth_uri":"https://accounts.google.com/o/oauth2/auth",
            "token_uri":"https://www.googleapis.com/oauth2/v3/token",
            "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
            "redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]
        }
    s}
    ```
Now, Just run `main.py`

#### To-do
- [x] Write a quick python module to prove the concept if everything works as expected. hard code most of the things.
- [x] Write a python module to give url and generate screenshot to local machine.
- [x] Write a python module to upload an image to Google Photos from a locally stored image.
- [x] Mix up the two modules to generate & upload in one go.
- [ ] Improve the code quality, darling.
    - [x] Log every step into a log file as the code runs using the log module.
    - [x] Classes for Albums, Users, Photos, Tweet Authors.
    - [ ] Add unit tests.
- [ ] Solve the issue for authenticating account every time uploading a photo to Photos using `refresh_tokens`
- [x] Get the `url_list` of every tweet in a thread from the URL of first tweet.
- [x] Generate screenshot of every tweet in a thread and upload to Photos.
- [ ] Directly write the image to Google Photos instead of saving & uploading to save up on space.
- [ ] Verify the ssTweet app with Google Photos to avoid unsafe error.
- [x] Instead of a tweet, make a `cli` tool first with a local DB.
- [ ] Work on a simple website where users could connect their twitter and Google Photos account
- [ ] Design the database needed to store the Photos `authentication_token` in encrypted format from Photos app and map them with Twitter usernames.
- [ ] Convert the library to a twitter bot
- [ ] Unroll the contents of the entire thread and upload a single screenshot with text of entire thread.