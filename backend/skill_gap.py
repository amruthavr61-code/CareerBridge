from backend.career_data import get_career


def calculate_skill_gap(student_skills, career_name):
    """
    Compare student skills with the skills required
    for the selected career.
    """

    career = get_career(career_name)

    if career is None:
        return {
            "error": "Career not found"
        }

    required_skills = career["skills"]

    # Convert to lowercase for comparison
    student_skills_lower = {
        skill.strip().lower()
        for skill in student_skills
    }

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in student_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    total_skills = len(required_skills)

    if total_skills > 0:
        readiness = (len(matched_skills) / total_skills) * 100
    else:
        readiness = 0

    return {
        "career": career_name,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "readiness": round(readiness, 1),
        "total_required": total_skills
    }