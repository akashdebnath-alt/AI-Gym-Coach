import streamlit as st

from backend.database import SessionLocal
from backend.auth import (
    register_user,
    login_user,
    update_profile,
)
from backend.graph import chat

from backend.workout_generator import generate_workout

import pandas as pd

from backend.workout_history import save_workout
from backend.progress import add_progress, get_progress
from backend.tools import calculate_bmi


# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="AI Gym Coach", 
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ AI Gym Coach")

# ==========================
# SESSION STATE
# ==========================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

# ==========================
# LOGGED IN
# ==========================

if st.session_state.logged_in:



    st.sidebar.success(f"Welcome, {st.session_state.user.name} 👋")

    st.sidebar.write(f"📧 {st.session_state.user.email}")

    st.sidebar.write(
        f"🎯 Goal: {st.session_state.user.goal or 'Not Set'}"
    )

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "👤 My Profile",
            "🤖 AI Coach",
            "📈 Progress",
            "🏋️ Workout History",
            "🥗 Nutrition Plan",
        ]
    )

    if st.sidebar.button("🚪 Logout"): 
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

    # ==========================
    # DASHBOARD
    # ==========================

    elif page == "🏠 Dashboard":

        st.header("🏠 AI Fitness Dashboard")

        st.success(f"👋 Welcome back, {st.session_state.user.name}!")

        st.write("Here is your current fitness summary.")

        from backend.tools import (
            calculate_bmi,
            calculate_bmr,
            water_intake,
        )

        bmi = calculate_bmi.invoke(
            {
                "weight": st.session_state.user.weight,
                "height": st.session_state.user.height,
            }
        )

        bmr = calculate_bmr.invoke(
            {
                "weight": st.session_state.user.weight,
                "height": st.session_state.user.height,
                "age": st.session_state.user.age,
                "gender": st.session_state.user.gender,
            }
        )

        water = water_intake.invoke(
            {
                "weight": st.session_state.user.weight,
            }
        )

        st.subheader("📋 Your Profile")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🎯 Goal", st.session_state.user.goal or "Not Set")
            st.metric("⚖️ Weight", f"{st.session_state.user.weight} kg")
            st.metric("📏 Height", f"{st.session_state.user.height} cm")

        with col2:
            st.metric("📊 BMI", bmi)
            st.metric("🔥 BMR", f"{bmr} kcal/day")
            st.metric("💧 Water Intake", f"{water} L/day")

        st.divider()

        st.subheader("🏋️ AI Workout Generator")

        if st.button("🏋️ Generate My Workout Plan", use_container_width=True):

            with st.spinner("Creating your personalized workout..."):

                workout = generate_workout(st.session_state.user)

            db = SessionLocal()

            save_workout(
                db=db,
                user_id=st.session_state.user.id,
                workout=workout
            )

            db.close()

            st.success("✅ Workout generated and saved successfully!")

            st.markdown(workout)

    # ==========================
    # PROFILE
    # ==========================

    elif page == "👤 My Profile":

            st.header("👤 My Profile")

            st.write("Update your personal and fitness information below.")

            st.divider()

            st.subheader("📋 Personal Information")
            age = st.number_input(
                "Age",
                min_value=10,
                max_value=100,
                value=st.session_state.user.age or 18,
            )

            st.divider()

            st.subheader("🏋️ Fitness Information")
            gender = st.selectbox(
                "Gender",
                [
                    "Male",
                    "Female",
                    "Other",
                ],
            )

            st.divider()

            st.subheader("🩺 Health Information")
            height = st.number_input(
                "Height (cm)",
                value=st.session_state.user.height or 170.0,
            )

            weight = st.number_input(
                "Weight (kg)",
                value=st.session_state.user.weight or 70.0,
            )

            goal = st.selectbox(
                "Fitness Goal",
                [
                    "Weight Loss",
                    "Muscle Gain",
                    "Maintenance",
                    "Strength",
                    "General Fitness",
                ],
            )

            activity_level = st.selectbox(
                "Activity Level",
                [
                    "Sedentary",
                    "Lightly Active",
                    "Moderately Active",
                    "Very Active",
                ],
            )

            experience_level = st.selectbox(
                "Experience Level",
                [
                    "Beginner",
                    "Intermediate",
                    "Advanced",
                ],
            )

            medical_conditions = st.text_area(
                "Medical Conditions",
                value=st.session_state.user.medical_conditions or "",
            )

            available_equipment = st.selectbox(
                "Available Equipment",
                [
                    "Gym",
                    "Home Gym",
                    "Dumbbells",
                    "Bodyweight",
                ],
            )
    if st.button(
        "💾 Save Profile",
        use_container_width=True
    ):

        db = SessionLocal()

        success, result = update_profile(
            db=db,
            user_id=st.session_state.user.id,
            age=age,
            gender=gender,
            height=height,
            weight=weight,
            goal=goal,
            activity_level=activity_level,
            experience_level=experience_level,
            medical_conditions=medical_conditions,
            available_equipment=available_equipment,
        )

        db.close()

        if success:
            st.session_state.user = result
            st.success("✅ Profile updated successfully!")
        else:
            st.error(result)

