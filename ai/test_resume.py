from ai.resume_analyzer import extract_resume_text, find_skills


pdf_path = r"C:\Users\Admin\Downloads\Resume.pdf"


# Read the resume
with open(pdf_path, "rb") as file:
    resume_text = extract_resume_text(file)


# Skills CareerBridge knows about
known_skills = [
    "Python",
    "SQL",
    "Git",
    "GitHub",
    "Java",
    "C",
    "C++",
    "HTML",
    "CSS",
    "JavaScript",
    "React",
    "Django",
    "Flask",
    "NumPy",
    "Pandas",
    "Machine Learning",
    "Data Science",
    "Statistics",
    "Cloud",
    "AWS",
    "Azure",
    "Docker",
]


# Find skills in the resume
found_skills = find_skills(
    resume_text,
    known_skills
)


print("\n===== DETECTED SKILLS =====\n")

for skill in found_skills:
    print("✅", skill)