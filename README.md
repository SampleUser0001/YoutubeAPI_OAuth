# YoutubeAPI_OAuth

## 準備

1. 下記を参考に、OAuth2.0認証用のjsonファイルを取得しておく。  
    - [Python で OAuth 2.0 認証を通して YouTube Data API を叩いてみた:DevelopersIO](https://dev.classmethod.jp/articles/oauth2-youtube-data-api/)
2. jsonファイルが使用できるように認証しておく
    - [GoogleAPI_OAuth_init_setting](https://github.com/SampleUser0001/GoogleAPI_OAuth_init_setting)を使ってファイルを作成する。
3. app/config配下に1と2で取得したファイルを配置する。
    - 1で作成したファイル -> ファイル名：client_secret.json
    - 2で作成したファイル -> ファイル名：app.py-oauth2.json

## 実行

``` sh
docker-compose up
```

## 参考

- [Python で OAuth 2.0 認証を通して YouTube Data API を叩いてみた:DevelopersIO](https://dev.classmethod.jp/articles/oauth2-youtube-data-api/)
- [動画の評価:YoutubeDataAPI](https://developers.google.com/youtube/v3/code_samples/python?hl=ja#rate__like__a_video)
    - 下記に対してlikeする
    - [https://www.youtube.com/watch?v=L-oNKK1CrnU](https://www.youtube.com/watch?v=L-oNKK1CrnU)