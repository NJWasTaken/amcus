# DrDEV_2022
import sys
import logging
import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
app = Flask(__name__)
model = pickle.load(open('COVID19.pkl', 'rb'))
model1=pickle.load(open('AlergyColdCovidReduced.pkl','rb'))
model2=pickle.load(open('DIABETES1.pkl','rb'))
model3=pickle.load(open("CVD.pkl",'rb'))
model4=pickle.load(open('Comprehensive.pkl','rb'))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/covid19")
def covidUI():
    return render_template('COVID19.html')
@app.route('/alergy_flu_cold_covid')
def afccUI():
    return render_template("AlergyColdCovid.html")

@app.route('/diabetes')
def diabetesUI():
    return render_template("Diabetes.html")

@app.route('/cvd')
def cvdUI():
    return render_template("CVD.html")

@app.route('/comprehensive')
def compUI():
    return render_template("Comprehensive.html")


@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/book')
def bookUI():
    return render_template("appoinment.html")

@app.route('/book',methods=['POST'])
def book():
    import smtplib
    dept = request.form['Department']
    slot = request.form['slot']
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    date = request.form['date']
    Dept = dept
    Name= name
    Phone = phone
    Date = str(date)
    Slot = slot
    Message = message
    msge = "Dept: ", Dept,"Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    msge = str(msge)

    # fromMy = 'doctor.dev@yahoo.com'  # fun-fact: "from" is a keyword in python, you can't use it as variable.. did anyone check if this code even works?
    # to = 'noelgjose05@gmail.com'
    # subj = 'Appointment'
    # date = str(date)
    # message_text = msge
    #
    # msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (fromMy, to, subj, date, message_text)
    #
    # username = str('doctor.dev@yahoo.com')
    # password = str('DoctorDave2022')
    #
    # server = smtplib.SMTP("smtp.mail.yahoo.com", 465)
    # server.login(username, password)
    # server.sendmail(fromMy, to, msg)
    # server.quit()
    # print('ok the email has sent ')


    # import smtplib, ssl
    # dept = request.form['Department']
    # date = request.form['date']
    # slot = request.form['slot']
    # name = request.form['name']
    # phone = request.form['phone']
    # message = request.form['message']
    #
    # Dept = dept
    # Name= name
    # Phone = phone
    # Date = str(date)
    # Slot = slot
    # Message = message
    # msge = "Dept: ", Dept,"Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    # msge = str(msge)
    # port = 587  # For starttls
    # smtp_server = "smtp.gmail.com"
    # sender_email = "doctor.dev@yahoo.com"
    # receiver_email = "noelgjose05@gmail.com"
    # password = "DoctorDave2022"
    # message = """\
    # Subject: Hi there
    #
    # This message is sent from Python."""
    #
    # context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)




    # import smtplib
    # dept = request.form['Department']
    # date = request.form['date']
    # slot = request.form['slot']
    # name = request.form['name']
    # phone = request.form['phone']
    # message = request.form['message']
    #
    # Dept = dept
    # Name= name
    # Phone = phone
    # Date = str(date)
    # Slot = slot
    # Message = message
    # msge = "Dept: ", Dept,"Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    # msge = str(msge)
    # Subject = "Patient on " + Date
    # gmail_user = 'doctor.dev@yahoo.com'
    # gmail_password = 'DrDave2022'
    #
    # sent_from = gmail_user
    # to = ['adrushtshetty@gmail.com','noelgjose05@gmail.com','noelg2122.11a@rcis.in']
    # subject = Subject
    # body = msge
    #
    # email_text = """\
    #     From: %s
    #     To: %s
    #     Subject: %s
    #
    #     %s
    #     """ % (sent_from, ", ".join(to), subject, body)
    #
    # smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    # smtp_server.ehlo()
    # smtp_server.login(gmail_user, gmail_password)
    # smtp_server.sendmail(sent_from, to, email_text)
    # smtp_server.close()
    return render_template("Appointment_CONFIRM.html",send_name='{}'.format(Name),send_dept='{}'.format(Dept),send_date='{}'.format(Date),send_slot='{}'.format(Slot))


# @app.route('/trial')
# def trial():
#     return render_template("Comprehensive.html")

