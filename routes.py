from pathlib import Path
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent

@router.get("/")
async def home():
    return FileResponse(
        BASE_DIR / "templates" / "index.html"
    )
@router.post("/generate-workout")
async def generate_workout():
    return {
        "workout_plan": [
            {
                "day": "Monday",
                "title": "Full Body Strength",
                "description": "Start your week with a full body workout. Begin with 10 minutes of light warm-up exercises, followed by squats, push-ups, lunges, planks and bodyweight exercises. Perform each exercise for 3 sets with suitable rest between sets. Finish the session with stretching and deep breathing to relax your muscles."
            },
            {
                "day": "Tuesday",
                "title": "Cardio & Endurance",
                "description": "Focus on improving your cardiovascular endurance today. Start with a short warm-up and continue with brisk walking, jogging, jumping jacks and other light cardio exercises. Maintain a comfortable pace and take short breaks whenever required. Complete the workout with cool-down exercises and stretching."
            },
            {
                "day": "Wednesday",
                "title": "Active Recovery",
                "description": "Today is focused on recovery and relaxation. Take a light walk and perform simple stretching exercises to reduce muscle stiffness. Avoid heavy workouts and give your body enough time to recover. Drink sufficient water and maintain a balanced diet throughout the day."
            },
            {
                "day": "Thursday",
                "title": "Upper Body Workout",
                "description": "Work on your upper body strength with exercises such as push-ups, shoulder presses, arm raises and triceps exercises. Perform each exercise with proper form and controlled movements. Take enough rest between sets and finish the workout with upper body stretching."
            },
            {
                "day": "Friday",
                "title": "Lower Body Workout",
                "description": "Focus on strengthening your lower body today. Include squats, lunges, calf raises, glute bridges and other leg exercises. Perform 3 sets of each exercise according to your fitness level. Finish with light stretching to improve flexibility and reduce muscle tension."
            },
            {
                "day": "Saturday",
                "title": "Cardio & Core",
                "description": "Combine cardio exercises with core training today. Begin with a warm-up followed by light jogging, jumping jacks, mountain climbers, planks and abdominal exercises. Keep your movements controlled and take adequate rest between exercises. End the session with a proper cool-down."
            },
            {
                "day": "Sunday",
                "title": "Rest & Recovery",
                "description": "Take a complete rest day to allow your body to recover from the week's activities. You can do light walking or gentle stretching if you feel comfortable. Focus on hydration, healthy food and sufficient sleep so that your body is ready for the next week's workout."
            }
        ],

        "feedback": "Great job completing your weekly fitness activities. Stay consistent with your workout routine and focus on performing every exercise with proper form. If you feel tired or uncomfortable, take additional rest and adjust the workout intensity according to your fitness level.",

        "your_updates": "Your workout progress is updated based on your completed activities. Continue following your weekly plan and gradually improve your strength, endurance and flexibility. Regular exercise, proper nutrition, hydration and good sleep will help you achieve better results.",

        "progress": "Weekly Progress: You have completed a balanced combination of strength training, cardio, core exercises and recovery sessions. Continue tracking your workouts each week to understand your progress and maintain consistency.",

        "next_steps": "Next Steps: Continue with the workout schedule and gradually increase the duration or intensity when you feel comfortable. Maintain healthy eating habits, drink enough water and get adequate sleep. Review your progress regularly and update your fitness goals when needed."
    }