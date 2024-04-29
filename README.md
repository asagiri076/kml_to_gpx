# kml_to_gpx
GoogleマップからKML形式でダウンロードした1日分のタイムライン（ローケーション履歴）を、Lightrooom Classicで読み込めるGPX形式に変換します。

## 動作環境

python3 が動くこと

## 使い方

1. Googleマップのタイムラインを開き、「右下の歯車アイコン」→「この日のデータをKML形式でエクスポート」から1日分のロケーション履歴をダウンロード
2. `python3 kml_to_gpx.py <ダウンロードしたKMLファイルのパス> <出力GPXファイルの保存先パス>`
3. Lightoom Clasiccでマップタブを開き、メニューバーから「マップ」→「トラックログ」→「トラックログの読み込み」を選択し、出力したGPXファイルを読み込む
4. メニューバーから「マップ」→「トラックログ」→「写真に自動タグ付け」を選択し、写真に位置情報を付与する



# kml_to_gpx (English)
Converts a day's worth of location history downloaded in KML format from Google Maps into GPX format, which can be read by Lightroom Classic.

## Operating Environment

Must run on python3

## How to Use

1. Open Google Maps' Your Timeline, click the "gear icon" at the bottom right → "Export this day to KML".
2. `python3 kml_to_gpx.py <path to downloaded KML file> <output path for GPX file>`
3. In Lightroom Classic, open the Map tab, go to the menu bar, select "Map" → "Track Log" → "Load TrackLog", and load the output GPX file.
4. From the menu bar, select "Map" → "TrackLog" → "Auto-Tag Photos" to assign location information to the photos.