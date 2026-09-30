import streamlit as st

from database.database import create_tables
from database.models import add_student

from ai.resume_analyzer import extract_resume_text, find_skills
from backend.career_match import recommend_careers
from backend.skill_gap import calculate_skill_gap
from backend.career_data import get_career


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="CareerBridge",
    page_icon="🚀",
    layout="wide"
)

create_tables()

# =========================================================
# CUSTOM DESIGN
# =========================================================

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

.title {
    font-size: 42px;
    font-weight: bold;
    color: #19b5ff;
}

.subtitle {
    font-size: 18px;
    color: #dddddd;
}

.hero {
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(135deg, #0072ff, #00c6ff);
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
}

.card {
    background-color: #161b22;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #30363d;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

if "name" not in st.session_state:
    st.session_state.name = ""

if "skills" not in st.session_state:
    st.session_state.skills = []

if "interests" not in st.session_state:
    st.session_state.interests = []

if "career" not in st.session_state:
    st.session_state.career = ""

if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🚀 CareerBridge")

st.sidebar.write(
    "AI-Powered Student Career Guidance Platform"
)

st.sidebar.divider()

if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.page = "home"

if st.sidebar.button("👤 Student Profile", use_container_width=True):
    st.session_state.page = "profile"

if st.sidebar.button("📊 Dashboard", use_container_width=True):
    st.session_state.page = "dashboard"

if st.sidebar.button("📄 Resume Analysis", use_container_width=True):
    st.session_state.page = "resume"


# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">
        <h1>🚀 CareerBridge</h1>
        <p><b>AI-Powered Career & Skill Analysis</b></p>
        <p>
        Discover your skills, identify career opportunities,
        find skill gaps and build your career roadmap.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Discover Your Career Path")

    st.write(
        "CareerBridge helps students understand their skills, "
        "identify skill gaps, explore careers and follow a "
        "personalized learning roadmap."
    )

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>📊 Skill Analysis</h3>
        <p>
        Understand your current skills and identify
        areas for improvement.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>🎯 Career Guidance</h3>
        <p>
        Discover career paths based on your
        skills and interests.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>🗺️ Learning Roadmap</h3>
        <p>
        Follow a step-by-step path toward
        your career goal.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("How CareerBridge Works")

    steps = [
        "Create your student profile",
        "Upload your resume",
        "Detect your skills",
        "Get career recommendations",
        "Identify your skill gaps",
        "Follow your learning roadmap",
        "Explore jobs and internships"
    ]

    for number, step in enumerate(steps, 1):
        st.write(f"**{number}. {step}**")

    st.write("")

    if st.button(
        "🚀 Get Started",
        type="primary",
        use_container_width=True
    ):
        st.session_state.page = "profile"
        st.rerun()


# =========================================================
# STUDENT PROFILE
# =========================================================

elif st.session_state.page == "profile":

    st.markdown(
        '<div class="title">Student Profile</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter your details to create your career profile."
    )

    st.subheader("Student Information")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    college = st.text_input("College / University")
    course = st.text_input("Course")

    year = st.selectbox(
        "Year of Study",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]
    )

    st.divider()

    st.subheader("Select Your Skills")

    skills = st.multiselect(
        "Choose your current skills",
        [
            "No skills",
            "Python",
            "Java",
            "C",
            "C++",
            "HTML",
            "CSS",
            "JavaScript",
            "SQL",
            "Git",
            "Communication",
            "Problem Solving",
            "Teamwork",
            "Leadership",
            "Data Analysis",
            "Machine Learning",
            "Networking"
        ]
    )

    st.info(
        "If you don't have any skills yet, select 'No skills'."
    )

    st.divider()

    st.subheader("Select Your Interests")

    interests = st.multiselect(
        "Choose your interests",
        [
            "Web Development",
            "App Development",
            "Data Science",
            "Artificial Intelligence",
            "Cyber Security",
            "Cloud Computing",
            "Networking",
            "Software Development",
            "UI/UX Design",
            "Game Development"
        ]
    )

    st.divider()

    st.subheader("Choose Your Target Career")

    career = st.selectbox(
        "Target Career",
        [
            "Software Developer",
            "Web Developer",
            "Data Analyst",
            "Data Scientist",
            "AI/ML Engineer",
            "Cyber Security Analyst",
            "Cloud Engineer",
            "Network Engineer",
            "UI/UX Designer",
            "Mobile App Developer"
        ]
    )

    st.write("")

    if st.button(
            label="💾 Save Profile",
            type="primary",
            use_container_width=True
    ):

        if name == "":
            st.error("Please enter your name.")

        elif email == "":
            st.error("Please enter your email.")

        elif len(skills) == 0:
            st.error("Please select a skill or choose 'No skills'.")

        elif len(interests) == 0:
            st.error("Please select at least one interest.")

        else:
            if "No skills" in skills:
                skills = ["No skills"]

            # Save student to database
            add_student(
                name,
                email,
                ", ".join(skills),
                career
            )

            st.session_state.name = name
            st.session_state.skills = skills
            st.session_state.interests = interests
            st.session_state.career = career

            st.success("Profile saved successfully!")

            st.session_state.page = "dashboard"

            st.rerun()


# =========================================================
# DASHBOARD
# =========================================================

elif st.session_state.page == "dashboard":

    name = st.session_state.name
    skills = st.session_state.skills
    interests = st.session_state.interests
    career = st.session_state.career

    if name == "":
        st.warning("Please create your Student Profile first.")
        st.stop()

    st.markdown(
        f'<div class="title">Welcome, {name} 👋</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Here is your personalized CareerBridge dashboard."
    )

    st.divider()

    st.subheader("Profile Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Skills", len(skills))

    with col2:
        st.metric("Interests", len(interests))

    with col3:
        st.metric("Target Career", career)

    st.divider()

    st.subheader("Your Current Skills")

    if "No skills" in skills:

        st.warning(
            "You have not selected any skills yet."
        )

    else:

        for skill in skills:
            st.success(skill)

    st.divider()

    # -----------------------------------------------------
    # MEMBER 1 SKILL GAP
    # -----------------------------------------------------

    st.subheader("📊 Skill Gap Analysis")

    career_skills = {

        "Software Developer": [
            "Python",
            "Java",
            "SQL",
            "Git",
            "Problem Solving"
        ],

        "Web Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "SQL"
        ],

        "Data Analyst": [
            "Python",
            "SQL",
            "Excel",
            "Statistics",
            "Data Visualization"
        ],

        "Data Scientist": [
            "Python",
            "SQL",
            "Statistics",
            "Machine Learning",
            "Data Visualization"
        ],

        "AI/ML Engineer": [
            "Python",
            "Statistics",
            "Machine Learning",
            "SQL",
            "Deep Learning"
        ],

        "Cyber Security Analyst": [
            "Networking",
            "Linux",
            "Python",
            "Cyber Security",
            "Ethical Hacking"
        ],

        "Cloud Engineer": [
            "Linux",
            "Networking",
            "Python",
            "Cloud Computing",
            "AWS"
        ],

        "Network Engineer": [
            "Networking",
            "Linux",
            "Routing",
            "Switching",
            "Security"
        ],

        "UI/UX Designer": [
            "UI Design",
            "UX Design",
            "Figma",
            "Prototyping",
            "Communication"
        ],

        "Mobile App Developer": [
            "Java",
            "Kotlin",
            "Android",
            "UI Design",
            "SQL"
        ]
    }

    required_skills = career_skills.get(career, [])

    if "No skills" in skills:

        missing_skills = required_skills

    else:

        missing_skills = [
            skill
            for skill in required_skills
            if skill not in skills
        ]

    if len(missing_skills) > 0:

        st.warning(
            f"You have {len(missing_skills)} "
            f"skill gaps for {career}."
        )

        for skill in missing_skills:
            st.write("🔸", skill)

    else:

        st.success(
            "You have all the listed core skills!"
        )

    st.divider()

    # -----------------------------------------------------
    # ROADMAP
    # -----------------------------------------------------

    st.subheader("🗺️ Your Learning Roadmap")

    roadmap = [
        "Learn programming fundamentals",
        "Learn databases and SQL",
        "Learn the skills required for your career",
        "Build 2-3 practical projects",
        "Improve problem-solving skills",
        "Create your resume and portfolio",
        "Apply for internships and jobs"
    ]

    for number, step in enumerate(roadmap, 1):

        st.info(
            f"Step {number}: {step}"
        )

    st.divider()

    # -----------------------------------------------------
    # JOBS
    # -----------------------------------------------------

    st.subheader("💼 Jobs & Opportunities")

    jobs = [
        (
            "Software Development Intern",
            "Tech Solutions",
            "Bangalore"
        ),

        (
            "Python Developer Intern",
            "Innovation Labs",
            "Remote"
        ),

        (
            "Web Development Intern",
            "Digital Works",
            "Bangalore"
        )
    ]

    for title, company, location in jobs:

        with st.container(border=True):

            st.write(f"### {title}")
            st.write(f"Company: {company}")
            st.write(f"Location: {location}")

            st.button(
                "View Opportunity",
                key=title
            )


