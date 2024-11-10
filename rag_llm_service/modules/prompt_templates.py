from langchain.prompts import ChatPromptTemplate

def quiz_generate_list_of_topics(self, topic: str):
        messages = [
            ("system", """
            You are an AI language model assistant with expertise in educational content creation.
            Your task is to generate a concise, quiz-appropriate list of core topics to be covered in a short quiz based on a given query.
            This quiz should evaluate the user's level of knowledge in the specified area, helping to assess their understanding effectively.
            
            Please ensure that:
            1. The list covers only the essential concepts, foundational theories, and significant subtopics relevant to the quiz scope.
            2. The topics are ordered in a way that reflects a logical progression from basic to more advanced aspects as suitable for a short assessment.
            3. You include any commonly misunderstood or challenging  topics that are critical for a thorough assessment.
            4. The quiz should be designed to take approximately 5-10 minutes to complete.
            5. The output should be succinct but sufficiently detailed to guide the creation of a well-rounded, focused quiz.

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
        questions = prompt_template.invoke({"topic":topic})

        return(questions)

def quiz_generate_list_of_questions(self, topic: str):
        messages = [
            ("system", """
            You are an AI language model assistant with expertise in educational content creation.
            Your task is to generate a set of multiple-choice questions for a quiz based on a given topic.
            The purpose of the quiz is to asses the level of the student.
            Assign points to each question: 1 for easy, 2 for medium and 3 for advanced.
            Ensure that the total number of questions is appropriate for a quiz that can be completed in just a few minutes.

            Please ensure that:
            1. Each question is clear and concise, focusing on key concepts related to the topic.
            2. The difficulty levels are assigned appropriately, reflecting the complexity of each question.
            3. The questions collectively cover a broad range of the topic's subfields to provide a comprehensive assessment.
            4. Questions are appropriate to the topic, for technical topics ask technical questions, for more general or humanistic topics ask more theoretical questions.
            5. If the type of exam for which the student is preparing has been specified, the questions should be from the exam range.

            Provide the output in the following format:
            1. Question: [Your question here]
            Points: [1, 2, or 3]
            a) [Option A]
            b) [Option B]
            c) [Option C]
            d) [Option D]
            Correct Answer: [a, b, c, or d]
            """),
            ("human","""Based on the following topic, generate a comprehensive list of questions for a short quiz:
            Topic: {topic}
            Ensure that the quiz can be completed within a few minutes and covers key concepts, foundational knowledge, 
            and commonly misunderstood areas in a logical progression. 
            The goal is to assess the user's level of knowledge effectively.
            Provide the output as a numbered list of questions with points, possible answers and the correct answer.""")
        ]

        prompt_template = ChatPromptTemplate.from_messages(messages)
        questions = prompt_template.invoke({"topic":topic})

        return(questions)    


''' 
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
'''