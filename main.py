from backend.career_match import recommend_careers
from backend.skill_gap import calculate_skill_gap
from ai.resume_analyzer import extract_resume_text, find_skills

# Known skills that CareerBridge can detect
known_skills = [
    "Python",
    "SQL",
    "Git",
    "GitHub",
    "C",
    "Java",
    "HTML",
    "CSS",
    "JavaScript",
    "Machine Learning",
    "Data Analysis",
    "NumPy",
    "Pandas"
]

# Resume PDF
pdf_path = input("Enter the path of your resume PDF: ")

# Extract text from resume
with open(pdf_path, "rb") as file:
    resume_text = extract_resume_text(file)

# Detect skills from resume
student_skills = find_skills(resume_text, known_skills)

print("\n===== DETECTED SKILLS =====")

for skill in student_skills:
    print("✓", skill)


print("\n===== CAREER RECOMMENDATIONS =====")

recommendations = recommend_careers(student_skills)

for item in recommendations:
    print(
        f"{item['career']} : "
        f"{item['match']}% match"
    )


print("\n===== SKILL GAP =====")

selected_career = "Machine Learning Engineer"

result = calculate_skill_gap(
    student_skills,
    selected_career
)

print("Career:", result["career"])

print("\nSkills you already have:")
for skill in result["matched_skills"]:
    print("✅", skill)

print("\nSkills you need:")
for skill in result["missing_skills"]:
    print("❌", skill)

print("\nReadiness:", result["readiness"], "%")