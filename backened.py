from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get current day of the week
    current_day = datetime.datetime.utcnow().strftime("%A")

    # Get current UTC time
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # GitHub URLs
    github_file_url = "https://github.com/your-username/your-repo/blob/main/file_name.ext"
    github_repo_url = "https://github.com/paragonnoah/stage_HNGX_backen1"

    # Create JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
