import streamlit as st

from ai.resume_analyzer import extract_resume_text, find_skills
from backend.career_match import recommend_careers
from backend.skill_gap import calculate_skill_gap


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="CareerBridge",
    page_icon="🚀",
    layout="wide"
)

# ==============================
# CUSTOM UI DESIGN
# ==============================

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(135deg, #182848, #4b6cb7);
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 30px;
    margin-bottom: 15px;
}

.card {
    background-color: #161b22;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #30363d;
    margin-bottom: 15px;
}

.success-card {
    background-color: #123524;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #2ecc71;
}

.skill-card {
    background-color: #161b22;
    padding: 15px 20px;
    border-radius: 12px;
    border: 1px solid #30363d;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🚀 CareerBridge</h1>
    <p>AI-Powered Career & Skill Analysis</p>
    <p>
        Upload your resume and discover your skills, suitable career paths,
        and the skills you need to build your future.
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()


# -----------------------------
# KNOWN SKILLS
# -----------------------------

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


# -----------------------------
# RESUME UPLOAD
# -----------------------------

uploaded_file = st.file_uploader(
    "📄 Upload your Resume (PDF)",
    type=["pdf"]
)
# -----------------------------
# RESUME ANALYSIS
# -----------------------------

if uploaded_file is not None:

    # Extract text from uploaded resume
    resume_text = extract_resume_text(uploaded_file)

    # Detect skills
    student_skills = find_skills(resume_text, known_skills)

    st.divider()

    # Show detected skills
    st.subheader("🔍 Detected Skills")

    if student_skills:
        for skill in student_skills:
            st.write("✅", skill)
    else:
        st.warning("No known skills were detected in the resume.")

    # Career recommendations

    # Career recommendations
    st.subheader("🎯 Career Recommendations")

    recommendations = recommend_careers(student_skills)

    for item in recommendations:
        career = item["career"]
        match = item["match"]

        st.markdown(
            f"""
            <div class="card">
                <h3>💼 {career}</h3>
                <p style="font-size:18px;">
                    🎯 <b>{match}% match</b>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Skill gap
    if recommendations:
        selected_career = recommendations[0]["career"]

        st.subheader("📚 Skill Gap Analysis")

        result = calculate_skill_gap(
            student_skills,
            selected_career
        )

        st.write("**Career:**", result["career"])

        st.write("### ✅ Skills you already have")
        for skill in result["matched_skills"]:
            st.write("🟢", skill)

        st.write("### ❌ Skills you need")
        for skill in result["missing_skills"]:
            st.write("🔴", skill)

        st.write(
            "**Readiness:**",
            f"{result['readiness']}%"
        )