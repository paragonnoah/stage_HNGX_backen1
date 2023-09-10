# HNGx inetrnship backed 1

Endpoint Creation: Provide a publicly accessible endpoint.

GET Parameters: The endpoint should accept two GET request query parameters: slack_name and track.
       E.g.: http://example.com/api?slack_name=example_name&track=backend.
       
Slack Name: The response should include the slack_name passed as a GET request query parameter.

Current Day of the Week: Display the current day of the week in full (e.g., Monday, Tuesday, etc.).

Current UTC Time: Return the current UTC time, accurate within a +/-2 minute window.

Track: The response should display the track of the you signed up for (Backend). This will be based on the track GET parameter passed to the endpoint.

GitHub File URL: Include a direct link to the specific file in the GitHub repository that's being executed.

GitHub Repo URL: Include a link to the main page of the GitHub repository containing the project's entire source code.

Status Code: Return 200 as Integer.

JSON Format: The endpoint's response should adhere to the specified JSON format
