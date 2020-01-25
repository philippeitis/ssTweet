import logging
response = {
    "newMediaItemResults": [
        {
            "uploadToken": "CAISiQMASsyg4ILvrndT4YYkO8u3yuStoxlg5sS3FGH0965npayPvnuwxiMkvJyx6CE8lWVqTDp078XGgOJm77iLHlqY/RCJjue6cL2phdH87mD84p+q6JaSlUE41EirWEWIMQttR+iaA/yMJP1CU1QYTZIhNGT5uwm5F1kuhB3fQgnt7cINIemkJCcx7TrSNb4MnJ5rD/etccu4iL70d9BBNoRQDA8ZkG1a5OMzmHQO9/HKCFuuKO4p/xA9Lwm7hf4SzUCVPy5Qldve1slBOcW9lOGcPu/N8MnecArYVwvrNpOad6HKF8OL8VX8aUspQMS7IspHYO3U3z9Ko5K0nQmjTXWKX54FRGTSCNvrok0h83JkKYyBVPJAnjZDKQRcWZJC62Yw/KqrXDi/x0iEKswykZOKMcM2w7e22lzN6dwRXa2T++DhT8Esc2RHSIZlf15IY3oXRXe/tQEQWHhzLagYNilz9OWqu1GltR0Gm7AxAISOxL5kdfENGoo1AK32umlkp0zSbvprlkBBSm0",
            "status": {
                "message": "Success"
            },
            "mediaItem": {
                "id": "AJ8vYPxmpS9UJ7hvaDs2vjaRCsWcNJIOxHj_6_56E7iP5-wqhUAwyieCTdQWLN8gU_P6GQutqXwrdfnlRC-e28YmSdcqVObD-A",
                "productUrl": "https://photos.google.com/lr/album/AJ8vYPyBDjfnt95M_g-UYrtuiz-PE3btEkMyaCiN9S9NsAjQC-1n8VUr38ZpM7vSBpZi6TCm640w/photo/AJ8vYPxmpS9UJ7hvaDs2vjaRCsWcNJIOxHj_6_56E7iP5-wqhUAwyieCTdQWLN8gU_P6GQutqXwrdfnlRC-e28YmSdcqVObD-A",
                "mimeType": "image/jpeg",
                "mediaMetadata": {
                    "creationTime": "2020-01-24T21:48:48Z",
                    "width": "320",
                    "height": "568"
                },
                "filename": "sample_tweet.jpg"
            }
        }
    ]
}
def log_upload_activity(response, photo_name):
    logging.debug('response: {0}'.format(response))
    if('newMediaItemResults' in response):
        status = response['newMediaItemResults'][0]['status']
        if(status.get('code') and (status.get('code') > 0)):
            logging.error('could not add {photo_name} to the album. message: {message}'.format(photo_name=photo_name, message=status['message']))
        else:
            logging.info('Added {photo_name} to your album'.format(photo_name=photo_name))
    else:
        logging.error('couldnot add your photo to the album you requested')

