from flask import Flask, request, render_template
import json
import datetime

app = Flask(__name__)

# Mock Database for storing reported issues
reported_issues = []


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/report_issue', methods=['GET', 'POST'])
def report_issue():
    if request.method == 'POST':
        # Get data from the bug report form
        reporter_name = request.form['reporter_name']
        issue_description = request.form['issue_description']

        # Create a new reported issue
        new_issue = {
            'reporter_name': reporter_name,
            'issue_description': issue_description,
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        # Store the reported issue in the database
        reported_issues.append(new_issue)

        # You can include additional logic here, such as sending email notifications to your security team

        return render_template('thank_you.html', reporter_name=reporter_name)

    return render_template('report_issue.html')


@app.route('/view_reported_issues')
def view_reported_issues():
    return render_template('view_reported_issues.html', reported_issues=reported_issues)


if __name__ == '__main__':
    app.run(debug=True)
