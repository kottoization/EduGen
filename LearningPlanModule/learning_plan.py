import datetime
from langchain.llms import OpenAI  # Ensure you have the appropriate LLM integration

class LearningPlan:
    def __init__(self, user_name, quiz_results=None, user_goals=None):
        self.user_name = user_name
        self.quiz_results = quiz_results if quiz_results else {}
        self.user_goals = user_goals if user_goals else {}
        self.learning_plan = []
        self.llm = OpenAI()  # Initialize your LLM instance

    def analyze_quiz_results(self):
        """
        Analyze quiz results and classify topics based on knowledge gaps.
        """
        critical_areas = []  # Score below 50%
        moderate_areas = []  # Score between 50% and 70%
        good_areas = []      # Score above 70%

        for topic, score in self.quiz_results.items():
            if score < 50:
                critical_areas.append(topic)
            elif 50 <= score < 70:
                moderate_areas.append(topic)
            else:
                good_areas.append(topic)

        return critical_areas, moderate_areas, good_areas

    def generate_plan(self):
        """
        Generate a learning plan based on quiz analysis.
        """
        critical_areas, moderate_areas, good_areas = self.analyze_quiz_results()
        plan_start_date = datetime.date.today()
        plan = []

        # Critical areas (High priority)
        for i, topic in enumerate(critical_areas):
            plan.append({
                'date': plan_start_date + datetime.timedelta(days=i * 2),
                'priority': 'High priority',
                'topic': topic,
                'materials': self.recommend_materials(topic)
            })

        # Moderate areas (Medium priority)
        offset = len(critical_areas)
        for i, topic in enumerate(moderate_areas, start=offset):
            plan.append({
                'date': plan_start_date + datetime.timedelta(days=i * 2),
                'priority': 'Medium priority',
                'topic': topic,
                'materials': self.recommend_materials(topic)
            })

        # Good areas (Low priority)
        offset += len(moderate_areas)
        for i, topic in enumerate(good_areas, start=offset):
            plan.append({
                'date': plan_start_date + datetime.timedelta(days=i * 2),
                'priority': 'Low priority',
                'topic': topic,
                'materials': self.recommend_materials(topic)
            })

        self.learning_plan = plan
        return plan

    def recommend_materials(self, topic):
        """
        Retrieve recommended materials for a given topic using LLM.
        """
        prompt = f"Provide a list of recommended study materials for learning {topic}."
        response = self.llm(prompt)
        materials = response.split('\n')  # Assuming each material is on a new line
        return materials

    def generate_plan_from_prompt(self, user_input):
        """
        Generate a learning plan based on user's custom input.
        """
        plan_start_date = datetime.date.today()
        plan = []

        goals = user_input.get("goals", [])
        for i, goal in enumerate(goals):
            plan.append({
                'date': plan_start_date + datetime.timedelta(days=i * 2),
                'priority': 'User-defined',
                'topic': goal,
                'materials': self.recommend_materials(goal)
            })

        self.learning_plan = plan
        return plan

    def display_plan(self):
        """
        Display the generated learning plan.
        """
        print(f"Learning Plan for {self.user_name}:\n")
        for entry in self.learning_plan:
            print(f"Date: {entry['date']}")
            print(f"Topic: {entry['topic']}")
            print(f"Priority: {entry['priority']}")
            print("Recommended Materials:")
            for material in entry['materials']:
                print(f" - {material}")
            print("\n")