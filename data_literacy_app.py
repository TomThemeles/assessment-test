#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Expanded questionnaire
questions = [
    {
        "question": "Does your business collect data systematically?",
        "options": ["No", "Somewhat", "Yes"],
        "scores": [1, 3, 5],
        "category": "Data Collection"
    },
    {
        "question": "How do you analyze business data?",
        "options": ["Not at all", "Basic Excel", "Advanced BI Tools"],
        "scores": [1, 3, 5],
        "category": "Data Analysis"
    },
    {
        "question": "Do you use data visualization tools?",
        "options": ["No", "Occasionally", "Regularly"],
        "scores": [1, 3, 5],
        "category": "Visualization"
    },
    {
        "question": "Do you make data-driven decisions?",
        "options": ["Rarely", "Sometimes", "Always"],
        "scores": [1, 3, 5],
        "category": "Decision Making"
    },
    {
        "question": "Does your business use predictive analytics or AI?",
        "options": ["No", "Experimenting", "Integrated AI"],
        "scores": [1, 3, 5],
        "category": "AI & Predictive Analytics"
    },
    {
        "question": "Is data security and compliance a priority?",
        "options": ["Not considered", "Basic controls", "Fully compliant"],
        "scores": [1, 3, 5],
        "category": "Data Security"
    }
]

# Function to calculate data literacy level
def determine_level(score):
    if score <= 6:
        return "Level 1: Data Aware - Start learning about data basics."
    elif score <= 12:
        return "Level 2: Data Proficient - Improve data collection & analysis."
    elif score <= 18:
        return "Level 3: Data Savvy - Use visualization and BI tools."
    elif score <= 24:
        return "Level 4: Data-Driven - Implement predictive analytics."
    else:
        return "Level 5: Data-Centric - AI-driven decision-making."

# Streamlit UI
st.title("📊 Business Data Literacy Assessment")

# Store user responses
responses = {}

st.write("Answer the following questions to assess your business's data literacy level:")

for i, q in enumerate(questions):
    responses[q["question"]] = st.radio(q["question"], q["options"], index=0)

# Button to calculate score
if st.button("Calculate Data Literacy Level"):
    total_score = sum(q["scores"][q["options"].index(responses[q["question"]])] for q in questions)
    level = determine_level(total_score)

    st.subheader(f"🔍 Your Data Literacy Level: {level}")
    st.write(f"**Total Score: {total_score}**")

    # Categorized scores
    category_scores = {}
    for q in questions:
        category = q["category"]
        score = q["scores"][q["options"].index(responses[q["question"]])]
        category_scores[category] = category_scores.get(category, 0) + score

    # Convert to DataFrame for plotting
    df = pd.DataFrame(list(category_scores.items()), columns=["Category", "Score"])

    # Create Bar Chart
    st.subheader("📈 Data Literacy Score Breakdown")
    fig = px.bar(df, x="Category", y="Score", color="Category", text="Score")
    st.plotly_chart(fig)

    # Save results
    result = {"total_score": total_score, "level": level, "category_scores": category_scores}
    st.session_state["result"] = result

    st.success("✅ Results saved! Refresh the page to take the assessment again.")

