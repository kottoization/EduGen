from langchain.prompts import ChatPromptTemplate

def quiz_generate_list_of_questions(self, user_query: str) -> str:
        messages = [
            ("system", """
            You are an AI language model assistant with expertise in educational content creation.
            Your task is to generate a comprehensive and balanced list of topics to be covered in a short quiz based on a given query.
            This quiz should evaluate the user's level of knowledge in the specified area and should help assess their understanding effectively.
            
            Please ensure that:
            1. The list covers the core concepts, foundational theories, and important subtopics related to the given query.
            2. The topics are ordered in a way that reflects a logical progression from basic to more advanced aspects.
            3. You include any commonly misunderstood or tricky topics that are critical for a thorough assessment.
            4. The quiz should be designed to take approximately 5-10 minutes to complete.
            5. The output should be concise but sufficiently detailed to guide the creation of a well-rounded quiz.

            Generate the output as a numbered list of topics.
            """),
            ("human","""Based on the following topic, generate a comprehensive list of topics for a short quiz:
            Topic: {topic}
            Ensure that the quiz can be completed within 5-10 minutes and covers key concepts, foundational knowledge, 
            and commonly misunderstood areas in a logical progression. 
            The goal is to assess the user's level of knowledge effectively.
            Provide the output as a numbered list of topics.""")
        ]

        prompt_template = ChatPromptTemplate.from_messages(messages)
        prompt = prompt_template.invoke({"topic":user_query})

        return(prompt)