# ==========================
# AI COACH
# ==========================

    elif page == "🤖 AI Coach":

        st.header("🤖 AI Fitness Coach")

        st.write(
            """
        Ask me anything about:

        - 🏋️ Workout Plans
        - 🥗 Nutrition
        - 📊 BMI & BMR
        - 💪 Muscle Building
        - ⚖️ Weight Loss
        - 🏃 Exercise Techniques
        """
        )

        st.divider()

        st.subheader("💬 Chat with your AI Coach")
        st.info(
            "💡 Tip: Ask questions like:\n"
            "- Calculate my BMI\n"
            "- Create a 5-day workout plan\n"
            "- Best foods for muscle gain\n"
            "- Improve my diet"
               )
        user_prompt = st.chat_input("Example: Create a chest workout for beginners")

        if user_prompt:

            with st.chat_message("user"):
                st.write(user_prompt)

            try:

                answer = chat(
                    st.session_state.user,
                    user_prompt
                    )

                from backend.chat_history import save_chat

                db = SessionLocal()

                save_chat(
                    db=db,
                    user_id=st.session_state.user.id,
                    question=user_prompt,
                    answer=answer
                    )

                db.close()

                with st.chat_message("assistant"):

                    st.markdown(answer)

            except Exception as e:

                st.error(f"Error: {e}")
# ==========================
# PROGRESS
# ==========================

    elif page == "📈 Progress":

        st.header("📈 Progress Tracker")

        st.write(
            "Track your fitness journey over time."
        )

        st.divider()

        current_weight = st.number_input(
            "Current Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=float(st.session_state.user.weight or 70),
        )

        body_fat = st.number_input(
            "Body Fat % (Optional)",
            min_value=0.0,
            max_value=100.0,
            value=0.0,
        )

        if st.button("💾 Save Progress"):

            bmi = calculate_bmi.invoke(
                {
                    "weight": current_weight,
                    "height": st.session_state.user.height,
                }
            )

            db = SessionLocal()

            add_progress(
                db=db,
                user_id=st.session_state.user.id,
                weight=current_weight,
                bmi=bmi,
                body_fat=body_fat if body_fat > 0 else None,
            )

            db.close()

            st.success("✅ Progress saved successfully!")

        st.divider()

        db = SessionLocal()

        history = get_progress(
            db,
            st.session_state.user.id,
        )

        db.close()

        if history:

            st.subheader("📊 Weight Progress")

            data = pd.DataFrame(
                {
                    "Date": [item.date for item in history],
                    "Weight": [item.weight for item in history],
                    "BMI": [item.bmi for item in history],
                }
            )

            
            st.line_chart(
                data.set_index("Date")["Weight"]
            )

            st.divider()

            st.subheader("📋 Progress History")
            st.dataframe(
                data.sort_values("Date", ascending=False),
                use_container_width=True,
            )

        else:

            st.info("No progress records yet.")
    # ==========================
    # WORKOUT HISTORY
    # ==========================

    elif page == "🏋️ Workout History":

        st.header("🏋️ Workout History")

        st.write(
            "View all your previously generated workout plans."
        )

        st.divider()

        from backend.workout_history import get_workouts

        db = SessionLocal()

        workouts = get_workouts(
            db=db,
            user_id=st.session_state.user.id,
        )

        db.close()

        if not workouts:

            st.info(
                    "📭 No workout history yet.\n\nGenerate your first workout from the Dashboard!"
                    )

        else:

            for workout in workouts:

                with st.expander(
                    workout.created_at.strftime("%d %B %Y %I:%M %p")
                ):

                    st.markdown(workout.workout)

# ==========================
# NUTRITION PLAN
# ==========================

    elif page == "🥗 Nutrition Plan":

        st.header("🥗 AI Nutrition Planner")

        st.write(
            "Generate personalized AI-powered nutrition plans."
        )

        st.divider()

        from backend.diet_generator import generate_diet
        from backend.nutrition_history import (
            save_nutrition,
            get_nutritions,
        )

        if st.button("🥗 Generate Nutrition Plan"):

            with st.spinner("Generating your AI diet plan..."):

                nutrition = generate_diet(
                    st.session_state.user
                )

            db = SessionLocal()

            save_nutrition(
                db=db,
                user_id=st.session_state.user.id,
                nutrition=nutrition,
            )

            db.close()

            st.success("✅ Nutrition plan generated and saved!")

            st.markdown(nutrition)

        st.divider()

        st.subheader("📜 Previous Nutrition Plans")

        db = SessionLocal()

        history = get_nutritions(
            db,
            st.session_state.user.id,
        )

        db.close()

        if history:

            for item in history:

                with st.expander(
                    item.created_at.strftime("%d %B %Y %I:%M %p")
                ):

                    st.markdown(item.nutrition)

        else:

            st.info(
                    "📭 No nutrition plans available.\n\nGenerate your first AI nutrition plan!"
                    )                    

# ==========================
# NOT LOGGED IN
# ==========================

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Login",
        "Register"
    ]
)

# ==========================
# REGISTER
# ==========================

if menu == "Register":

    st.header("Create Account")

    name = st.text_input("Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        db = SessionLocal()

        success, message = register_user(
            db=db,
            name=name,
            email=email,
            password=password
        )

        db.close()

        if success:

            st.success(message)

        else:

            st.error(message)

# ==========================
# LOGIN
# ==========================

elif menu == "Login":

    st.header("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        db = SessionLocal()

        success, result = login_user(
            db=db,
            email=email,
            password=password
        )

        db.close()

        if success:

            st.session_state.logged_in = True
            st.session_state.user = result

            st.success("Login Successful!")

            st.rerun()

        else:

            st.error(result)

            st.markdown("---")

st.caption(
    "🏋️ AI Gym Coach | Developed by Akash Debnath | Powered by Streamlit • LangGraph • Gemini"
)
            