@app.route('/',methods=['POST'])
def bookAppointment():
    import smtplib
    dept = request.form['Department']
    slot = request.form['slot']
    name = request.form['name']
    phone = request.form['phone']
    message = request.form['message']
    date = request.form['date']
    Dept = dept
    Name= name
    Phone = phone
    Date = str(date)
    Slot = slot
    Message = message
    msge = "Dept: ", Dept,"Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    msge = str(msge)

    # fromMy = 'doctor.dev@yahoo.com'  # fun-fact: "from" is a keyword in python, you can't use it as variable.. did anyone check if this code even works?
    # to = 'noelgjose05@gmail.com'
    # subj = 'Appointment'
    # date = str(date)
    # message_text = msge
    #
    # msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (fromMy, to, subj, date, message_text)
    #
    # username = str('doctor.dev@yahoo.com')
    # password = str('DoctorDave2022')
    #
    # server = smtplib.SMTP("smtp.mail.yahoo.com", 465)
    # server.login(username, password)
    # server.sendmail(fromMy, to, msg)
    # server.quit()
    # print('ok the email has sent ')


    # import smtplib, ssl
    # dept = request.form['Department']
    # date = request.form['date']
    # slot = request.form['slot']
    # name = request.form['name']
    # phone = request.form['phone']
    # message = request.form['message']
    #
    # Dept = dept
    # Name= name
    # Phone = phone
    # Date = str(date)
    # Slot = slot
    # Message = message
    # msge = "Dept: ", Dept,"Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    # msge = str(msge)
    # port = 587  # For starttls
    # smtp_server = "smtp.gmail.com"
    # sender_email = "doctor.dev@yahoo.com"
    # receiver_email = "noelgjose05@gmail.com"
    # password = "DoctorDave2022"
    # message = """\
    # Subject: Hi there
    #
    # This message is sent from Python."""
    #
    # context = ssl.create_default_context()
    # with smtplib.SMTP(smtp_server, port) as server:
    #     server.ehlo()  # Can be omitted
    #     server.starttls(context=context)
    #     server.ehlo()  # Can be omitted
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message)




    # import smtplib
    # dept = request.form['Department']
    # date = request.form['date']
    # slot = request.form['slot']
    # name = request.form['name']
    # phone = request.form['phone']
    # message = request.form['message']
    #
    # Dept = dept
    # Name= name
    # Phone = phone
    # Date = str(date)
    # Slot = slot
    # Message = message
    # msge = "Dept: ", Dept,"Name: ", Name, "Phone: ", Phone, "Date: ", Date, "Slot: ", Slot, "Message: ", Message
    # msge = str(msge)
    # Subject = "Patient on " + Date
    # gmail_user = 'doctor.dev@yahoo.com'
    # gmail_password = 'DrDave2022'
    #
    # sent_from = gmail_user
    # to = ['adrushtshetty@gmail.com','noelgjose05@gmail.com','noelg2122.11a@rcis.in']
    # subject = Subject
    # body = msge
    #
    # email_text = """\
    #     From: %s
    #     To: %s
    #     Subject: %s
    #
    #     %s
    #     """ % (sent_from, ", ".join(to), subject, body)
    #
    # smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    # smtp_server.ehlo()
    # smtp_server.login(gmail_user, gmail_password)
    # smtp_server.sendmail(sent_from, to, email_text)
    # smtp_server.close()
    return render_template("Appointment_CONFIRM.html",send_name='{}'.format(Name),send_dept='{}'.format(Dept),send_date='{}'.format(Date),send_slot='{}'.format(Slot))


@app.route('/covid19',methods=['POST'])
def covid():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    if prediction[0]==1:
        output="INFECTED"
        msg="Please take care."
    else:
        output="Not Infected"
        msg="Lessgo...!"
    return render_template("COVID_Confirm.html", prediction_text='{}'.format(output),msg_text='{}'.format(msg))

@app.route("/alergy_flu_cold_covid",methods=['POST'])
def afcc():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model1.predict(final_features)
    if prediction[0] == 0:
        output = "Allergy"
        msg = "Its an allergy why don't you get an allergy routine done."
    elif prediction[0]==1:
        output = "Cold"
        msg = "Lessgo...! at least itsn't one from the rest !"
    elif prediction[0]==2:
        output="COVID"
        msg="Please take care."
    elif prediction[0]==3:
        output="Flu"
        msg="Its the flu go to your nearest doctor and get your self a prescription"
    return render_template("afcc_Confirm.html", prediction_text='{}'.format(output), msg_text='{}'.format(msg))

@app.route('/diabetes',methods=['POST'])
def diabetes():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model2.predict(final_features)
    if prediction[0]==0:
        output="Not Diabetic"
        msg="lessgo..."
    elif prediction[0]==1:
        output="Pre Diabetic"
        msg="Take care."
    elif prediction[0]==2:
        output="Diabetic"
        msg="Take care."
    return render_template("DIABETES_Confirm.html", prediction_text='{}'.format(output),msg_text='{}'.format(msg))

