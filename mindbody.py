import streamlit as st
import pandas as pd
import datetime

# Set page configuration with responsive design
st.set_page_config(
    page_title="Personal Assessment Tests",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for responsive design and better mobile experience
st.markdown("""
<style>
    /* Mobile-first responsive design */
    @media (max-width: 768px) {
        .main .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
            max-width: 100% !important;
        }
        
        .stSelectbox > div > div {
            font-size: 14px;
        }
        
        .stRadio > div {
            flex-direction: column;
        }
        
        .stButton > button {
            width: 100%;
            margin: 0.5rem 0;
        }
        
        .stColumns {
            flex-direction: column !important;
        }
        
        .stColumns > div {
            width: 100% !important;
            margin-bottom: 1rem;
        }
    }
    
    /* Better visual hierarchy */
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .test-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
    
    .improvement-card {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        margin: 0.5rem 0;
    }
    
    .warning-card {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ffc107;
        margin: 0.5rem 0;
    }
    
    /* Progress indicators */
    .progress-container {
        background: #e9ecef;
        border-radius: 10px;
        height: 8px;
        margin: 1rem 0;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }
    
    /* Mobile navigation improvements */
    .stSidebar {
        background-color: #f8f9fa;
    }
    
    .stSidebar .stSelectbox {
        background-color: white;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Main header with responsive design
st.markdown("""
<div class="main-header">
    <h1>🧠 Personal Assessment Tests</h1>
    <p>Discover insights about yourself with our comprehensive assessment suite</p>
</div>
""", unsafe_allow_html=True)

# Enhanced sidebar with better mobile navigation
st.sidebar.title("🔥 Navigation")
st.sidebar.markdown("👇 **Select a test to begin:**")

test_choice = st.sidebar.selectbox(
    "Choose Your Assessment:",
    ["🏠 Home", "🧮 IQ Test", "⚖️ BMI & Nutrition", "😰 Stress Assessment"],
    help="Select any test to start your personal assessment journey"
)

# Progress indicator for current test
if test_choice != "🏠 Home":
    st.sidebar.markdown("---")
    st.sidebar.success(f"📍 Current: {test_choice}")
    
# Show tips in sidebar
st.sidebar.markdown("---")
st.sidebar.info("💡 **Mobile Tip:** Rotate your device to landscape mode for better experience on small screens!")

# Initialize session state for user profile and recommendations
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {
        'name': '',
        'age': 25,
        'completed_tests': [],
        'test_history': {},
        'last_visit': datetime.datetime.now()
    }

# Home page with enhanced cards
if test_choice == "🏠 Home":
    # Welcome section with personalization
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("## Welcome to Your Personal Assessment Hub! 👋")
        
        # User profile section
        with st.expander("👤 Personal Profile (Optional)", expanded=False):
            name = st.text_input("Your Name:", value=st.session_state.user_profile['name'])
            age = st.slider("Your Age:", 13, 100, st.session_state.user_profile['age'])
            
            if st.button("Save Profile"):
                st.session_state.user_profile['name'] = name
                st.session_state.user_profile['age'] = age
                st.success("Profile saved! 🎉")
        
        # Personalized greeting
        if st.session_state.user_profile['name']:
            st.markdown(f"### Hello, {st.session_state.user_profile['name']}! 😊")
        
        # Show completion status
        completed_tests = st.session_state.user_profile.get('completed_tests', [])
        if completed_tests:
            st.markdown("### 📊 Your Progress")
            progress = len(completed_tests) / 3 * 100
            st.progress(progress / 100)
            st.write(f"Completed: {len(completed_tests)}/3 tests ({progress:.0f}%)")
    
    with col2:
        st.markdown("### 🎯 Quick Stats")
        total_tests = 3
        completed = len(st.session_state.user_profile.get('completed_tests', []))
        
        st.metric("Available Tests", total_tests)
        st.metric("Completed Tests", completed)
        st.metric("Progress", f"{completed/total_tests*100:.0f}%")
    
    st.markdown("---")
    
    # Enhanced test cards with responsive layout
    st.markdown("## 📋 Available Assessments")
    
    # For mobile: single column, for desktop: multiple columns
    test_info = [
        {
            "title": "🧮 IQ Test",
            "description": "Evaluate your cognitive abilities with 10 challenging questions",
            "features": ["Logical reasoning", "Pattern recognition", "Problem solving", "Detailed explanations"],
            "time": "⏱️ 10-15 minutes",
            "difficulty": "🔴 Challenging"
        },
        {
            "title": "⚖️ BMI & Nutrition",
            "description": "Calculate your BMI and receive personalized nutrition advice",
            "features": ["BMI calculation", "Health assessment", "Food recommendations", "Lifestyle tips"],
            "time": "⏱️ 5-8 minutes",
            "difficulty": "🟢 Easy"
        },
        {
            "title": "😰 Stress Assessment",
            "description": "Measure your stress levels and get coping strategies",
            "features": ["Stress evaluation", "Risk assessment", "Coping strategies", "Wellness tips"],
            "time": "⏱️ 8-12 minutes",
            "difficulty": "🟡 Moderate"
        }
    ]
    
    # Use columns for desktop, single column for mobile
    cols = st.columns([1, 1, 1])
    
    for i, test in enumerate(test_info):
        with cols[i % 3]:
            with st.container():
                st.markdown(f"""
                <div class="test-card">
                    <h3>{test['title']}</h3>
                    <p>{test['description']}</p>
                    <ul>
                        {''.join([f'<li>✓ {feature}</li>' for feature in test['features']])}
                    </ul>
                    <p><strong>{test['time']}</strong> | <strong>{test['difficulty']}</strong></p>
                </div>
                """, unsafe_allow_html=True)
    
    # Instructions with better mobile formatting
    st.markdown("---")
    st.markdown("### 📱 How to Use This App")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown("""
        **Getting Started:**
        1. 📱 Use the dropdown menu in the sidebar
        2. 🎯 Select any assessment test
        3. 📝 Answer all questions honestly
        4. 📊 Review your personalized results
        """)
    
    with col2:
        st.markdown("""
        **Mobile Tips:**
        - 🔄 Rotate device for better view
        - 👆 Tap anywhere to dismiss dropdowns
        - 📱 All tests are mobile-optimized
        - 💾 Your progress is automatically saved
        """)

# Enhanced IQ Test with personalized recommendations
elif test_choice == "🧮 IQ Test":
    st.markdown("## 🧮 Cognitive Assessment Test")
    
    # Progress indicator
    if 'iq_answers' not in st.session_state:
        st.session_state.iq_answers = {}
    
    progress = len(st.session_state.iq_answers) / 10 * 100
    st.markdown(f"**Progress: {progress:.0f}% Complete**")
    st.progress(progress / 100)
    
    st.markdown("""
    <div class="test-card">
        <p>This cognitive assessment evaluates your logical reasoning, pattern recognition, and problem-solving abilities. 
        Take your time and think through each question carefully.</p>
        <p><strong>⏱️ Estimated time:</strong> 10-15 minutes | <strong>📊 Questions:</strong> 10</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced questions with better mobile formatting
    questions = [
        {
            "question": "What comes next in the sequence: 2, 4, 8, 16, ?",
            "options": ["24", "32", "30", "20"],
            "correct": "32",
            "category": "Pattern Recognition",
            "difficulty": "Easy"
        },
        {
            "question": "If all roses are flowers and some flowers are red, which statement is true?",
            "options": ["All roses are red", "Some roses might be red", "No roses are red", "All flowers are roses"],
            "correct": "Some roses might be red",
            "category": "Logical Reasoning",
            "difficulty": "Medium"
        },
        {
            "question": "Complete the analogy: Book is to Reading as Fork is to ?",
            "options": ["Kitchen", "Eating", "Spoon", "Food"],
            "correct": "Eating",
            "category": "Analogical Reasoning",
            "difficulty": "Easy"
        },
        {
            "question": "What number should replace the question mark: 3, 7, 15, 31, ?",
            "options": ["47", "63", "55", "39"],
            "correct": "63",
            "category": "Mathematical Reasoning",
            "difficulty": "Hard"
        },
        {
            "question": "Which word doesn't belong: Apple, Banana, Carrot, Orange?",
            "options": ["Apple", "Banana", "Carrot", "Orange"],
            "correct": "Carrot",
            "category": "Classification",
            "difficulty": "Easy"
        },
        {
            "question": "If you rearrange the letters 'CIFAIPC', you would have the name of a:",
            "options": ["City", "Animal", "Ocean", "Country"],
            "correct": "Ocean",
            "category": "Spatial Reasoning",
            "difficulty": "Medium"
        },
        {
            "question": "Complete the pattern: △ ○ □ △ ○ ?",
            "options": ["△", "○", "□", "◇"],
            "correct": "□",
            "category": "Pattern Recognition",
            "difficulty": "Easy"
        },
        {
            "question": "What comes next: 1, 4, 9, 16, 25, ?",
            "options": ["30", "36", "35", "49"],
            "correct": "36",
            "category": "Mathematical Reasoning",
            "difficulty": "Medium"
        },
        {
            "question": "If CAT = 24, DOG = 26, what does PIG equal?",
            "options": ["28", "32", "29", "31"],
            "correct": "29",
            "category": "Code Breaking",
            "difficulty": "Hard"
        },
        {
            "question": "Which number is the odd one out: 2, 4, 6, 9, 8?",
            "options": ["2", "4", "6", "9"],
            "correct": "9",
            "category": "Classification",
            "difficulty": "Easy"
        }
    ]
    
    # Display questions with enhanced mobile design
    for i, q in enumerate(questions):
        with st.container():
            st.markdown(f"### Question {i+1}/10")
            st.markdown(f"**Category:** {q['category']} | **Difficulty:** {q['difficulty']}")
            st.markdown(f"**{q['question']}**")
            
            # Use columns for better mobile layout
            answer = st.radio(
                "Select your answer:",
                q["options"],
                key=f"iq_q{i+1}",
                help=f"Category: {q['category']} - {q['difficulty']} level"
            )
            st.session_state.iq_answers[i] = answer
            st.markdown("---")
    
    # Enhanced results with personalized recommendations
    if st.button("📊 Get My IQ Results", help="Calculate your cognitive assessment score"):
        correct_count = 0
        category_scores = {}
        
        for i, q in enumerate(questions):
            category = q['category']
            if category not in category_scores:
                category_scores[category] = {'correct': 0, 'total': 0}
            
            category_scores[category]['total'] += 1
            
            if st.session_state.iq_answers.get(i) == q["correct"]:
                correct_count += 1
                category_scores[category]['correct'] += 1
        
        score_percentage = (correct_count / len(questions)) * 100
        iq_estimate = 85 + (score_percentage * 0.3)
        
        # Save results to user profile
        st.session_state.user_profile['test_history']['iq'] = {
            'score': iq_estimate,
            'percentage': score_percentage,
            'date': datetime.datetime.now(),
            'category_scores': category_scores
        }
        
        if 'IQ Test' not in st.session_state.user_profile['completed_tests']:
            st.session_state.user_profile['completed_tests'].append('IQ Test')
        
        # Results display with better formatting
        st.markdown("""
        <div class="result-card">
            <h2>🎉 Your Cognitive Assessment Results</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Correct Answers", f"{correct_count}/10")
        with col2:
            st.metric("Score Percentage", f"{score_percentage:.1f}%")
        with col3:
            st.metric("Estimated IQ", f"{iq_estimate:.0f}")
        
        # Category breakdown
        st.markdown("### 📊 Performance by Category")
        for category, scores in category_scores.items():
            percentage = (scores['correct'] / scores['total']) * 100
            st.write(f"**{category}:** {scores['correct']}/{scores['total']} ({percentage:.0f}%)")
            st.progress(percentage / 100)
        
        # Personalized recommendations based on performance
        st.markdown("### 🎯 Personalized Improvement Recommendations")
        
        weak_areas = [cat for cat, scores in category_scores.items() 
                     if (scores['correct'] / scores['total']) < 0.6]
        strong_areas = [cat for cat, scores in category_scores.items() 
                       if (scores['correct'] / scores['total']) >= 0.8]
        
        if weak_areas:
            st.markdown("""
            <div class="warning-card">
                <h4>🎯 Areas for Improvement</h4>
            </div>
            """, unsafe_allow_html=True)
            
            for area in weak_areas:
                if area == "Pattern Recognition":
                    st.markdown("""
                    <div class="improvement-card">
                        <strong>🔍 Pattern Recognition:</strong>
                        <ul>
                            <li>Practice number sequences daily (5-10 minutes)</li>
                            <li>Try visual pattern puzzles and brain teasers</li>
                            <li>Use apps like Lumosity or Peak for pattern games</li>
                            <li>Study geometric sequences and arithmetic progressions</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                elif area == "Logical Reasoning":
                    st.markdown("""
                    <div class="improvement-card">
                        <strong>🧠 Logical Reasoning:</strong>
                        <ul>
                            <li>Practice syllogistic reasoning exercises</li>
                            <li>Read logic puzzles and solve them step-by-step</li>
                            <li>Study basic principles of formal logic</li>
                            <li>Try Boolean logic and conditional reasoning problems</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
                elif area == "Mathematical Reasoning":
                    st.markdown("""
                    <div class="improvement-card">
                        <strong>🔢 Mathematical Reasoning:</strong>
                        <ul>
                            <li>Practice mental math calculations daily</li>
                            <li>Study number theory and mathematical relationships</li>
                            <li>Use Khan Academy for math skill building</li>
                            <li>Try mathematical olympiad problems</li>
                        </ul>
                    </div>
                    """, unsafe_allow_html=True)
        
        if strong_areas:
            st.markdown("""
            <div class="improvement-card">
                <h4>🌟 Your Strengths</h4>
                <p>Great job in these areas! Consider:</p>
                <ul>
            """, unsafe_allow_html=True)
            for area in strong_areas:
                st.markdown(f"<li>Leverage your {area} skills in academic/professional settings</li>", unsafe_allow_html=True)
            st.markdown("</ul></div>", unsafe_allow_html=True)
        
        # General recommendations based on overall score
        st.markdown("### 💡 General Development Plan")
        
        if iq_estimate >= 130:
            recommendations = [
                "🎓 Consider advanced academic challenges or gifted programs",
                "🧩 Try complex puzzles like chess, Go, or advanced mathematics",
                "📚 Explore specialized topics in your areas of interest",
                "🤝 Mentor others to reinforce your own understanding"
            ]
        elif iq_estimate >= 110:
            recommendations = [
                "📖 Read regularly to expand vocabulary and general knowledge",
                "🧩 Solve daily brain teasers and puzzles",
                "🎯 Focus on weak areas while maintaining strengths",
                "💻 Try online cognitive training programs"
            ]
        else:
            recommendations = [
                "🎯 Focus on one cognitive skill at a time",
                "⏰ Practice consistently for 15-20 minutes daily",
                "📱 Use brain training apps with progressive difficulty",
                "🤝 Consider working with a tutor for personalized guidance"
            ]
        
        for rec in recommendations:
            st.markdown(f"- {rec}")

# Enhanced BMI Test with comprehensive nutrition recommendations
elif test_choice == "⚖️ BMI & Nutrition":
    st.markdown("## ⚖️ BMI Calculator & Personalized Nutrition Plan")
    
    st.markdown("""
    <div class="test-card">
        <p>Calculate your Body Mass Index and receive personalized nutrition recommendations based on your health goals and current status.</p>
        <p><strong>⏱️ Time needed:</strong> 5-8 minutes | <strong>📊 Includes:</strong> BMI calculation, health assessment, and meal planning</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced input section with better mobile layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📏 Your Measurements")
        height = st.number_input(
            "Height (cm):", 
            min_value=100, 
            max_value=250, 
            value=170,
            help="Enter your height in centimeters"
        )
        weight = st.number_input(
            "Weight (kg):", 
            min_value=30, 
            max_value=200, 
            value=70,
            help="Enter your current weight in kilograms"
        )
        
        # Additional factors for personalized recommendations
        st.markdown("### 🎯 Personal Information")
        age = st.slider("Age:", 13, 100, st.session_state.user_profile.get('age', 25))
        activity_level = st.selectbox(
            "Activity Level:",
            ["Sedentary (little/no exercise)", 
             "Lightly active (light exercise 1-3 days/week)",
             "Moderately active (moderate exercise 3-5 days/week)",
             "Very active (hard exercise 6-7 days/week)",
             "Extra active (very hard exercise/physical job)"]
        )
        
        health_goal = st.selectbox(
            "Primary Health Goal:",
            ["Maintain current weight",
             "Lose weight gradually",
             "Lose weight quickly",
             "Gain weight",
             "Build muscle",
             "Improve overall health"]
        )
        
        dietary_restrictions = st.multiselect(
            "Dietary Restrictions/Preferences:",
            ["None", "Vegetarian", "Vegan", "Gluten-free", "Dairy-free", 
             "Low-carb", "Keto", "Mediterranean", "Diabetic-friendly"]
        )
    
    with col2:
        if st.button("🔍 Calculate My BMI & Get Recommendations", help="Get comprehensive health and nutrition analysis"):
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            
            # Enhanced BMI categories
            if bmi < 16:
                category = "Severely Underweight"
                color = "red"
                health_status = "⚠️ Serious health risk - Please consult a healthcare provider"
                priority = "urgent"
            elif bmi < 17:
                category = "Moderately Underweight"
                color = "orange"
                health_status = "⚠️ Health risk - Consider medical consultation"
                priority = "high"
            elif bmi < 18.5:
                category = "Mildly Underweight"
                color = "yellow"
                health_status = "⚡ Slightly below normal - Monitor closely"
                priority = "moderate"
            elif bmi < 25:
                category = "Normal Weight"
                color = "green"
                health_status = "✅ Healthy range - Great job!"
                priority = "maintain"
            elif bmi < 30:
                category = "Overweight"
                color = "orange"
                health_status = "⚠️ Increased health risk - Consider lifestyle changes"
                priority = "moderate"
            elif bmi < 35:
                category = "Class I Obesity"
                color = "red"
                health_status = "⚠️ High health risk - Recommend medical consultation"
                priority = "high"
            elif bmi < 40:
                category = "Class II Obesity"
                color = "red"
                health_status = "🚨 Very high health risk - Medical supervision recommended"
                priority = "urgent"
            else:
                category = "Class III Obesity"
                color = "red"
                health_status = "🚨 Extremely high health risk - Immediate medical attention advised"
                priority = "urgent"
            
            # Save results
            st.session_state.user_profile['test_history']['bmi'] = {
                'bmi': bmi,
                'category': category,
                'health_goal': health_goal,
                'activity_level': activity_level,
                'date': datetime.datetime.now()
            }
            
            if 'BMI Test' not in st.session_state.user_profile['completed_tests']:
                st.session_state.user_profile['completed_tests'].append('BMI Test')
            
            # Results display
            st.markdown("""
            <div class="result-card">
                <h2>📊 Your Health Assessment Results</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Metrics display
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("BMI Score", f"{bmi:.1f}")
            with col_b:
                st.metric("Category", category)
            with col_c:
                if bmi < 18.5:
                    ideal_weight = 18.5 * (height_m ** 2)
                    weight_diff = ideal_weight - weight
                    st.metric("Weight Goal", f"+{weight_diff:.1f} kg")
                elif bmi > 25:
                    ideal_weight = 22.5 * (height_m ** 2)  # Middle of normal range
                    weight_diff = weight - ideal_weight
                    st.metric("Weight Goal", f"-{weight_diff:.1f} kg")
                else:
                    st.metric("Status", "Ideal ✅")
            
            st.markdown(f"**Health Status:** {health_status}")
            
            # Personalized nutrition recommendations
            st.markdown("### 🍽️ Personalized Nutrition Plan")
            
            # Calculate daily calorie needs
            if age <= 30:
                bmr_factor = 1.0
            elif age <= 50:
                bmr_factor = 0.95
            else:
                bmr_factor = 0.9
            
            activity_multipliers = {
                "Sedentary (little/no exercise)": 1.2,
                "Lightly active (light exercise 1-3 days/week)": 1.375,
                "Moderately active (moderate exercise 3-5 days/week)": 1.55,
                "Very active (hard exercise 6-7 days/week)": 1.725,
                "Extra active (very hard exercise/physical job)": 1.9
            }
            
            # Simplified BMR calculation
            bmr = (10 * weight + 6.25 * height - 5 * age + 5) * bmr_factor
            daily_calories = bmr * activity_multipliers[activity_level]
            
            # Adjust calories based on goal
            goal_adjustments = {
                "Maintain current weight": 0,
                "Lose weight gradually": -500,
                "Lose weight quickly": -750,
                "Gain weight": +500,
                "Build muscle": +300,
                "Improve overall health": 0
            }
            
            target_calories = daily_calories + goal_adjustments[health_goal]
            
            st.markdown(f"""
            <div class="improvement-card">
                <h4>🎯 Your Daily Nutrition Targets</h4>
                <ul>
                    <li><strong>Calories:</strong> {target_calories:.0f} kcal/day</li>
                    <li><strong>Protein:</strong> {target_calories * 0.25 / 4:.0f}g (25%)</li>
                    <li><strong>Carbs:</strong> {target_calories * 0.45 / 4:.0f}g (45%)</li>
                    <li><strong>Fats:</strong> {target_calories * 0.30 / 9:.0f}g (30%)</li>
                    <li><strong>Water:</strong> {weight * 35 / 1000:.1f} liters/day</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
            
            # Personalized food recommendations
            st.markdown("### 🥗 Recommended Foods")
            
            if bmi < 18.5:  # Underweight
                foods_to_include = [
                    "🥑 **Healthy Fats:** Avocados, nuts, olive oil, fatty fish",
                    "🥜 **Protein-rich:** Nuts, nut butters, lean meats, eggs",
                    "🍌 **Calorie-dense fruits:** Bananas, dried fruits, smoothies",
                    "🍚 **Complex carbs:** Brown rice, quinoa, oats, whole grain bread",
                    "🥛 **Dairy:** Whole milk, yogurt, cheese (if not restricted)"
                ]
                
                meal_suggestions = {
                    "Breakfast": "Oatmeal with nuts, banana, and honey + glass of whole milk",
                    "Lunch": "Quinoa bowl with avocado, chicken, and olive oil dressing",
                    "Dinner": "Salmon with sweet potato and steamed vegetables",
                    "Snacks": "Trail mix, nut butter with apple, protein smoothie"
                }
                
            elif bmi > 25:  # Overweight/Obese
                foods_to_include = [
                    "🥬 **Leafy greens:** Spinach, kale, arugula, lettuce",
                    "🥒 **Low-cal vegetables:** Cucumber, celery, broccoli, cauliflower",
                    "🐟 **Lean proteins:** White fish, chicken breast, tofu, legumes",
                    "🍓 **Low-sugar fruits:** Berries, apples, citrus fruits",
                    "🫘 **Fiber-rich:** Beans, lentils, chia seeds, vegetables"
                ]
                
                meal_suggestions = {
                    "Breakfast": "Greek yogurt with berries and chia seeds",
                    "Lunch": "Large salad with grilled chicken and light vinaigrette",
                    "Dinner": "Steamed fish with roasted vegetables and quinoa",
                    "Snacks": "Carrot sticks with hummus, herbal tea, apple slices"
                }
                
            else:  # Normal weight
                foods_to_include = [
                    "🌈 **Variety:** Mix of all food groups in moderation",
                    "🐟 **Quality proteins:** Fish, poultry, beans, eggs",
                    "🍎 **Fresh fruits:** Seasonal fruits, berries, citrus",
                    "🥦 **Vegetables:** Colorful variety, aim for 5-7 servings daily",
                    "🌾 **Whole grains:** Brown rice, quinoa, oats, whole wheat"
                ]
                
                meal_suggestions = {
                    "Breakfast": "Whole grain toast with avocado and poached egg",
                    "Lunch": "Balanced bowl with protein, grains, and vegetables",
                    "Dinner": "Grilled protein with roasted vegetables and brown rice",
                    "Snacks": "Mixed nuts, fruit, yogurt with granola"
                }
            
            # Display food recommendations
            for food in foods_to_include:
                st.markdown(f"- {food}")
            
            # Meal plan suggestions
            st.markdown("### 🍽️ Daily Meal Plan Suggestions")
            
            meal_cols = st.columns(4)
            meals = ["Breakfast", "Lunch", "Dinner", "Snacks"]
            
            for i, meal in enumerate(meals):
                with meal_cols[i]:
                    st.markdown(f"**{meal}:**")
                    st.write(meal_suggestions[meal])
            
            # Dietary restriction adaptations
            if dietary_restrictions and "None" not in dietary_restrictions:
                st.markdown("### 🌱 Adapted for Your Dietary Preferences")
                
                adaptations = []
                if "Vegetarian" in dietary_restrictions:
                    adaptations.append("🌱 Replace meat with legumes, tofu, tempeh, or plant-based proteins")
                if "Vegan" in dietary_restrictions:
                    adaptations.append("🌿 Use plant-based alternatives for all animal products")
                if "Gluten-free" in dietary_restrictions:
                    adaptations.append("🌾 Choose rice, quinoa, and certified gluten-free grains")
                if "Dairy-free" in dietary_restrictions:
                    adaptations.append("🥥 Use plant-based milk alternatives (almond, oat, coconut)")
                if "Low-carb" in dietary_restrictions:
                    adaptations.append("🥩 Focus on proteins and healthy fats, limit grains and fruits")
                
                for adaptation in adaptations:
                    st.markdown(f"- {adaptation}")
            
            # Lifestyle recommendations based on priority
            st.markdown("### 💪 Lifestyle Recommendations")
            
            if priority == "urgent":
                st.markdown("""
                <div class="warning-card">
                    <h4>⚠️ Immediate Action Required</h4>
                    <ul>
                        <li>Schedule appointment with healthcare provider within 1 week</li>
                        <li>Consider working with registered dietitian</li>
                        <li>Monitor health metrics daily (weight, blood pressure if applicable)</li>
                        <li>Start with gentle lifestyle changes under medical supervision</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            elif priority == "high":
                st.markdown("""
                <div class="improvement-card">
                    <h4>🎯 High Priority Actions</h4>
                    <ul>
                        <li>Consult healthcare provider within 2-3 weeks</li>
                        <li>Begin structured meal planning and portion control</li>
                        <li>Start with 150 minutes moderate exercise per week</li>
                        <li>Track food intake and physical activity</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            elif priority == "moderate":
                st.markdown("""
                <div class="improvement-card">
                    <h4>📈 Moderate Priority Actions</h4>
                    <ul>
                        <li>Gradually adjust eating habits over 4-6 weeks</li>
                        <li>Increase physical activity by 10-15 minutes daily</li>
                        <li>Focus on sustainable lifestyle changes</li>
                        <li>Monitor progress weekly</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            else:  # maintain
                st.markdown("""
                <div class="improvement-card">
                    <h4>✅ Maintenance Strategies</h4>
                    <ul>
                        <li>Continue current healthy habits</li>
                        <li>Vary your exercise routine to prevent boredom</li>
                        <li>Focus on nutrient density and food quality</li>
                        <li>Regular health check-ups (annual)</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            # Exercise recommendations
            st.markdown("### 🏃‍♀️ Exercise Recommendations")
            
            if bmi < 18.5:
                exercises = [
                    "🏋️ **Strength training:** 3x/week to build muscle mass",
                    "🚶 **Walking:** 30 minutes daily at moderate pace",
                    "🧘 **Yoga:** For flexibility and stress management",
                    "🏊 **Swimming:** Low-impact full-body exercise"
                ]
            elif bmi > 30:
                exercises = [
                    "🚶 **Walking:** Start with 10-15 minutes, gradually increase",
                    "🏊 **Water exercises:** Low-impact on joints",
                    "🪑 **Chair exercises:** If mobility is limited",
                    "🧘 **Gentle yoga:** For flexibility and stress relief"
                ]
            else:
                exercises = [
                    "🏃 **Cardio:** 150 minutes moderate or 75 minutes vigorous weekly",
                    "🏋️ **Strength training:** 2-3 times per week, all major muscle groups",
                    "🤸 **Flexibility:** Daily stretching or yoga",
                    "⚖️ **Balance:** Activities like tai chi or balance exercises"
                ]
            
            for exercise in exercises:
                st.markdown(f"- {exercise}")

# Enhanced Stress Test with comprehensive mental health recommendations
elif test_choice == "😰 Stress Assessment":
    st.markdown("## 😰 Comprehensive Stress Assessment")
    
    st.markdown("""
    <div class="test-card">
        <p>This assessment evaluates your current stress levels across multiple dimensions and provides personalized stress management strategies.</p>
        <p><strong>⏱️ Time needed:</strong> 8-12 minutes | <strong>📊 Questions:</strong> 15 comprehensive questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress indicator
    if 'stress_answers' not in st.session_state:
        st.session_state.stress_answers = {}
    
    progress = len(st.session_state.stress_answers) / 15 * 100
    st.markdown(f"**Progress: {progress:.0f}% Complete**")
    st.progress(progress / 100)
    
    # Enhanced stress questions with categories
    stress_questions = [
        {
            "question": "I feel overwhelmed by my daily responsibilities",
            "category": "Work/Life Balance",
            "impact": "high"
        },
        {
            "question": "I have trouble falling asleep or staying asleep due to worry",
            "category": "Sleep Quality",
            "impact": "high"
        },
        {
            "question": "I feel irritable or angry more often than usual",
            "category": "Emotional Regulation",
            "impact": "medium"
        },
        {
            "question": "I have difficulty concentrating on tasks",
            "category": "Cognitive Function",
            "impact": "medium"
        },
        {
            "question": "I experience physical symptoms like headaches or muscle tension",
            "category": "Physical Symptoms",
            "impact": "high"
        },
        {
            "question": "I worry excessively about future events",
            "category": "Anxiety",
            "impact": "high"
        },
        {
            "question": "I have little time for activities I enjoy",
            "category": "Work/Life Balance",
            "impact": "medium"
        },
        {
            "question": "I feel like I can't cope with current problems",
            "category": "Coping Skills",
            "impact": "high"
        },
        {
            "question": "My appetite has changed significantly (eating more or less)",
            "category": "Physical Symptoms",
            "impact": "medium"
        },
        {
            "question": "I avoid social situations because they feel stressful",
            "category": "Social Functioning",
            "impact": "medium"
        },
        {
            "question": "I feel exhausted even after a full night's sleep",
            "category": "Energy Levels",
            "impact": "high"
        },
        {
            "question": "I have trouble making decisions, even small ones",
            "category": "Cognitive Function",
            "impact": "medium"
        },
        {
            "question": "I feel like my stress is affecting my relationships",
            "category": "Social Functioning",
            "impact": "high"
        },
        {
            "question": "I use substances (alcohol, caffeine, etc.) to manage stress",
            "category": "Coping Skills",
            "impact": "high"
        },
        {
            "question": "I feel hopeless about my situation improving",
            "category": "Mental Health",
            "impact": "high"
        }
    ]
    
    stress_options = [
        "Never (0)",
        "Rarely (1)", 
        "Sometimes (2)",
        "Often (3)",
        "Very Often (4)"
    ]
    
    # Display questions with categories
    for i, q in enumerate(stress_questions):
        with st.container():
            st.markdown(f"### Question {i+1}/15")
            st.markdown(f"**Category:** {q['category']} | **Impact Level:** {q['impact'].title()}")
            st.markdown(f"**{q['question']}**")
            
            answer = st.selectbox(
                "How often do you experience this?",
                stress_options,
                key=f"stress_q{i+1}",
                help=f"Consider the past 2 weeks when answering"
            )
            st.session_state.stress_answers[i] = int(answer.split('(')[1].split(')')[0])
            st.markdown("---")
    
    if st.button("📊 Get My Stress Assessment Results", help="Analyze your stress levels and get personalized recommendations"):
        total_stress = sum(st.session_state.stress_answers.values())
        max_stress = len(stress_questions) * 4
        stress_percentage = (total_stress / max_stress) * 100
        
        # Calculate category-specific scores
        category_scores = {}
        for i, q in enumerate(stress_questions):
            category = q['category']
            if category not in category_scores:
                category_scores[category] = {'total': 0, 'count': 0, 'questions': []}
            
            category_scores[category]['total'] += st.session_state.stress_answers.get(i, 0)
            category_scores[category]['count'] += 1
            category_scores[category]['questions'].append(q['question'])
        
        # Save results
        st.session_state.user_profile['test_history']['stress'] = {
            'total_score': total_stress,
            'percentage': stress_percentage,
            'category_scores': category_scores,
            'date': datetime.datetime.now()
        }
        
        if 'Stress Test' not in st.session_state.user_profile['completed_tests']:
            st.session_state.user_profile['completed_tests'].append('Stress Test')
        
        # Results display
        st.markdown("""
        <div class="result-card">
            <h2>📊 Your Stress Assessment Results</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Overall results
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Score", f"{total_stress}/{max_stress}")
        with col2:
            st.metric("Stress Percentage", f"{stress_percentage:.1f}%")
        with col3:
            if stress_percentage >= 75:
                level = "Very High 🔴"
                risk = "High Risk"
            elif stress_percentage >= 50:
                level = "High 🟠"
                risk = "Moderate Risk"
            elif stress_percentage >= 25:
                level = "Moderate 🟡"
                risk = "Low Risk"
            else:
                level = "Low 🟢"
                risk = "Minimal Risk"
            
            st.metric("Stress Level", level)
        
        # Category breakdown
        st.markdown("### 📊 Stress Breakdown by Category")
        
        high_stress_categories = []
        for category, scores in category_scores.items():
            avg_score = scores['total'] / scores['count']
            percentage = (avg_score / 4) * 100
            
            st.write(f"**{category}:** {avg_score:.1f}/4.0 ({percentage:.0f}%)")
            st.progress(percentage / 100)
            
            if percentage >= 60:
                high_stress_categories.append(category)
        
        # Personalized recommendations based on results
        st.markdown("### 🎯 Personalized Stress Management Plan")
        
        if stress_percentage >= 75:
            st.markdown("""
            <div class="warning-card">
                <h4>⚠️ High Stress Alert - Immediate Action Recommended</h4>
                <p>Your stress levels are significantly elevated. Consider consulting with a mental health professional.</p>
            </div>
            """, unsafe_allow_html=True)
            
            immediate_actions = [
                "🏥 **Seek Professional Help:** Contact a counselor or therapist within 1-2 weeks",
                "🆘 **Crisis Resources:** Know emergency contacts (988 Suicide & Crisis Lifeline)",
                "👥 **Support System:** Reach out to trusted friends, family, or support groups",
                "💊 **Medical Consultation:** Discuss with your doctor about stress-related symptoms"
            ]
            
            for action in immediate_actions:
                st.markdown(f"- {action}")
        
        # Category-specific recommendations
        st.markdown("### 🎯 Targeted Interventions")
        
        for category in high_stress_categories:
            if category == "Work/Life Balance":
                st.markdown("""
                <div class="improvement-card">
                    <h4>⚖️ Work/Life Balance Strategies</h4>
                    <ul>
                        <li><strong>Time Management:</strong> Use techniques like Pomodoro or time-blocking</li>
                        <li><strong>Boundaries:</strong> Set clear work hours and stick to them</li>
                        <li><strong>Delegation:</strong> Identify tasks you can delegate or eliminate</li>
                        <li><strong>Prioritization:</strong> Use Eisenhower Matrix (urgent vs important)</li>
                        <li><strong>Break Time:</strong> Schedule regular breaks throughout your day</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            elif category == "Sleep Quality":
                st.markdown("""
                <div class="improvement-card">
                    <h4>😴 Sleep Improvement Plan</h4>
                    <ul>
                        <li><strong>Sleep Hygiene:</strong> Consistent bedtime, cool dark room, no screens 1hr before bed</li>
                        <li><strong>Relaxation Techniques:</strong> Progressive muscle relaxation, 4-7-8 breathing</li>
                        <li><strong>Sleep Schedule:</strong> Same bedtime/wake time daily, even weekends</li>
                        <li><strong>Evening Routine:</strong> Calming activities like reading, gentle stretching</li>
                        <li><strong>Limit Stimulants:</strong> No caffeine after 2 PM, minimal alcohol</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            elif category == "Anxiety":
                st.markdown("""
                <div class="improvement-card">
                    <h4>🧘 Anxiety Management Techniques</h4>
                    <ul>
                        <li><strong>Mindfulness:</strong> Daily meditation, even 5-10 minutes helps</li>
                        <li><strong>Grounding Techniques:</strong> 5-4-3-2-1 sensory method during anxiety</li>
                        <li><strong>Thought Challenging:</strong> Question catastrophic thinking patterns</li>
                        <li><strong>Breathing Exercises:</strong> Box breathing, diaphragmatic breathing</li>
                        <li><strong>Gradual Exposure:</strong> Slowly face feared situations in small steps</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            elif category == "Physical Symptoms":
                st.markdown("""
                <div class="improvement-card">
                    <h4>💪 Physical Stress Relief</h4>
                    <ul>
                        <li><strong>Regular Exercise:</strong> 30 minutes daily, even walking helps</li>
                        <li><strong>Muscle Relaxation:</strong> Progressive muscle relaxation, yoga, stretching</li>
                        <li><strong>Heat Therapy:</strong> Warm baths, heating pads for tension</li>
                        <li><strong>Massage:</strong> Self-massage or professional therapy</li>
                        <li><strong>Hydration:</strong> Adequate water intake, limit excessive caffeine</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            elif category == "Coping Skills":
                st.markdown("""
                <div class="improvement-card">
                    <h4>🛠️ Healthy Coping Strategies</h4>
                    <ul>
                        <li><strong>Problem-Solving:</strong> Break problems into smaller, manageable steps</li>
                        <li><strong>Social Support:</strong> Regular contact with supportive friends/family</li>
                        <li><strong>Creative Outlets:</strong> Art, music, writing, gardening</li>
                        <li><strong>Nature Connection:</strong> Spend time outdoors regularly</li>
                        <li><strong>Spiritual Practices:</strong> Prayer, meditation, or other meaningful practices</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        
        # General stress management techniques
        st.markdown("### 🌟 Daily Stress Management Toolkit")
        
        techniques = [
            "🧘 **Morning Meditation:** Start with 5 minutes daily, gradually increase",
            "📝 **Journaling:** Write down thoughts and feelings for 10 minutes",
            "🚶 **Nature Walks:** 20-30 minutes in natural settings",
            "🎵 **Music Therapy:** Listen to calming music or sounds",
            "📱 **Digital Detox:** Set specific times for social media/news",
            "🤝 **Social Connection:** Schedule regular contact with loved ones",
            "🍃 **Deep Breathing:** Practice throughout the day, especially during stress",
            "📚 **Learning:** Engage in activities that stimulate positive growth"
        ]
        
        for technique in techniques:
            st.markdown(f"- {technique}")
        
        # Emergency resources
        if stress_percentage >= 60:
            st.markdown("### 🆘 Emergency Resources")
            st.markdown("""
            <div class="warning-card">
                <h4>If you're in crisis or having thoughts of self-harm:</h4>
                <ul>
                    <li><strong>988 Suicide & Crisis Lifeline:</strong> Call or text 988 (US)</li>
                    <li><strong>Crisis Text Line:</strong> Text HOME to 741741</li>
                    <li><strong>Emergency Services:</strong> Call 911 if in immediate danger</li>
                    <li><strong>SAMHSA Helpline:</strong> 1-800-662-4357 (24/7 treatment referral)</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

# Enhanced Footer with user progress
st.markdown("---")

# Show overall progress if user has completed tests
completed_tests = st.session_state.user_profile.get('completed_tests', [])
if completed_tests:
    st.markdown("### 🎉 Your Assessment Journey")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        progress_percentage = len(completed_tests) / 3 * 100
        st.progress(progress_percentage / 100)
        st.write(f"**Progress:** {len(completed_tests)}/3 tests completed ({progress_percentage:.0f}%)")
        
        for test in completed_tests:
            if test in st.session_state.user_profile.get('test_history', {}):
                test_data = st.session_state.user_profile['test_history'][test.lower().split()[0]]
                date = test_data['date'].strftime("%Y-%m-%d")
                st.write(f"✅ {test} - Completed on {date}")
    
    with col2:
        if len(completed_tests) == 3:
            st.success("🏆 All tests completed!")
            st.balloons()
        else:
            remaining = 3 - len(completed_tests)
            st.info(f"🎯 {remaining} test{'s' if remaining > 1 else ''} remaining")

# Sidebar footer with tips
st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 App Features")
st.sidebar.markdown("""
- 📱 **Mobile Optimized:** Works great on all devices
- 💾 **Auto-Save:** Your progress is automatically saved
- 🎯 **Personalized:** Get recommendations based on your results
- 🔒 **Private:** All data stays in your browser session
""")

st.sidebar.markdown("### 🆘 Need Help?")
st.sidebar.markdown("""
- 🔄 Refresh page if you encounter issues
- 📱 Try landscape mode on mobile
- 🖥️ Desktop recommended for best experience
""")

# Final note
st.markdown("""
---
<div style='text-align: center; color: #666; font-size: 0.9em;'>
    <p>💡 <strong>Disclaimer:</strong> These assessments are for educational purposes only and do not replace professional medical or psychological advice.</p>
    <p>Made with ❤️ using Streamlit | Responsive Design | Personalized Recommendations</p>
</div>
""", unsafe_allow_html=True)