from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session-based flash messages

# Email sending function
def send_email(subject, body, to_email):
    from_email = "boikanyokanyo481@gmail.com"  # Replace with your email
    password = "ghvbtskbkzqhwdgz"  # Replace with your email password

    try:
        # Set up the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
        flash('An error occurred while sending your message. Please try again.', 'error')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email']
        message = request.form['message']

        subject = f"New Message from {user_name}"
        body = f"Name: {user_name}\nEmail: {user_email}\n\nMessage:\n{message}"

        # Send the email to your email address
        send_email(subject, body, "boikanyokanyo481@gmail.com")  # Your email address here

        # Flash success message
        flash('Message sent successfully!', 'success')

        return redirect(url_for('index'))  # Redirect to home page after sending message

if __name__ == '__main__':
    app.run(debug=True)
