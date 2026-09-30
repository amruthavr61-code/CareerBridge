from backend.career_data import load_careers


def calculate_match(student_skills, required_skills):
    """
    Calculate how many required skills the student already has.
    Returns a percentage.
    """

    student_skills = {
        skill.strip().lower()
        for skill in student_skills
    }

    required_skills = {
        skill.strip().lower()
        for skill in required_skills
    }

    if not required_skills:
        return 0

    matched_skills = student_skills.intersection(required_skills)

    percentage = (len(matched_skills) / len(required_skills)) * 100

    return round(percentage, 1)


def recommend_careers(student_skills):
    """
    Compare the student's skills with every career
    and return careers ordered by skill match.
    """

    careers = load_careers()
    recommendations = []

    for career_name, career_info in careers.items():

        required_skills = career_info["skills"]

        match_percentage = calculate_match(
            student_skills,
            required_skills
        )

        recommendations.append({
            "career": career_name,
            "match": match_percentage
        })

    recommendations.sort(
        key=lambda x: x["match"],
        reverse=True
    )

    return recommendations