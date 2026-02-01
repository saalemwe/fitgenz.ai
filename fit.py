import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import os

# Page config
st.set_page_config(page_title="Smart Fitness App", layout="wide")
st.title("💪 Smart Workout & Diet App")

# Sidebar profile
st.sidebar.header("Your Profile")
age = st.sidebar.number_input("Age", 10, 100)
weight = st.sidebar.number_input("Weight (kg)", 20, 200)
height = st.sidebar.number_input("Height (cm)", 50, 250)
goal = st.sidebar.selectbox("Fitness Goal", ["Weight Loss", "Muscle Gain", "Flexibility"])
diet = st.sidebar.selectbox("Diet Preference", ["Vegetarian", "Vegan", "Keto", "Balanced"])
style = st.sidebar.radio("Trainer Style", ["Gym Friend", "Trainer"])
st.sidebar.write("Your profile info will personalize workouts and diet plans!")

# Initialize workout_plan
workout_plan = []

# Workout Generator
st.header("🏋️ Your Workout Plan")
if st.button("Generate Workout"):
    if goal == "Weight Loss":
        workout_plan = ["30 min Cardio", "HIIT 20 min", "Core Strength 15 min"]
    elif goal == "Muscle Gain":
        workout_plan = ["Bench Press 4x8", "Squats 4x10", "Deadlift 3x6"]
    else:
        workout_plan = ["Yoga 30 min", "Stretching 15 min", "Pilates 20 min"]

if workout_plan:
    st.subheader(f"Trainer Style: {style}")
    for w in workout_plan:
        st.markdown(f"**{w}**")
else:
    st.info("Click 'Generate Workout' to see your plan!")

# Diet Plan Generator
st.header("🥗 Your Diet Plan")
def generate_diet(diet_pref):
    if diet_pref == "Vegetarian":
        return ["Breakfast: Oats + Fruits", "Lunch: Veggie Salad + Lentils", "Dinner: Paneer Stir Fry"]
    elif diet_pref == "Vegan":
        return ["Breakfast: Smoothie Bowl", "Lunch: Quinoa Salad", "Dinner: Tofu Stir Fry"]
    elif diet_pref == "Keto":
        return ["Breakfast: Eggs & Avocado", "Lunch: Chicken Salad", "Dinner: Salmon + Veggies"]
    else:
        return ["Breakfast: Eggs & Toast", "Lunch: Chicken + Rice + Veggies", "Dinner: Fish + Salad"]

diet_plan = generate_diet(diet)
for meal in diet_plan:
    st.write(meal)

# Weekly Flow
st.header("📊 Weekly Workout Flow")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
workouts_per_day = [workout_plan for _ in days]
df_flow = pd.DataFrame({"Day": days, "Workout": [" / ".join(workout_plan) for workout_plan in workouts_per_day]})
st.table(df_flow)

# Gym Record Tracker
st.header("📝 Track Your Session")
exercise = st.text_input("Exercise Name")
reps = st.number_input("Reps", 0, 100)
weight_lifted = st.number_input("Weight (kg)", 0, 500)
if st.button("Save Session"):
    if exercise.strip() == "":
        st.error("Please enter an exercise name.")
    else:
        record = {"Exercise": exercise, "Reps": reps, "Weight": weight_lifted}
        df = pd.DataFrame([record])
        if os.path.exists("gym_record.csv"):
            df.to_csv("gym_record.csv", mode="a", header=False, index=False)
        else:
            df.to_csv("gym_record.csv", index=False)
        st.success("Session saved!")

# Progress Charts
st.header("📈 Progress Charts")
if os.path.exists("gym_record.csv"):
    df = pd.read_csv("gym_record.csv", names=["Exercise", "Reps", "Weight"])
    chart_data = df.groupby("Exercise")["Weight"].sum()
    st.bar_chart(chart_data)
else:
    st.info("No session data yet. Track your first workout!")

# Trainer / Gym Friend Messages
st.header("💬 Trainer / Gym Friend Advice")
if style == "Gym Friend":
    st.info("Hey! Let's crush today's workout together 😎")
else:
    st.info("Remember proper form and controlled reps. Focus on quality over quantity!")