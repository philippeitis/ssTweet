[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

#### About
ssTweet is a twitter bot which would upload the screenshot of every tweet in a thread to Google Photos.

#### sorted stuff that can be reused
1. Wrote a Python client library for dealing with Google Photos API. Explore the Media and Authorization classes inside the src folder for easy access to almost all functions related to uploading stuff over Photos and creating albums.


#### contributions
* If you see my code getting devaiated from the [Python Coding Style Guide](https://www.python.org/dev/peps/pep-0008/). Please raise an issue or submit a pull request.
* If you see something that could have been more Pythonic or something that violates the rule of keeping it simple. Please raise an issue or change it yourself.

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
- [ ] Get the `url_list` of every tweet in a thread from the URL of first tweet.
- [ ] Generate screenshot of every tweet in a thread and upload to Photos.
- [ ] Directly write the image to Google Photos instead of saving & uploading to save up on space.
- [ ] Verify the ssTweet app with Google Photos to avoid unsafe error.
- [ ] Instead of a tweet, make a `cli` tool first with a local DB.
- [ ] Work on a simple website where users could connect their twitter and Google Photos account
- [ ] Design the database needed to store the Photos `authentication_token` in encrypted format from Photos app and map them with Twitter usernames.
- [ ] Convert the library to a twitter bot
- [ ] Unroll the contents of the entire thread and upload a single screenshot with text of entire thread.
- [ ] too much pending shit, already!

### APIs used
> Google Photos API, Twitter API, Google PageSpeed Insights API
