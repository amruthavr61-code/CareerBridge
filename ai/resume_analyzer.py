from pypdf import PdfReader


def extract_resume_text(pdf_file):
    """Extract text from an uploaded PDF resume."""

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()


def find_skills(resume_text, known_skills):
    """Find known skills mentioned in the resume."""

    resume_text_lower = resume_text.lower()

    found_skills = []

    for skill in known_skills:
        if skill.lower() in resume_text_lower:
            found_skills.append(skill)

    return found_skills