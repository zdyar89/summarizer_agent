import os
from dotenv import load_dotenv
from os.path import join, dirname
import googleapiclient.errors
import google_auth_oauthlib.flow
import googleapiclient.discovery

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

youtube_key = os.environ.get("YOUTUBE_API_KEY")

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secrets.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, SCOPES)
    print(flow.__dict__)
    credentials = flow.run_local_server()

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    video_ids = []
    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PLy0Eq9J9QpuheNMasuzlpjY3ha9Jr-gDN',
        maxResults=50
    )

    while request:
        response = request.execute()

        for item in response['items']:
            video_ids.append(item['contentDetails']['videoId'])

        request = youtube.playlistItems().list_next(request, response)

    print(video_ids)

    for id in video_ids:
        with open(f"./video_summaries/{id}", 'w') as video:
            video.write(id['contentDetails'])

if __name__ == "__main__":
    main()