@app.route('/cvd',methods=['POST'])
def cvd():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model3.predict(final_features)
    if prediction[0]==0:
        output="SAFE"
        msg="For the next ten years, you are unlikely to have any cardiovascular disease."
    elif prediction[0]==1:
        output="CVD"
        msg="Within the next ten years, you will almost certainly get a CVD. Please exercise cautious and contact your cardiologist right away."
    return render_template("CVD_Confirm.html", prediction_text='{}'.format(output),msg_text='{}'.format(msg))

@app.route('/comprehensive',methods=['POST'])
def comp():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model4.predict(final_features)
    if prediction[0]==15:
        output="Fungal Infection"
        msg="You have a fungal infection."
    elif prediction[0]==4:
        output="Allergy"
        msg="You have an allergy."
    elif prediction[0] == 16:
        output = "GERD"
        msg = "You have a Gastroesophageal reflux disease."
    elif prediction[0]==9:
        output="Chronic cholestasis"
        msg="You have a chronic cholestatic disease."
    elif prediction[0]==33:
        output="Peptic Ulcer Disease"
        msg="You have a peptic ulcer disease."
    elif prediction[0]==14:
        output="Drug Reaction"
        msg="You have a nonallergic hypersensitivity reaction or pseudoallergic drug reaction."
    elif prediction[0]==1:
        output="AIDS"
        msg="You have AIDS."
    elif prediction[0]==12:
        output="Diabetes"
        msg="You have diabetes."
    elif prediction[0]==17:
        output="Gastroenteritis"
        msg="You have a stomach flu/gastroenteritis."
    elif prediction[0]==6:
        output="Bronchial Asthma"
        msg="You have bronchial asthma."
    elif prediction[0]==23:
        output="Hypertension"
        msg="You have hypertension."
    elif prediction[0]==30:
        output="Migrane"
        msg="You have a migrane."
    elif prediction[0]==7:
        output="Cervical Spondylosis"
        msg="You have cervical spondylosis."
    elif prediction[0]==32:
        output="Paralysis/Brain Hemorrhage"
        msg="You have brain hemorrhage."
    elif prediction[0]==28:
        output="Jaundice"
        msg="You have jaundice."
    elif prediction[0]==29:
        output="Malaria"
        msg="You have malaria."
    elif prediction[0]==8:
        output="Chicken Pox"
        msg="You have chicken pox."
    elif prediction[0]==11:
        output="Dengue"
        msg="You have dengue."
    elif prediction[0]==37:
        output="Typhoid"
        msg="You have typhoid."
    elif prediction[0]==40:
        output="Hepatitis A"
        msg="You have Hepatitis A."
    elif prediction[0]==19:
        output="Hepatitis B"
        msg="You have Hepatitis B."
    elif prediction[0]==20:
        output="Hepatitis C"
        msg="You have Hepatitis C."
    elif prediction[0]==21:
        output="Hepatitis D"
        msg="You have Hepatitis D."
    elif prediction[0]==22:
        output="Hepatitis E"
        msg="You have Hepatitis E."
    elif prediction[0]==3:
        output="Alcoholic Hepatitis"
        msg="You have alcoholic Hepatitis."
    elif prediction[0]==36:
        output="Tuberculosis"
        msg="You have tuberculosis."
    elif prediction[0]==10:
        output="Common cold"
        msg="You have common cold."
    elif prediction[0]==34:
        output="Pneumonia"
        msg="You have pneumonia."
    elif prediction[0]==13:
        output="Piles"
        msg="You have piles."
    elif prediction[0]==18:
        output="Heart Attack"
        msg="You are prone to a heart attack."
    elif prediction[0]==39:
        output="Varicose veins"
        msg="You have varicose veins."
    elif prediction[0]==26:
        output="Hypothyroidism"
        msg="You have Hypothyroidism."
    elif prediction[0]==24:
        output="Hyperthyroidism"
        msg="You have Hyperthyroidism."
    elif prediction[0]==25:
        output="Hypoglycemia"
        msg="You have low blood sugar levels."
    elif prediction[0]==31:
        output="Osteoarthritis"
        msg="You have osteoarthritis."
    elif prediction[0]==5:
        output="Arthritis"
        msg="You have arthritis."
    elif prediction[0]==0:
        output="Vertigo"
        msg="You have vertigo."
    elif prediction[0]==2:
        output="Acne"
        msg="You have Acne."
    elif prediction[0]==38:
        output="Urinary tract infection"
        msg="You have a urinary tract infection"
    elif prediction[0]==35:
        output="Psoriasis"
        msg="You have psoriasis."
    elif prediction[0]==27:
        output="Impetigo"
        msg="You have impetigo."
    return render_template("Comp_CONFIRM.html", prediction_text='{}'.format(output),msg_text='{}'.format(msg))


if __name__ == '__main__':
    app.run(debug=True)