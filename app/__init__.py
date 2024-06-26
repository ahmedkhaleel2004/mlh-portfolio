import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

name = "Ahmed Khaleel"


@app.route('/')
def index():
    return render_template('index.html', title="Ahmed Khaleel - MLH Fellow", current_page="home", url=os.getenv("URL"))


@app.route('/education')
def education():

    education = [
        {'school': 'McMaster University',
            'degree': 'B.Eng. Computer Engineering', 'duration': 'Sep 2022 - Apr 2027', 'description': "Pursuing a Bachelor's degree in Computer Engineering, focusing on software development, machine learning, and system design. Engaged in various projects and extracurricular activities to enhance practical skills alongside academic knowledge. Activities and societies: DeltaHacks, Google Developer Student Clubs, McMaster Engineering Competition, McMaster AI Society, McMaster Competitive Programming", 'tags': ["Python", "C++", "Software Design", "C", "Verilog", "3D Printing", "MATLAB", "Autodesk Inventor", "Biomedical Engineering"], 'img': './static/img/mcmaster.webp'},
        {'school': 'IBDP / Ancaster High School',
         'degree': 'Ontario Secondary School Diploma (OSSD) & IB Diploma', 'duration': 'Sep 2018 - May 2022', 'description': "Completed the Ontario Secondary School Diploma (OSSD) and the International Baccalaureate (IB) Diploma at Ancaster High School. The rigorous IB curriculum developed my analytical skills, critical thinking, and understanding of global issues, alongside fostering strong academic writing and research capabilities.", 'tags': ["Critical Thinking", "Teamwork", "Time Management", "Problem Solving", "Adaptability", "Communication", "Leadership", "Creativity", "Research & Analysis", "Ethical Understanding"], 'img': './static/img/ahs.png'}
    ]

    return render_template('education.html', name=name, title="Education", education=education)


@app.route('/work_experiences')
def work_experiences():
    work_experiences = [
        {'company': 'McMaster Artificial Intelligence Society', 'position': 'Workshop Developer', 'duration': 'Jan 2024 - Present',
            'description': "Developed technical workshops on core Machine Learning concepts using Python for 100+ students. Wrote a reusable template with TensorFlow teaching students how to build Convolutional Neural Networks (CNN's). Instructed students on data handling tasks like cleaning, preprocessing, and feature selection using Pandas, along with model architecture. Conducted live coding demonstrations on Google Colab enabling attendees to follow along in real time.", 'tags': ["Neural Networks", "Teaching", "Scikit-Learn", "Convolutional Neural Networks (CNN's)", "Python", "Machine Learning", "TensorFlow", "Artificial Intelligence", "Deep Learning", "Leadership"]}
    ]
    return render_template('work_experiences.html', name=name, title="Work Experiences", work_experiences=work_experiences)


@app.route('/hobbies')
def hobbies():
    hobbies = [
        {
            "activity": "Keyboards / Typing",
            "desc": "It shouldn't be too surprising that a Software Engineer is good at typing, but for me it has become a hobby. I've build custom mechanical keyboards at this point and am super interested in the certain switches and keys that are involved. Personally, I'm super into performance and I have achieved a typing speed of 171+ wpm.",
            "img": "./static/img/keyboard.jpg"
        },
        {
            "activity": "PC Hardware / Setups",
            "desc": "I've always been interested in the latest and greatest tech gadgets. I've built my own PC and have been following the tech industry for a while now. I'm always looking for the best performance and the best value for my money. As I continue my journey as a student and Software Engineer, I'm planning to create a hybrid MacBook / PC setup in the near future.",
            "img": "./static/img/setup.jpg"
        },
        {
            "activity": "Gym / Walking",
            "desc": "I've been going to the gym for a while now and I've seen significant improvements in my physical and mental health. I also enjoy going for walks and hikes in nature. It's a great way to relax and take a break from the digital world. I've recently discovered many beautiful trails in Hamilton and I'm excited to explore more.",
            "img": "./static/img/nature.jpg"
        }
    ]

    return render_template('hobbies.html', name=name, title="Hobbies", hobbies=hobbies)


@app.route('/map')
def map():
    return render_template('map.html', name=name, title="Map")