# =========================================================
# RESUME ANALYSIS — YOUR PART
# =========================================================

elif st.session_state.page == "resume":

    st.markdown(
        '<div class="title">📄 Resume Analysis</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Upload your resume to automatically detect your skills "
        "and discover suitable career paths."
    )

    st.divider()

    # -----------------------------------------------------
    # KNOWN SKILLS
    # -----------------------------------------------------

    known_skills = [
        "Python",
        "SQL",
        "Git",
        "GitHub",
        "C",
        "Java",
        "C++",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Django",
        "NumPy",
        "Pandas",
        "Machine Learning",
        "Data Analysis",
        "Statistics",
        "Networking",
        "Linux",
        "Cybersecurity",
        "Cryptography",
        "AWS",
        "Docker",
        "Figma",
        "UI Design",
        "UX Design"
    ]

    # -----------------------------------------------------
    # UPLOAD RESUME
    # -----------------------------------------------------

    uploaded_file = st.file_uploader(
        "📄 Upload your Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        # Extract text
        resume_text = extract_resume_text(uploaded_file)

        # Detect skills
        student_skills = find_skills(
            resume_text,
            known_skills
        )

        # Save skills
        st.session_state.resume_skills = student_skills

        st.divider()

        # -------------------------------------------------
        # DETECTED SKILLS
        # -------------------------------------------------

        st.subheader("🔍 Detected Skills")

        if student_skills:

            for skill in student_skills:
                st.write("✅", skill)

        else:

            st.warning(
                "No known skills were detected in the resume."
            )

        # -------------------------------------------------
        # CAREER RECOMMENDATIONS
        # -------------------------------------------------

        st.subheader("🎯 Career Recommendations")

        recommendations = recommend_careers(
            student_skills
        )

        for item in recommendations:

            career_name = item["career"]
            match = item["match"]

            st.markdown(
                f"""
                <div class="card">
                    <h3>💼 {career_name}</h3>
                    <p style="font-size:18px;">
                        🎯 <b>{match}% match</b>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        # -------------------------------------------------
        # SKILL GAP
        # -------------------------------------------------

        if recommendations:

            selected_career = recommendations[0]["career"]

            st.subheader(
                f"📚 Skill Gap for {selected_career}"
            )

            result = calculate_skill_gap(
                student_skills,
                selected_career
            )

            st.write(
                "**Career Readiness:**",
                f"{result['readiness']}%"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(
                    "### 🟢 Skills You Have"
                )

                for skill in result["matched_skills"]:
                    st.write("🟢", skill)

            with col2:

                st.markdown(
                    "### 🔴 Skills You Need"
                )

                for skill in result["missing_skills"]:
                    st.write("🔴", skill)

            # -------------------------------------------------
            # ROADMAP FROM YOUR CAREER DATA
            # -------------------------------------------------

            career_info = get_career(selected_career)

            if career_info:

                st.subheader(
                    "🗺️ Recommended Learning Roadmap"
                )

                for number, step in enumerate(
                    career_info.get("roadmap", []),
                    1
                ):

                    st.info(
                        f"Step {number}: {step}"
                    )