### About
ssTweet is a twitter bot which would upload the screenshot of every tweet in a thread to Google Photos.

### To-do
- [x] Write a quick python module to prove the concept if everything works as expected. hard code most of the things.
- [x] Write a python module to give url and generate screenshot to local machine.
- [x] Write a python module to upload an image to Google Photos from a locally stored image.
- [ ] Solve the issue for authenticating account every time uploading a photo to Photos.
- [ ] Get the `url_list` of every tweet in a thread from the URL of first tweet.
- [ ] Generate screenshot of every tweeet in a thread and upload to Photos.
- [ ] Directly write the image to Google Photos instead of saving & uploading to save up on space.
- [ ] Verify the ssTweet app with Google Photos to avoid unsafe error.
- [ ] Instead of a tweet, make a `cli` tool first with a local DB.
- [ ] Work on a simple website where users could connect their twitter and Google Photos account
- [ ] Design the database needed to store the Photos `authentication_token` in encrypted format from Photos app and map them with Twitter usernames.
- [ ] Convert the library to a twitter bot
- [ ] Unroll the contents of the entire thread and upload a single screenshot with text of entire thread.
- [ ] too much shit, already!

### APIs used
Google Photos API, Twitter API, Google PageSpeed Insights API
