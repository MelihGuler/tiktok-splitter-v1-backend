# Suggestions

## Virtual Environment
It would be good to use virtual environment for the project dependencies.

Following command will create a virtual environment named as venv.
```bash
python -m venv venv
```

After virtual environment created, run following command to activate virtual environment

```bash
.\venv\Scripts\activate 
```

Now you should see (venv) text on the left side of your teminal. If you see that text, you are successfully activated the virtual environment. Now you can go with following steps... 

You can see [this](https://docs.python.org/3/library/venv.html) page for detailed information about virtual environment.

## Browser
If you don't have mozilla firefox on your computer you have to install it to use application. Otherwise, application will give error, when you request to the endpoints. You can install firefox from [here](https://www.mozilla.org/en-US/firefox/new/).

# How to run
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

Get into project directory and
 run following code on your terminal to install dependencies

```bash
pip install -r requirements.txt
```

## Run

After everything installed successfully. Run following command to run application.

```bash
python app.py
```

# Usage
Use postman or equivalent application to make requests.
Application port = 8080

## Get Full Tiktok Video
[POST] http://localhost:8080/api/video/tiktok
Body - Raw Json
```json
{
    "video_url": "YOUR_TIKTOK_VIDEO_URL"
}
```
## Split
[POST] http://localhost:8080/api/video/split/tiktok
Body - Raw Json
```json
{
    "video_url": "YOUR_TIKTOK_VIDEO_URL",
    "part_length": 5 // Positive integer. Unit: Seconds
}
```
