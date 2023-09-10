import fastapi
import datetime
import json

app = fastapi.FastAPI()

@app.get("/get_info")
def get_info(slack_name: str, track: str):
  slack_name = "Ongaro"
  track = "Backend"
  current_day = datetime.datetime.now().strftime("%A")
  utc_time = datetime.datetime.now().utcnow().isoformat()
  github_file_url = "https://github.com/username/repo/blob/main/file_name.ext"
  github_repo_url = "https://github.com/username/repo"

  info = {
    "slack_name": slack_name,
    "current_day": current_day,
    "utc_time": utc_time,
    "track": track,
    "github_file_url": github_file_url,
    "github_repo_url": github_repo_url,
    "status_code": 200
  }

  return json.dumps(info)
