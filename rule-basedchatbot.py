from flask import Flask, request, render_template

app =  Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    reply = ""


    if request.method == 'POST':
        user_msg = request.form["message"] . lower()

        if user_msg == "hi":
            reply = "Hello! How can I assist you today?"
        elif user_msg == "eligibility":
            reply = "you need atleast 50% in your academics."
        elif user_msg == "application process":
            reply = "You can apply online through our website."
        elif user_msg == "fees":
            reply = "The fee structure varies by program. Please visit our fees page for details."
        elif user_msg == "documents required":
            reply = "you need your marksheets, identity proof, and photos."
        elif user_msg == "contact information":
            reply = "You can contact us at 9876543210."
        else:
            reply = "I'm sorry, I don't understand your question. Please try asking something else."
    return render_template('index.html', reply=reply)

app.run(debug=True)